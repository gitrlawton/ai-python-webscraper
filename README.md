# AI Web Scraper

## Overview

This project is an AI-powered web scraper built using Python, Streamlit, and various libraries for web scraping and natural language processing. The application allows users to input a URL, scrape the DOM content of the webpage, and parse specific information based on user-provided prompts.

## Features

- **Web Scraping**: Utilizes Selenium to navigate to a specified URL and extract the HTML content.
- **Content Cleaning**: Cleans the scraped HTML to remove unnecessary tags (like `<script>` and `<style>`) and formats the text for easier processing.
- **Information Extraction**: Uses the Langchain library to interact with the Ollama LLM for extracting specific information based on user prompts.
- **User Interface**: Built with Streamlit, providing an interactive web interface for users to input URLs and view results.

## Installation

To set up the project, ensure you have Python installed on your machine. Then, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the Chrome WebDriver installed and available in your system's PATH. Alternatively, you can add the driver executable directly to the project directory. You can download it from [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable).

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Enter a website URL in the input field and click the "Scraper Site" button to scrape the content.

4. After scraping, you can describe what you want to parse in the "Describe what you want to parse" text area and click the "Parse Content" button to extract the relevant information.

## File Descriptions

- **main.py**: The main application file that handles user input, scraping, and displaying results.
- **scrape.py**: Contains functions for scraping websites, cleaning HTML content, and splitting content into manageable chunks.
- **parse.py**: Defines the logic for parsing the cleaned content using the Ollama LLM based on user descriptions.
- **requirements.txt**: Lists the necessary Python packages for the project.

## Dependencies

- **Streamlit**: For creating the web interface.
- **Langchain**: For managing prompts and interactions with the LLM.
- **Langchain Ollama**: For utilizing the Ollama LLM for parsing tasks.
- **Selenium**: For web scraping and browser automation.
- **BeautifulSoup4**: For parsing and cleaning HTML content.
- **lxml, html5lib**: For additional HTML parsing capabilities.
- **python-dotenv**: For managing environment variables.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
