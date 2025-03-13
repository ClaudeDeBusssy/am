from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.example.com")
# Locate and fill in a form field
input_field = driver.find_element_by_id("field-id")
input_field.send_keys("Your desired value")
# Example actions
size_button = driver.find_element_by_id("size-button")
size_button.click()

checkout_button = driver.find_element_by_id("checkout-button")
checkout_button.click()

# Fill in shipping information
name_input = driver.find_element_by_id("name-input")
name_input.send_keys("John Doe")

# ...
# Wait for an element to be clickable
checkout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkout-button"))
)
