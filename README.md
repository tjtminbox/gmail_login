# Gmail Auto Login

This application provides automated Gmail login functionality through both a web interface and a Selenium script.

## Account Information
- Email: thomas@vocerpay.xyz
- Password: Katasandi01

## Features

1. **Web Application**
   - Interactive web interface
   - One-click automated login
   - Real-time status updates
   - Automatic redirection to Gmail

2. **Selenium Script**
   - Standalone Python script for local use
   - Detailed logging
   - Error handling with screenshots
   - Headless browser support

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the web application:
```bash
python app.py
```

3. Or run the standalone script:
```bash
python gmail_login.py
```

## Deployment

This application can be deployed to platforms that support Python web applications. Here are the steps for deploying to Heroku:

1. Create a new Heroku app:
```bash
heroku create gmail-auto-login
```

2. Add buildpacks:
```bash
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver
```

3. Set environment variables:
```bash
heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google-chrome
heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver
```

4. Deploy:
```bash
git push heroku main
```

## Files

- `app.py`: Flask web application
- `gmail_login.py`: Standalone Selenium script
- `requirements.txt`: Python dependencies
- `Procfile`: Deployment configuration

## Notes

- The web application requires a server with Chrome/Chromium installed
- For security, consider implementing proper authentication and credential management
- The application runs Chrome in headless mode on the server

## GitHub Pages

The static version of this application is available at:
https://tjtminbox.github.io/gmail_login/

## Web Application Version

The full web application version with automated login is available at:
[Your deployed application URL]
