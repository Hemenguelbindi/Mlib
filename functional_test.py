import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class NewVisitorTest(unittest.TestCase):
    '''тест нового поситителя'''

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        self.browser('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail("Закончить тест!")

if __name__ == '__main__':
    unittest.main(warnings='ignore')