from django.core.urlresolvers import  resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from kv.models import Tenant

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
        request.POST['tenant_lastname'] = 'Rentnik'

        response = home_page(request)

        self.assertEqual(Tenant.objects.count(), 1)
        new_tenant = Tenant.objects.first()
        self.assertEqual(new_tenant.lastname, 'Rentnik')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['tenant_lastname'] = 'Rentnik'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_displays_all_list_tenants(self):
        Tenant.objects.create(lastname = 'Üks')
        Tenant.objects.create(lastname = 'Kaks')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('Üks', response.content.decode())
        self.assertIn('Kaks', response.content.decode())



    def test_home_page_save_tenant_only_when_necessary(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertEqual(Tenant.objects.count(), 0)




class IterModelTest(TestCase):
    def test_sending_and_reciving_tenants(self):
        first_tenant = Tenant()
        first_tenant.lastname = 'First tenant lastname'
        first_tenant.save()

        second_tenant = Tenant()
        second_tenant.lastname = 'Sec lastname'
        second_tenant.save()

        saved_tenants = Tenant.objects.all()
        self.assertEqual(saved_tenants.count(), 2)

        first_saved_tenant = saved_tenants[0]
        second_saved_tenant = saved_tenants[1]
        self.assertEqual(first_saved_tenant.lastname, 'First tenant lastname')
        self.assertEqual(second_saved_tenant.lastname, 'Sec lastname')





















