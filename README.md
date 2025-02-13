# Gmail Login Automation

This repository contains two methods for Gmail login:

1. Quick Login Link (Web): https://tjtminbox.github.io/gmail_login/
2. Selenium Automation Script (Python)

## Account Information
- Email: thomas@vocerpay.xyz
- Password: Katasandi01

## Selenium Automation Setup

1. Install Python requirements:
```bash
pip install -r requirements.txt
```

2. Make sure you have Google Chrome installed on your computer

3. Run the automation script:
```bash
python gmail_login.py
```

The script will:
- Open Chrome browser
- Navigate to Gmail
- Automatically enter the email and password
- Log in to the account
- Keep the browser open for 10 seconds to show the result
- Close automatically

### Customization

You can modify `gmail_login.py` to:
- Run in headless mode (uncomment the headless option)
- Change the wait time after login
- Add additional automation steps

## Notes
- The script requires a stable internet connection
- Make sure no other automation is running on Chrome
- If you encounter any issues, check that Chrome is up to date
