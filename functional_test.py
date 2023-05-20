from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get('http://localhost:8000')

assert 'The install worked successfully! Congratulations!' in driver.title