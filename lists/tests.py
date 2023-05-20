from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    """Тест домашний страницы"""
    def test_home_page_returns_correct_html(self):
        """Тест: домашная страница возвращает правильный html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')