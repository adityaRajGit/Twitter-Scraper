from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import uuid
import requests
from config import *
from pymongo import MongoClient

class TwitterScraper:
    def __init__(self):
        self.mongo_client = MongoClient(MONGO_URI)
        self.db = self.mongo_client.twitter_trends
        
    def get_proxy_ip(self):
        """Get current IP address through ProxyMesh"""
        proxy = f"http://{PROXYMESH_HOST}:{PROXYMESH_PORT}"
        response = requests.get('https://api.ipify.org', proxies={'http': proxy, 'https': proxy})
        return response.text

    def setup_driver(self):
        """Configure Chrome with proxy settings"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server={PROXYMESH_HOST}:{PROXYMESH_PORT}')
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def login_to_twitter(self, driver):
        """Handle Twitter login"""
        driver.get('https://twitter.com/login')
        wait = WebDriverWait(driver, 20)
        
        
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
        email_input.send_keys(TWITTER_EMAIL)
        email_input.submit()
        
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.submit()

    def get_trending_topics(self):
        """Scrape trending topics from Twitter"""
        driver = self.setup_driver()
        try:
            self.login_to_twitter(driver)
            wait = WebDriverWait(driver, 20)
            trends = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '[data-testid="trend"]')))[:5]
            
            
            trend_names = [trend.find_element(By.CSS_SELECTOR, 'span').text 
                         for trend in trends]
            
            current_ip = self.get_proxy_ip()
            
            trend_data = {
                'unique_id': str(uuid.uuid4()),
                'trend1': trend_names[0] if len(trend_names) > 0 else None,
                'trend2': trend_names[1] if len(trend_names) > 1 else None,
                'trend3': trend_names[2] if len(trend_names) > 2 else None,
                'trend4': trend_names[3] if len(trend_names) > 3 else None,
                'trend5': trend_names[4] if len(trend_names) > 4 else None,
                'timestamp': datetime.now(),
                'ip_address': current_ip
            }
            
            self.db.trends.insert_one(trend_data)
            return trend_data
            
        finally:
            driver.quit()