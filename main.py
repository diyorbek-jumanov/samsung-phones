from flask import Flask, render_template
import json

imges = json.loads(open('data.json').read())

app = Flask(__name__)

@app.route('/')
def home():
    return imges[0]['name']


app.run(debug=True)