from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Login credentials
EMAIL = "thomas@vocerpay.xyz"
PASSWORD = "Katasandi01"

def wait_and_find_element(driver, by, value, timeout=20):
    """Wait for an element to be present and return it"""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, value)))

def login_gmail():
    # Setup Chrome options
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--headless=new')  # Uncomment for headless mode

    print("Initializing Chrome driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        print("Navigating to Gmail login page...")
        driver.get('https://accounts.google.com/signin/v2/identifier?service=mail')
        
        # Wait for email field and enter email
        print("Entering email...")
        email_field = wait_and_find_element(driver, By.NAME, "identifier")
        email_field.clear()
        email_field.send_keys(EMAIL)
        
        # Click Next after email
        print("Clicking Next after email...")
        next_button = wait_and_find_element(driver, By.CSS_SELECTOR, "#identifierNext button")
        driver.execute_script("arguments[0].click();", next_button)
        
        # Wait for password field and enter password
        print("Waiting for password field...")
        time.sleep(2)  # Short pause to let the transition complete
        password_field = wait_and_find_element(driver, By.NAME, "Passwd", timeout=30)
        print("Entering password...")
        password_field.clear()
        password_field.send_keys(PASSWORD)
        
        # Click Next after password
        print("Clicking Next after password...")
        password_next = wait_and_find_element(driver, By.CSS_SELECTOR, "#passwordNext button")
        driver.execute_script("arguments[0].click();", password_next)
        
        # Wait for Gmail to load
        print("Waiting for Gmail to load...")
        try:
            wait_and_find_element(driver, By.CSS_SELECTOR, 'div[role="main"]', timeout=30)
            print("Successfully logged in!")
        except TimeoutException:
            print("Timeout waiting for Gmail to load, but login might have succeeded.")
        
        print("Keeping browser open for 30 seconds...")
        time.sleep(30)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Take a screenshot if there's an error
        try:
            driver.save_screenshot("error_screenshot.png")
            print("Error screenshot saved as 'error_screenshot.png'")
        except:
            print("Could not save error screenshot")
    
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    print("Starting Gmail login automation...")
    login_gmail()
