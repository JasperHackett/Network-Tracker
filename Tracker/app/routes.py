# from control import fetch_data
# import control
from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index/')
#Displays device activity log
def index():

    text = open('activity_log', 'r+')
    content = text.read()
    text.close()


    return render_template('index.html',title='Home', text = content)

   


@app.route('/devices', methods=['GET','POST'])
def devices():
    device_list = {}


# Reading and writing to device list
    with open("device_list") as f:
        for line in f:
            (key,value) = line.split(':')
            val = value.rstrip()
            device_list[key] = val


    if request.method == 'POST':
        multi_dict = request.form
        device_to_append = {}
        device_to_append = multi_dict.to_dict(flat = False)

        i = 0
        append_str = ""
        for entry in device_to_append:
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
        f = open("device_list","a+")
        f.write(append_str + '\n')
        f.close()
        with open("device_list") as f:
            for line in f:
                (key,value) = line.split(':')
                val = value.rstrip()
                device_list[key] = val
        return render_template('devices.html',device_list = device_list)



    return render_template('devices.html',title='Devices',device_list = device_list)


# Page for setting network interface name
@app.route('/networkconfig', methods=['GET','POST'])
def networkconfig():
    nic_name = {}

    if request.method == 'POST':
        multi_dict = request.form

        nic_name = {}
        nic_name = multi_dict.to_dict(flat = False)

        i = 0
        append_str = ""
        for entry in nic_name:

            if i is 0:
                f = open("nic_id","w")
                f.truncate(0)
                f.write(nic_name[entry][0])
                f.close()
                append_str = append_str + nic_name[entry][0]
            i = i + 1



    return render_template('networkconfig.html',title='Network Config',nic_name = nic_name)