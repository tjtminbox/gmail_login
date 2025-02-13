# Gmail Quick Login

A simple web application that provides quick access to Gmail login with pre-filled credentials.

## Account Information
- Email: thomas@vocerpay.xyz
- Password: Katasandi01

## Features
- One-click Gmail login
- Pre-filled email address
- Clean, responsive interface
- Simple deployment

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Deployment

### Deploy to Heroku

1. Create a new Heroku app:
```bash
heroku create gmail-quick-login
```

2. Deploy the application:
```bash
git push heroku main
```

### Deploy to Render

1. Create a new Web Service
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

### Deploy to Railway

1. Create a new project
2. Connect your GitHub repository
3. The deployment will automatically use the Procfile

## Files
- `app.py`: Flask web application
- `requirements.txt`: Python dependencies
- `Procfile`: Deployment configuration

## GitHub Pages Version
A static version is available at:
https://tjtminbox.github.io/gmail_login/

## Web Application Version
The full web application is available at:
[Your deployed application URL]

## Notes
- The application uses Flask for serving the web interface
- Credentials are displayed on the interface for easy access
- The login link pre-fills the email address for convenience
