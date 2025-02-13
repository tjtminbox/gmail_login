# Gmail Quick Login

A simple web application that provides quick access to Gmail login with pre-filled credentials.

## Account Information
- Email: thomas@vocerpay.xyz
- Password: Katasandi01

## Features
- One-click Gmail login
- Pre-filled email address
- Device-specific handling (Android/iOS/Desktop)
- Clean, responsive interface

## Firebase Deployment Instructions

1. Install Firebase CLI:
```bash
npm install -g firebase-tools
```

2. Login to Firebase:
```bash
firebase login
```

3. Initialize Firebase project:
```bash
firebase init
```
Select:
- Hosting
- Use existing project or create new
- public directory: `public`
- Single-page app: No
- GitHub actions: No

4. Deploy to Firebase:
```bash
firebase deploy
```

Your application will be available at:
`https://gmail-quick-login.web.app`

## Local Testing

To test locally before deployment:
```bash
firebase serve
```

## Project Structure
```
├── public/
│   └── index.html    # Main application page
├── firebase.json     # Firebase configuration
└── .firebaserc      # Firebase project settings
```

## How It Works
1. Click the "Quick Login" button
2. Automatically redirects to Gmail login
3. Email is pre-filled
4. Enter password: Katasandi01
5. Access Gmail

## Device Support
- Android: Opens in Gmail app or browser
- iOS: Opens in Gmail app
- Desktop: Opens in browser

## Notes
- The application uses pure HTML/JavaScript
- No backend required
- Fast and reliable
- Secure (uses official Google login)
