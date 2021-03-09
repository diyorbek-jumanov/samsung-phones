from flask import Flask, render_template
import json

imges_url = json.loads(open('data.json').read())

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html', title='home', content=imges_url)

@app.route('/<string:name>')
def S3(name='s3'):
    title = f'Samsung Galaxy {name}'
    data = imges_url[0]
    routes = name

    return render_template('phone.html', title=title, data=data, routes=routes)
    
# @app.route('/s4')
# def S4():
#     title = 'Samsung Galaxy S4'
#     data = imges_url[1]

#     return render_template('phone.html', title=title, data=data)
    
# @app.route('/s5')
# def S5():
#     title = 'Samsung Galaxy S5'
#     data = imges_url[2]

#     return render_template('phone.html', title=title, data=data)
    
# @app.route('/s6')
# def S6():
#     title = 'Samsung Galaxy S6'
#     data = imges_url[3]

#     return render_template('phone.html', title=title, data=data)
    
# @app.route('/s7')
# def S7():
#     title = 'Samsung Galaxy S7'
#     data = imges_url[4]

#     return render_template('phone.html', title=title, data=data)
    
# @app.route('/s8')
# def S8():
#     title = 'Samsung Galaxy S8'
#     data = imges_url[5]

#     return render_template('phone.html', title=title, data=data)
    
# @app.route('/s9')
# def S9():
#     title = 'Samsung Galaxy S9'
#     data = imges_url[6]

#     return render_template('phone.html', title=title, data=data)
    
# @app.route('/s10')
# def S10():
#     title = 'Samsung Galaxy S10'
#     data = imges_url[7]

#     return render_template('phone.html', title=title, data=data)
    
# @app.route('/s20')
# def S20():
#     title = 'Samsung Galaxy S20'
#     data = imges_url[8]

#     return render_template('phone.html', title=title, data=data)
    
# @app.route('/s21')
# def S21():
#     title = 'Samsung Galaxy S21'
#     data = imges_url[9]

#     return render_template('phone.html', title=title, data=data)
    

app.run(debug=True)