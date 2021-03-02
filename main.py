from flask import Flask, render_template
import json

imges_url = json.loads(open('data.json').read())

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html', title='home', content=imges_url)


app.run(debug=True)