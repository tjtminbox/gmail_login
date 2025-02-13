from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Login credentials
EMAIL = "thomas@vocerpay.xyz"
PASSWORD = "Kurangkuat12"

def wait_and_find_element(driver, by, value, timeout=20):
    """Wait for an element to be present and return it"""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, value)))

def wait_and_click(driver, by, value, timeout=20):
    """Wait for an element to be clickable and click it"""
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable((by, value)))
    driver.execute_script("arguments[0].click();", element)

def login_gmail():
    # Setup Chrome options
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Suppress console logs
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
        wait_and_click(driver, By.CSS_SELECTOR, "#identifierNext button")
        
        # Wait for password field and enter password
        print("Waiting for password field...")
        time.sleep(2)  # Short pause to let the transition complete
        password_field = wait_and_find_element(driver, By.NAME, "Passwd", timeout=30)
        print("Entering password...")
        password_field.clear()
        password_field.send_keys(PASSWORD)
        
        # Click Next after password
        print("Clicking Next after password...")
        wait_and_click(driver, By.CSS_SELECTOR, "#passwordNext button")
        
        # Wait for Gmail to load - try multiple possible elements
        print("Waiting for Gmail to load...")
        success = False
        try:
            # Try different possible elements that indicate successful login
            selectors = [
                'div[role="main"]',
                '.nH',  # Gmail main container
                'div[aria-label="Main"]',
                '.ain'  # Inbox container
            ]
            
            for selector in selectors:
                try:
                    wait_and_find_element(driver, By.CSS_SELECTOR, selector, timeout=10)
                    success = True
                    break
                except (TimeoutException, NoSuchElementException):
                    continue
            
            if success:
                print("Successfully logged in!")
                print("\nLogin completed successfully!")
                print(f"Email: {EMAIL}")
                print("Password: " + "*" * len(PASSWORD))
            else:
                print("Could not verify successful login, but the process completed.")
                
        except Exception as e:
            print(f"Error while verifying login: {str(e)}")
            driver.save_screenshot("login_state.png")
            print("Current page state saved as 'login_state.png'")
        
        print("\nKeeping browser open for 30 seconds...")
        time.sleep(30)

    except Exception as e:
        print(f"\nAn error occurred during the login process: {str(e)}")
        try:
            driver.save_screenshot("error_screenshot.png")
            print("Error screenshot saved as 'error_screenshot.png'")
        except:
            print("Could not save error screenshot")
    
    finally:
        print("\nClosing browser...")
        driver.quit()

if __name__ == "__main__":
    print("Starting Gmail login automation...")
    print(f"\nAttempting to login with:")
    print(f"Email: {EMAIL}")
    print("Password: " + "*" * len(PASSWORD))
    print("\nStarting login process...")
    login_gmail()
