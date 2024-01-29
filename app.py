from flask import Flask, render_template, flash, redirect, url_for, request, session, jsonify
from flask_bcrypt import Bcrypt
import ssl


app = Flask(__name__, static_url_path='/static')
# Create an SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# Load the SSL certificate and key into the context
context.load_cert_chain('yourapp.crt', 'yourapp.key')

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playstore', methods=['POST','GET'])
def playstore():
    user_input = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        print(user_input)
    return render_template('playstore.html', user_input=user_input)


if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context=context)