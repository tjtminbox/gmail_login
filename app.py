from flask import Flask, jsonify, redirect
import os

app = Flask(__name__)

# Login credentials
EMAIL = "thomas@vocerpay.xyz"

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Gmail Quick Login</title>
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
                .credentials {
                    margin: 20px 0;
                    padding: 15px;
                    background-color: #f8f9fa;
                    border-radius: 5px;
                    text-align: left;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Gmail Quick Login</h1>
                <div class="credentials">
                    <p><strong>Email:</strong> thomas@vocerpay.xyz</p>
                    <p><strong>Password:</strong> Katasandi01</p>
                </div>
                <p>Click the button below to go to Gmail login:</p>
                <a href="/login" class="button">Quick Login</a>
            </div>
        </body>
    </html>
    '''

@app.route('/login')
def login():
    # Redirect to Gmail with pre-filled email
    return redirect(f'https://accounts.google.com/AccountChooser?Email={EMAIL}&continue=https://mail.google.com/mail/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
