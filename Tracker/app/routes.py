# from control import fetch_data
# import control
from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index/')
def index():

    text = open('activity_log', 'r+')
    content = text.read()
    text.close()


    return render_template('index.html',title='Home', text = content)

   


@app.route('/devices', methods=['GET','POST'])
def devices():
    device_list = {}
    # projectpath = request.form['projectFilepath']

    # text = open('device_list', 'r+')
    # content = text.read()
    # text.close()

    with open("device_list") as f:
        for line in f:
            (key,value) = line.split(':')
            val = value.rstrip()
            device_list[key] = val


    if request.method == 'POST':
        # print('TEST')
        multi_dict = request.form
        # print(multi_dict)
        device_to_append = {}
        device_to_append = multi_dict.to_dict(flat = False)
        print(device_to_append)

        i = 0
        append_str = ""
        for entry in device_to_append:
            print('ENTRY: ' + entry)
            if entry  == 'reset_button':
                    f = open("device_list","w")
                    f.truncate(0)
                    f.close()
                    device_list = {}
                    return render_template('devices.html',device_list = device_list)


            if i is 0:
                append_str = append_str + device_to_append[entry][0] + ":"
            if i is 1:
                append_str = append_str + device_to_append[entry][0]
            i = i + 1
            # print(device_to_append[entry])
        f = open("device_list","a+")
        f.write(append_str + '\n')
        # print(device_list_append[Name])
        # print(append_str)
        f.close()
        with open("device_list") as f:
            for line in f:
                (key,value) = line.split(':')
                val = value.rstrip()
                device_list[key] = val
        return render_template('devices.html',device_list = device_list)



    return render_template('devices.html',title='Devices',device_list = device_list)



@app.route('/networkconfig')
def networkconfig():

    posts = [
        {
            

        }
    ]
    return render_template('networkconfig.html',title='Network Config')