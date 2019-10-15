# from control import fetch_data
# import control
from app import app
from flask import render_template


@app.route('/')
@app.route('/index/')
def index():

    text = open('activity_log', 'r+')
    content = text.read()
    text.close()

    # control.fetch_data()
    activity = {
            'Jasper':'Reddit',
            'Harley':'Facebook'

        }
    return render_template('index.html',title='Home',activity = activity, text = content)

   


@app.route('/devices')
def devices():
    x = 0
    print('test')
    user = {'username':x}

    posts = [
        {
            'author':{'username':'Jasper'},
            'body':'Jasper labtop is visiting now'

        },
        {
            'author': {'username': 'Vicii'},
            'body': 'Vicii mobile is visiting now'
        }
    ]
    return render_template('devices.html',title='Devices',user=user,posts=posts)



@app.route('/networkconfig')
def networkconfig():

    posts = [
        {
            

        }
    ]
    return render_template('networkconfig.html',title='Network Config')