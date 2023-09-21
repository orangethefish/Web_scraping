from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from chromedriver_autoinstaller import install
from export_csv import export_csv
import time

# Install ChromeDriver if not already installed
install()

# List of categories to scrape
categories=["shop-sua-tam","bach-hoa-online-nuoc-lam-mem-vai","bach-hoa-online-nuoc-giat",
            "dau-goi-va-dau-xa","rua-tay","kem-danh-rang",
            "khu-mui-co-the","shop-ve-sinh-san-nha","bach-hoa-online-nuoc-rua-chen-bang-tay",
            "shop-ve-sinh-toilet","bach-hoa-online-cham-soc-dac-biet","dau-xa",
            "bach-hoa-online-chat-tay-da-nang","dau-goi-va-xa-toc-nam",
            "ban-chai-rang-chay-dien","ban-chai-rang","tay-te-bao-chet-toan-than",
            "dau-thay-ban-chai","khu-mui-nam","bach-hoa-online-nuoc-rua-chen-cho-may"]

# URL template for Lazada product categories
base_url = "https://www.lazada.vn/{}/?unilever-cham-soc-gia-dinh-nang-tam-cuoc-song&from=wangpu&m=shop&q=All-Products"

# Set up Chrome WebDriver with optional headless mode
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# Lists to store scraped data
all_prices = []
all_sold = []
all_names = []
all_reviews = []
all_gifts = []
all_categories = []

# Loop through each category and scrape data
for category in categories:
    url = base_url.format(category)
    # Navigate to the URL
    driver.get(url)
    
    # Scroll down the page to load more products
    for _ in range(10):
        driver.execute_script("window.scrollBy(0, 350)")
        time.sleep(1)
    
    WebDriverWait(driver, 2)  # You might want to use WebDriverWait for a specific purpose here
    
    # Find product divs
    product_divs = driver.find_elements(By.CLASS_NAME, "Ms6aG")
    
    for product_div in product_divs:
        # Initialize variables for each element with default values
        price = ""
        sold = ""
        name = ""
        review = ""
        gift = "No"
        
        try:
            # Find and extract the "price" element
            price = product_div.find_element(By.CLASS_NAME, "aBrP0").text
        except NoSuchElementException:
            pass  # Handle case where "price" element is not found
        
        try:
            # Find and extract the "sold" element
            sold = product_div.find_element(By.CLASS_NAME, "_1cEkb").text
        except NoSuchElementException:
            pass  # Handle case where "sold" element is not found

        try:
            # Find and extract the "name" element
            name = product_div.find_element(By.CLASS_NAME, "RfADt").text
        except NoSuchElementException:
            pass  # Handle case where "name" element is not found
        
        try:
            # Find and extract the "review" element
            review = product_div.find_element(By.CLASS_NAME, "qzqFw").text
        except NoSuchElementException:
            pass  # Handle case where "review" element is not found
        
        try:
            # Find and extract the "gift" element
            gift = product_div.find_element(By.CSS_SELECTOR, ".ic-dynamic-badge.ic-dynamic-badge-text.ic-dynamic-badge-fc.ic-dynamic-group-2").text
        except NoSuchElementException:
            pass  # Handle case where "gift" element is not found
        
        # Extracted data is added to respective lists
        all_prices.append(price)
        all_sold.append(sold)
        all_names.append(name)
        all_reviews.append(review)
        all_gifts.append(gift)
        all_categories.append(category)

# Export the collected data to a CSV file
export_csv(all_names, all_sold, all_prices, all_reviews, all_gifts, all_categories, "lazada.csv")

# Close the Chrome browser
driver.quit()
