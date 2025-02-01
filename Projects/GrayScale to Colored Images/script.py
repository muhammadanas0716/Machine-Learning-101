import os
import time
import requests
import base64
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Configuration
folder_name = 'datasetV0'
max_workers = 20  # Number of threads for faster downloading

# Create folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Set up headless Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in the background
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--log-level=3")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Google Images
search_query = "light blue sky and green trees"
driver.get("https://www.google.com/imghp?hl=en")

# Search for the query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(search_query)
search_box.submit()

# Wait for images to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.YQ4gaf")))
except:
    print("Images did not load. Exiting...")
    driver.quit()
    exit()

# Scroll to load all images
def scroll_to_end(driver, pause_time=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

scroll_to_end(driver)

# Extract image URLs
image_elements = driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")
print(f"Found {len(image_elements)} images. Starting download...")

# Function to download and save an image
def download_image(index, src):
    try:
        if src is None or src.strip() == "":
            return False  # Skip blank images

        # Handle Base64 images
        if src.startswith("data:image"):
            header, encoded = src.split(",", 1)
            img_data = base64.b64decode(encoded)
        else:
            img_data = requests.get(src, timeout=5).content

        # Check if image is blank (all white or transparent)
        img = Image.open(BytesIO(img_data))
        if img.getbbox() is None:
            return False  # Skip blank images

        # Save the image
        img.save(os.path.join(folder_name, f'image_{index}.jpg'))
        return True

    except Exception as e:
        return False

# Download images in parallel using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    tasks = []
    for index, img in enumerate(image_elements):
        src = img.get_attribute('src')
        tasks.append(executor.submit(download_image, index, src))

    downloaded_count = 0
    for task in tqdm(as_completed(tasks), total=len(tasks)):
        if task.result():
            downloaded_count += 1

print(f"Downloaded {downloaded_count} images into the '{folder_name}' folder.")

# Close the browser
driver.quit()
