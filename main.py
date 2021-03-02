from flask import Flask, render_template
import json

imges_url = json.loads(open('data.json').read())

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html', title='home', content=imges_url)

@app.route('/s3')
def S3():
    title = 'S3'
    data = imges_url[0]

    return render_template('phone.html', title=title, data=data)
    

app.run(debug=True)