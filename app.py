from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<div style=\"text-align: center;\"><h1>Hello from Farouk!</h1><p>Welcome to my GCP Project.</p><p></p></div>'


if __name__ == "__main__":
    app.run(debug=True)