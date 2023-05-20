import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def tearDown(self) -> None:
        """демонтаж"""
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """подтверждение строки в таблице списка"""
        table = self.browser.find_element(By.XPATH, "//*[@class='list_table']")
        rows = table.find_elements(By.TAG_NAME, 'div')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Your To-Do list', header_text)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить перья павлина')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Купить перья павлина')
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys("Сделать мушку из павлиньих перьев")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')


if __name__ == '__main__':
    unittest.main(warnings='ignore')