from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser.implicitly_wait(1)

    def tearDown(self):
        #self.browser.refresh()
        self.browser.quit()

    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_home_page_automatic_redirect_to_tenant(self):
        self.browser.get(self.live_server_url)
        current_url = self.browser.current_url
        self.assertRegex(current_url, '/tenants/')



    def test_tenant(self):
        self.browser.get(self.live_server_url)
        self.assertIn('EKL Kinnisvara', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Rentnikud', header_text)

        tenant_url = self.browser.current_url
        self.assertRegex(tenant_url, '/tenants/')

        inputbox = self.browser.find_element_by_id('id_new_tenant')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Sisesta rentniku nimi'
            )

        inputbox.send_keys('Silver')
        inputbox.send_keys(Keys.ENTER)

        tenant_url = self.browser.current_url
        self.assertRegex(tenant_url, '/tenants/[0-9]+/')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Rentnik', header_text)
        tenant_name = self.browser.find_element_by_id('tenant_name')
        self.assertEqual('Silver', tenant_name.text)

        self.browser.get(self.live_server_url + '/tenants/')

        self.check_for_row_in_table('1: Silver')

        inputbox = self.browser.find_element_by_id('id_new_tenant')
        inputbox.send_keys('Esta')
        inputbox.send_keys(Keys.ENTER)

        self.assertRegex(tenant_url, '/tenants/[0-9]+/')

        self.browser.get(self.live_server_url + '/tenants/')

        self.check_for_row_in_table('1: Silver')
        self.check_for_row_in_table('2: Esta')

# TEGEMATA
# muuda rentniku
# kinnisvara otsing

#        self.fail('Finish the test!')

    def test_estate(self):
        # lähen kinnisvara lehele
        self.browser.get(self.live_server_url + '/estates/')
        # on kinnisvara lehel
        estate_url = self.browser.current_url
        self.assertRegex(estate_url, '/estates/+')

        self.assertIn('EKL Kinnisvara', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Kinnisvara', header_text)

        # seal on lisa uus input
        inputbox = self.browser.find_element_by_id('id_new_estate')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Sisesta kinnisvara aadress'
            )

        # lisa uus kinnisvara
        inputbox.send_keys('Pärnu mnt 28')
        inputbox.send_keys(Keys.ENTER)
# TEGEMATA
# kontolli kas läheb õigele lehele

        # all näitab kõiki siiani lisatud kinnisvarasid
        self.check_for_row_in_table('1: Pärnu mnt 28')

        # lisa teine kinnisvara
        inputbox = self.browser.find_element_by_id('id_new_estate')
        inputbox.send_keys('Koidu 11')
        inputbox.send_keys(Keys.ENTER)

        # näitab mõlemat kinnisvara
        self.check_for_row_in_table('1: Pärnu mnt 28')
        self.check_for_row_in_table('2: Koidu 11')

# TEGEMATA
# Muuda kinnisvara




    def test_contract(self):
        pass
        # lisa rentnik ja kinnisvara
        # mine vaata rentniku andmeid
        # lisa talle leping
        # vaata, et läks õigele aadressile /contracts/id/
        # vaata, et rentnikule lisandus leping

        # vaata, kas kinnisvara nimekirjas on tekkinud kinnisvarale juurde üks rentnik





