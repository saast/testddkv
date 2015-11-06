from django.core.urlresolvers import  resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from kv.models import Tenant, Estate

from kv.views import home_page, estates_page, tenants_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_root_url_redirects_to_tenant_page_view(self):
        request = HttpRequest()
        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/tenants/')




class TenantPageTest(TestCase):
    def test_tenants_url_resolves_to_tenant_page_view(self):
        found = resolve('/tenants/')
        self.assertEqual(found.func, tenants_page)


    def test_tenants_page_returns_correct_html(self):
        request = HttpRequest()
        response = tenants_page(request)
        expected_html = render_to_string('tenants.html')
        self.assertEqual(response.content.decode(), expected_html)




class TenantViewTest(TestCase):
    def test_displays_all_tenants(self):
        Tenant.objects.create(lastname = 'Üks')
        Tenant.objects.create(lastname = 'Kaks')

        response = self.client.get('/tenants/')

        self.assertContains(response, 'Üks')
        self.assertContains(response, 'Kaks')


    def test_view_tenants_uses_tenants_template(self):
        response = self.client.get('/tenants/')
        self.assertTemplateUsed(response, 'tenants.html')


    def test_view_tenant_uses_tenant_template(self):
        tenant = Tenant()
        tenant.lastname = 'First tenant lastname'
        tenant.save()

        response = self.client.get('/tenants/' + str(tenant.id) + '/')
        self.assertTemplateUsed(response, 'tenant.html')




class NewTenantTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
            '/tenants/new',
            data={'tenant_lastname':'Rentnik'}
            )
        self.assertEqual(Tenant.objects.count(), 1)
        new_tenant = Tenant.objects.first()
        self.assertEqual(new_tenant.lastname, 'Rentnik')


    def test_redirects_after_POST(self):
        response = self.client.post(
            '/tenants/new',
            data={'tenant_lastname':'Rentnik'}
            )
        self.assertRedirects(response, '/tenants/')




class EstatePageTest(TestCase):
    def test_estate_url_rsolves_to_estate_page_view(self):
        found = resolve('/estates/')
        self.assertEqual(found.func, estates_page)


    def test_estate_page_returns_correct_html(self):
        request = HttpRequest()
        response = estates_page(request)
        expected_html = render_to_string('estates.html')
        self.assertEqual(response.content.decode(), expected_html)


    def test_estates_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['estate_address'] = 'Estate 1'

        response = estates_page(request)

        self.assertEqual(Estate.objects.count(), 1)
        new_estate = Estate.objects.first()
        self.assertEqual(new_estate.address, 'Estate 1')


    def test_estates_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['estate_address'] = 'Address 33'

        response = estates_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/estates/')


    def test_estates_page_displays_all_list_estates(self):
        Estate.objects.create(address = 'Üks')
        Estate.objects.create(address = 'Kaks')

        request = HttpRequest()
        response = estates_page(request)

        self.assertIn('Üks', response.content.decode())
        self.assertIn('Kaks', response.content.decode())


    def test_estate_page_save_estate_only_when_necessary(self):
        request = HttpRequest()
        response = estates_page(request)
        self.assertEqual(Estate.objects.count(), 0)




class TenantAndEstateModelTest(TestCase):
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


    def test_sending_and_reciving_estates(self):
        first_estate = Estate()
        first_estate.address = 'Address 1'
        first_estate.save()

        second_estate = Estate()
        second_estate.address = 'Address 2'
        second_estate.save()

        saved_estates = Estate.objects.all()
        self.assertEqual(saved_estates.count(), 2)

        first_saved_estate = saved_estates[0]
        second_saved_estate = saved_estates[1]
        self.assertEqual(first_saved_estate.address, 'Address 1')
        self.assertEqual(second_saved_estate.address, 'Address 2')





















