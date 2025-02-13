from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Login credentials
EMAIL = "thomas@vocerpay.xyz"
PASSWORD = "Katasandi01"

def login_gmail():
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    # Uncomment the line below if you want to run Chrome in headless mode
    # options.add_argument('--headless')

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Navigate to Gmail
        driver.get('https://accounts.google.com')

        # Wait for and enter email
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "identifier"))
        )
        email_field.send_keys(EMAIL)
        
        # Click Next
        next_button = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
        next_button.click()

        # Wait for and enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Passwd"))
        )
        password_field.send_keys(PASSWORD)
        
        # Click Next to login
        next_button = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
        next_button.click()

        # Wait for Gmail to load
        print("Successfully logged in!")
        
        # Keep the browser open for 10 seconds to see the result
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    login_gmail()
