from selenium import webdriver
import sqlite3
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Parser():
    def __init__(self, base, url):
        self.base = base
        self.url = url

    def setup(self):

        with sqlite3.connect(f"{self.base}.sqlite3") as db:
            cursor = db.cursor()
            cursor.executescript(
                '''CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY , count INTEGER, date DATE)''')
            print(cursor.execute("SELECT count, date FROM data").fetchall())
    def parse(self):
        options = Options()

        options.add_argument("--headless=new")

        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        el = driver.find_element(By.CLASS_NAME, 'rts-counter')

        count = int(el.text.replace(',',''))
        date = str(datetime.date.today())
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'rts-counter')))

        driver.quit()
        with sqlite3.connect(f"{self.base}.sqlite3") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO data(count, date) VALUES(?, ?)", (count, date))
        print(count, date)