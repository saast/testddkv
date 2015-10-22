from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        browser.quit()


    def test_page_titles(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('EKL Kinnisvara', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()

