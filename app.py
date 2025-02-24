from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello guys,this is my messaage from webhook lets go junnon'

@app.route('/health')
def health():
    return 'Server is up and running'
