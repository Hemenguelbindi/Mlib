from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    """Тест домашний страницы"""

    def test_root_url_resolves_to_home_page_view(self):
        """Тест: корневого url преобразуется в представление"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
