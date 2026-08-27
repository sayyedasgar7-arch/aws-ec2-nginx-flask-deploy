from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Ye mera Flask app AWS EC2 pe chal raha hai, Nginx ke through!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
