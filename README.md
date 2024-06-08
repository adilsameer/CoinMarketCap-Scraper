Here's the revised README with the additional information:

---

## CoinMarketCap Scraper

### Introduction
This project is a Python-based web scraper that extracts data from CoinMarketCap for cryptocurrency coins. It showcases the My knowledge of object-oriented programming (OOP) principles and the Selenium library for web scraping. The scraped data is stored in JSON format for further analysis or usage.

### Features
- Scrapes various data points for a given cryptocurrency coin, including price, price change, market cap, volume, circulating supply, and more.
- Supports extracting contract information, official links, and social media links (currently under development).
- Utilizes headless browsing with Selenium for efficient web scraping.
- Stores scraped data in JSON files for further analysis or usage.

### Usage
1. Ensure you have Python installed on your system.
2. Install the required Python packages:
   ```bash
   pip install selenium webdriver_manager
   ```
3. Run the `main.py` file and follow the prompts to enter the name of the cryptocurrency coin you want to scrape.
   ```bash
   python main.py
   
   input coin
   ```
4. Once the scraping is complete, the scraped data will be stored in a JSON file named `<coin>_data.json` in the current directory.

### Note
- This project is a submission project that demonstrates the My proficiency in Python, Selenium, and object-oriented programming. It serves as a showcase of strong understanding of OOPs and Selenium, with an intermediate level of knowledge in REST API development.
- The project is still a work in progress. Currently, the scraper extracts basic data, and the functionality to extract official links and social media links is under development.
- Due to time constraints, Django (I am is still learning Django) and Celery (I have theoretical knowledge of AWS SQS) were not implemented for creating REST APIs and background task management, respectively. However, these can be added in future iterations of the project.
