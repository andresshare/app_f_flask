from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'mensaje'



app.run(debug=True,port=8000)
