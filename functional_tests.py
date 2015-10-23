from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_page_titles(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('EKL Kinnisvara', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Rentnikud', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Sisesta rentniku nimi'
            )

        inputbox.send_keys('Silver')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Silver')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Esta')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Silver')
        self.check_for_row_in_list_table('2: Esta')


        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

