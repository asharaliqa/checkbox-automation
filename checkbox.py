import unittest
from selenium import webdriver

class TestCheckbox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.example.com")
        self.checkbox = self.driver.find_element_by_id("checkbox")
    
    def test_checkbox(self):
        # Verify checkbox is not selected
        self.assertFalse(self.checkbox.is_selected(), "Checkbox is selected by default")
        
        # Select checkbox
        self.checkbox.click()
        
        # Verify checkbox is selected
        self.assertTrue(self.checkbox.is_selected(), "Checkbox is not selected after clicking")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
