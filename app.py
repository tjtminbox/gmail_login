from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

app = Flask(__name__)

# Login credentials
EMAIL = "thomas@vocerpay.xyz"
PASSWORD = "Katasandi01"

def login_gmail():
    # Setup Chrome options
    options = Options()
    options.add_argument('--headless=new')  # Run in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Navigate to Gmail login page
        driver.get('https://accounts.google.com/signin/v2/identifier?service=mail')
        
        # Wait for and enter email
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "identifier"))
        )
        email_field.clear()
        email_field.send_keys(EMAIL)
        
        # Click Next after email
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#identifierNext button"))
        )
        driver.execute_script("arguments[0].click();", next_button)
        
        # Wait for password field and enter password
        time.sleep(2)
        password_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "Passwd"))
        )
        password_field.clear()
        password_field.send_keys(PASSWORD)
        
        # Click Next after password
        password_next = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#passwordNext button"))
        )
        driver.execute_script("arguments[0].click();", password_next)
        
        # Wait for Gmail to load
        success = False
        selectors = [
            'div[role="main"]',
            '.nH',
            'div[aria-label="Main"]',
            '.ain'
        ]
        
        for selector in selectors:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                success = True
                break
            except (TimeoutException, NoSuchElementException):
                continue
        
        if success:
            return {"status": "success", "message": "Successfully logged in to Gmail"}
        else:
            return {"status": "unknown", "message": "Login process completed but could not verify success"}
            
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    finally:
        driver.quit()

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Gmail Auto Login</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    margin: 0;
                    background-color: #f5f5f5;
                }
                .container {
                    text-align: center;
                    padding: 20px;
                    background-color: white;
                    border-radius: 10px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    max-width: 90%;
                    width: 400px;
                }
                .button {
                    display: inline-block;
                    background-color: #4285f4;
                    color: white;
                    padding: 12px 24px;
                    text-decoration: none;
                    border-radius: 5px;
                    margin: 10px 0;
                    font-weight: bold;
                    border: none;
                    cursor: pointer;
                }
                .button:hover {
                    background-color: #357abd;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Gmail Auto Login</h1>
                <p>Click the button below to start the automated login process:</p>
                <button onclick="startLogin()" class="button">Start Auto Login</button>
                <p id="status"></p>
            </div>
            <script>
                function startLogin() {
                    document.getElementById('status').textContent = 'Starting login process...';
                    fetch('/login')
                        .then(response => response.json())
                        .then(data => {
                            if (data.status === 'success') {
                                document.getElementById('status').textContent = 'Success! Redirecting to Gmail...';
                                window.location.href = 'https://mail.google.com';
                            } else {
                                document.getElementById('status').textContent = 'Error: ' + data.message;
                            }
                        })
                        .catch(error => {
                            document.getElementById('status').textContent = 'Error: ' + error.message;
                        });
                }
            </script>
        </body>
    </html>
    '''

@app.route('/login')
def login():
    result = login_gmail()
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
