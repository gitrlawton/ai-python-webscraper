import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching chrome browser...")
    
    # Location of our chrome driver.
    chrome_driver_path = "./chromedriver.exe"
    # How our chrome driver should operate.
    options = webdriver.ChromeOptions()
    # Set up the driver using Google Chrome.
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        # Use the driver to visit the website.
        driver.get(website)
        print("Page loaded...")
        # Extract the html from the webpage.
        html = driver.page_source
        
        return html
    finally:
        driver.quit()


## ---- Cleaning the DOM content of things like script or style tags to --- ##
## --- reduce the amount of characters/tokens we need to send to the LLM -- ##

# Helper function to extract the body from the HTML content.
def extract_body_content(html_content):
    # Create an HTML parser using BeautifulSoup to parse the HTML content.
    soup = BeautifulSoup(html_content, "html.parser")
    # Extract the body from the HTML parser.
    body_content = soup.body
    
    if body_content:
        # Return the body content as a string.
        return str(body_content)
    
    return ""

# Helper function to clean the body content.
def clean_body_content(body_content):
    # Create an HTML parser to parse the body content.
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Get rid of each script and style tag in the body content.
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    # Extract the text from the HTML content, separating elements 
    # by a newline character.    
    cleaned_content = soup.get_text(separator="\n")
    # Remove leading and trailing whitespace from each line of text, 
    # and join non-empty lines back together with newline characters in between.
    cleaned_content = "\n".join(
            line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
    
    return cleaned_content

# Helper function to split the content up into batches to send to the LLM.
def split_dom_content(dom_content, max_length=6000):
    # Grab the first 6000 characters, and continue iterating until you reach 
    # the length of the dom_content.
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]