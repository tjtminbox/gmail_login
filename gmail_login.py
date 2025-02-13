from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Login credentials
EMAIL = "thomas@vocerpay.xyz"
PASSWORD = "Katasandi01"

def login_gmail():
    # Setup Chrome options
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Uncomment the line below if you want to run Chrome in headless mode
    # options.add_argument('--headless=new')

    print("Initializing Chrome driver...")
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 20)
    
    try:
        print("Navigating to Gmail login page...")
        # Navigate to Gmail login page
        driver.get('https://gmail.com')

        print("Entering email...")
        # Wait for and enter email
        email_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        email_field.clear()
        email_field.send_keys(EMAIL)
        
        print("Clicking Next after email...")
        # Click Next after email
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#identifierNext button'))
        )
        next_button.click()

        print("Entering password...")
        # Wait for and enter password
        password_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        password_field.clear()
        password_field.send_keys(PASSWORD)
        
        print("Clicking Next after password...")
        # Click Next after password
        password_next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#passwordNext button'))
        )
        password_next_button.click()

        # Wait for Gmail to load
        print("Waiting for Gmail to load...")
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.nH'))
        )
        
        print("Successfully logged in!")
        print("Keeping browser open for 10 seconds...")
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    print("Starting Gmail login automation...")
    login_gmail()
