import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

def scrape_website(website):
    print("Launching chrome browser...")
    
    # Location of our chrome driver.
    chrome_driver_path = "./chromedriver.exe"
    # How our chrome driver should operate.
    options = webdriver.ChromeOptions()
    # Set up the driver using Google Chrome.
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        # Use the driver.
        driver.get(website)
        print("Page loaded...")
        # Extract the html
        html = driver.page_source
        
        return html
    finally:
        driver.quit()