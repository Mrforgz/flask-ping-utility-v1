import flask
import os 
import subprocess
import os
output = ("log.txt")
app = flask.Flask(__name__, template_folder='templates',static_folder='static')
@app.route('/')
def home():
    return flask.render_template('scanner.html')
@app.route('/scan', methods=['POST'])
def scan():
 subnet = flask.request.form['subnet'] 
 response = subprocess.call(["ping", "-n", "1", subnet])
 if response == 0:
  status = ("ONLINE")
 else:
   status = "offline"
 with open(output,"a") as f:
   f.write(f"-----------------------------\n")
   f.write(f"ping started at {subnet}\n")
   f.write(f"{subnet}\n is {status}\n")
   f.write(f"-----------------------------end\n")
 return flask.render_template('scanner.html', response=response, scanned_ip=subnet)
if __name__ == '__main__':
 app.run(debug=True)