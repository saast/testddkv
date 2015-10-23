from django.core.urlresolvers import  resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from kv.models import Item

from kv.views import home_page

class HomePageTest(TestCase):
    def test_root_url_rsolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_lastname'] = 'New Rentnik'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.lastname, 'New Rentnik')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')


    def test_home_page_save_item_only_when_necessary(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertEqual(Item.objects.count(), 0)




class IterModelTest(TestCase):
    def test_sending_and_reciving_items(self):
        first_item = Item()
        first_item.lastname = 'First item lastname'
        first_item.save()

        second_item = Item()
        second_item.lastname = 'Sec lastname'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.lastname, 'First item lastname')
        self.assertEqual(second_saved_item.lastname, 'Sec lastname')





















