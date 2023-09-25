from flask import Flask, jsonify, request
from flask_cors import CORS

import master_script

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
        return 'Hello World!'

@app.route('/new_run', methods = ['POST'])
def new_run():
    script_name = request.form['scriptName']
    sim_count = request.form['simCount']
    max_run_time = request.form['maxRunTime']
    email = request.form['userEmail']
    username = request.form['username']
    # code for calling simulation here

    output = master_script.master(username, email)
    output += "<br>" + script_name + " " + str(sim_count) + " " +  str(max_run_time) + " " + email + " " + username
    return output

@app.route('/new_run', methods = ['GET'])
def test():
       return 'Nothing to see here!'

@app.route("/verify_email_ses", methods=['POST'])
def verify_email_ses():
    if request.method == 'POST':
        email=request.json['email']

        output = master_script.verify_email_identity(email)
        return jsonify(output)


@app.route('/get_file', methods = ['POST'])
def get_file():
     #file = request.files['README']
     files_recieved = []
     for file_key in list(request.files.keys()):
          files_recieved.append(str(request.files[file_key]))
          
     ret = ", ".join(files_recieved)
     return "Recieved: " + ret

if __name__ == "__main__":
    app.run(debug = True)
