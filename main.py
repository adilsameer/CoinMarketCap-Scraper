import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_price_change(element):
    try:
        text = element.text
        percentage = float(text.split('%')[0])
        if element.get_attribute('data-change') == 'down':
            percentage = -percentage
        return percentage
    except Exception as e:
        print("An error occurred:", e)
        return None


class CoinMarketCap:

    BASE_URL = "https://coinmarketcap.com/currencies/"

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def scrape_coin(self, coin):
        url = f"{self.BASE_URL}{coin}/"
        self.driver.get(url)
        data = {}


        # Example of extracting data - adjust based on actual page structure
        data['price'] = float(
            self.get_element_text(By.XPATH, '//*[@id="section-coin-overview"]/div[2]/span').replace('$', '').replace(
                ',', ''))
        data['price_change'] = get_price_change(
            self.driver.find_element(By.CSS_SELECTOR, 'p[data-change][font-size="1"]'))
        data['market_cap'] = int(
            self.get_element_text(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[1]/div[1]/dd').split('$')[
                1].replace(',', ''))
        data['market_cap_rank'] = int(self.get_element_text(By.CLASS_NAME, 'slider-value.rank-value').replace('#', ''))
        data['volume'] = int(
            self.get_element_text(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[2]/div[1]/dd').split('$')[
                1].replace(',', ''))
        data['volume_rank'] = int(
            self.get_element_text(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[2]/div[2]/div/span').replace('#',
                                                                                                                   ''))
        data['volume_change'] = float(
            self.get_element_text(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[3]/div/dd').replace('%', ''))
        data['circulating_supply'] = int(
            self.get_element_text(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[4]/div/dd').split()[0].replace(
                ',', ''))
        data['total_supply'] = int(
            self.get_element_text(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[5]/div/dd').split()[0].replace(
                ',', ''))
        data['diluted_market_cap'] = int(
            self.get_element_text(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[7]/div/dd').split('$')[1].replace(
                ',', ''))

        data['contracts'] = self.get_contracts()

        data['official_links'] = self.get_official_links()

        data['socials'] = self.get_socials()

        return self.clean_output(data)

    def clean_output(self, data):
        cleaned_data = {}
        for key, value in data.items():
            if isinstance(value, str) and value.endswith('%'):
                cleaned_data[key] = float(value.replace('%', ''))
            elif isinstance(value, str) and value.startswith('$'):
                cleaned_data[key] = int(value.replace('$', '').replace(',', ''))
            elif isinstance(value, str) and value.startswith('#'):
                cleaned_data[key] = int(value.replace('#', ''))
            elif isinstance(value, str) and ' ' in value:
                cleaned_data[key] = int(value.split()[0].replace(',', ''))
            else:
                cleaned_data[key] = value

        return cleaned_data

    def get_element_text(self, by, selector):
        try:
            element = self.driver.find_element(by, selector)
            return element.text if element else None
        except Exception as e:
            print("An error occurred while getting element text:", e)
            return None

    def get_contracts(self):
        contracts = []
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR, '.chain-name')
            for element in elements:
                name = element.text.split(':')[0]
                href = element.get_attribute('href')
                address = href.split('/')[-1]
                contracts.append({'name': name, 'address': address})
        except Exception as e:
            print("An error occurred while getting contracts:", e)
        return contracts

    def get_official_links(self):
        links = []
        pass
        return links

    def get_socials(self):
        socials = []
        pass
        return socials

    def __del__(self):
        self.driver.quit()


def main():
    coin = input("Enter the name of the coin: ")
    scraper = CoinMarketCap()
    output = scraper.scrape_coin(coin)
    print({
        "coin": coin.upper(),
        "output": output
    })
    file_name = f"{coin.lower()}_data.json"
    with open(file_name, 'w') as f:
        json.dump(output, f, indent=4)

if __name__ == "__main__":
    main()
