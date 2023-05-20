import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


class NewVisitorTest(unittest.TestCase):
    '''тест нового поситителя'''

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.NAME,'h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element(By.CLASS_NAME, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить перья павлина')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element(By.CLASS_NAME, 'id_list_table')
        rows = table.find_element('tr')
        self.assertTrue(any(row.text == '1: Купить павлиньи перья' for row in rows))
        self.fail("Закончить тест!")

if __name__ == '__main__':
    unittest.main(warnings='ignore')