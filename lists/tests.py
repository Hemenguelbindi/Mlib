from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):
    """Тест домашний страницы"""
    def test_home_page_returns_correct_html(self):
        """Тест: домашная страница возвращает правильный html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_display_all_list_items(self):
        """Тест: отображаются все элементы списка"""
        Item.objects.create(text="itemey 1")
        Item.objects.create(text="itemey 2")

        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

    def test_can_save_a_POST_request(self):
        """Тест: можно сохранить post-запрос"""
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST_(self):
        """Тест: переадресует после Post-запроса"""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        """Тест: сохраняет элемент только когда нужно"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    """Тест: модели элемента списка """

    def test_saving_and_retrieving_item(self):
        """Тест: сохранения и получения элементов списка"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
