from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()

try:
    # Have user log in
    driver.get("https://app.joinhandshake.com/login")

    # wait until user logs in
    WebDriverWait(driver, float("inf")).until(EC.url_contains("explore"))

    # find url (depends on school)
    current = driver.current_url
    current = current.split('/')
    docs_url = current[0] + '//' + current[2] + "/docs"

    # go to documents page
    driver.get(docs_url)
    wait = WebDriverWait(driver, 10)
    
    # get all document links from table
    wait.until(EC.presence_of_element_located((By.XPATH, "//table")))
    count = 0
    while True:
        try:
            link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//table//a[contains(@href, 'docs')]")))
        except TimeoutException:
            break
        
        link.click()

        actions_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Actions')]")))
        actions_button.click()

        edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Edit')]")))
        edit_button.click()

        delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Delete')]")))
        delete_button.click()

        confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='dialog']//button[contains(text(), 'Delete')]")))
        confirm_delete.click()
        count += 1

    print(f"All done! Successfully deleted {count} documents.")

except TimeoutException as e:
    print(f"Timeout waiting for element: {str(e)}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    time.sleep(5)
    driver.quit()