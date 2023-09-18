from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.chrome.options import Options as ChromeOptions
from chromedriver_autoinstaller import install
from export_csv import export_csv
import time
install()

categories=["shop-sua-tam","bach-hoa-online-nuoc-lam-mem-vai","bach-hoa-online-nuoc-giat",
            "dau-goi-va-dau-xa","rua-tay","kem-danh-rang",
            "khu-mui-co-the","shop-ve-sinh-san-nha","bach-hoa-online-nuoc-rua-chen-bang-tay",
            "shop-ve-sinh-toilet","bach-hoa-online-cham-soc-dac-biet","dau-xa",
            "bach-hoa-online-chat-tay-da-nang","dau-goi-va-xa-toc-nam",
            "ban-chai-rang-chay-dien","ban-chai-rang","tay-te-bao-chet-toan-than",
            "dau-thay-ban-chai","khu-mui-nam","bach-hoa-online-nuoc-rua-chen-cho-may"]

def containGift(gift_element):
    child_elements = gift_element.find_elements(By.XPATH, "*")  # This XPath selects all child elements
    return len(child_elements) >= 3
# URL of the web page
base_url = "https://www.lazada.vn/{}/?unilever-cham-soc-gia-dinh-nang-tam-cuoc-song&from=wangpu&m=shop&q=All-Products"

# Set up Chrome WebDriver
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')  # Optional: Run headless (without opening a browser window)
driver = webdriver.Chrome(options=chrome_options)

# Lists to store data
all_prices = []
all_sold = []
all_names = []
all_reviews = []
all_gifts = []
all_categories = []


# Loop through the pages
for category in categories:
    url = base_url.format(category)
    # Navigate to the URL
    driver.get(url)
    for _ in range(10):
        driver.execute_script("window.scrollBy(0, 350)")
        time.sleep(1)
    WebDriverWait(driver,2)
    product_divs = driver.find_elements(By.CLASS_NAME, "Ms6aG")  # Replace with the actual class name
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
            pass  

        try:
            # Find and extract the "sold" element
            sold = product_div.find_element(By.CLASS_NAME, "_1cEkb").text
        except NoSuchElementException:
            pass 

        try:
            # Find and extract the "name" element
            name = product_div.find_element(By.CLASS_NAME, "RfADt").text
        except NoSuchElementException:
            pass  

        try:
            # Find and extract the "review" element
            review = product_div.find_element(By.CLASS_NAME, "qzqFw").text
        except NoSuchElementException:
            pass  
        
        try:
            gift = product_div.find_element(By.CSS_SELECTOR, ".ic-dynamic-badge.ic-dynamic-badge-text.ic-dynamic-badge-fc.ic-dynamic-group-2").text
        except NoSuchElementException:
            pass
        # Extract data from the current page and add it to the lists
        all_prices.append(price)
        all_sold.append(sold)
        all_names.append(name)
        all_reviews.append(review)
        all_gifts.append(gift)
        all_categories.append(category)
# Export the lists of data to a CSV file
export_csv(all_names,all_sold,all_prices,all_reviews,all_gifts,all_categories,"lazada.csv")
# Close the browser
driver.quit()