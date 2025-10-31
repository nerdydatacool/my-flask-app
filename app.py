from flask import Flask
app = Flask(__name__)
@app.route('/')

def home():
    return "Hello from Flask CI/CD via Docker on port 8080!"


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5050)


