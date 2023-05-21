import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from webdriver_manager.firefox import GeckoDriverManager


class NewVisitorTest(LiveServerTestCase):
    """Тест нового посетителя"""
    MAX_WAIT = 10

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def tearDown(self) -> None:
        """демонтаж"""
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """подтверждение строки в таблице списка"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.XPATH, "//*[@class='list_table']")
                rows = table.find_elements(By.TAG_NAME, 'div')
                self.assertIn(row_text, [row.text for row in rows])
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > 10:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        self.browser.get(self.live_server_url)
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
        self.check_for_row_in_list_table('1: Купить перья павлина')
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys("Сделать мушку из павлиньих перьев")
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')