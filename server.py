"""
wolserver
Basic wake-on-lan server
server.py

Run (linux):
export FLASK_APP=server.py
flask run

"""

from flask import *
from wakeonlan import send_magic_packet

app = Flask(__name__, template_folder="templates")

# Devices
devices = {
    "hyperv": "78:45:c4:04:11:9b"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/wake-up/<device>')
def wake_up(device):
    macAddr = ""
    if device in devices.keys():
        macAddr = devices[device]
        send_magic_packet(macAddr)
    else:
        return "Failed to wake on lan... Bad device name/mac address combo"

    return "Sent wol packet! Device should be waking up"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=420, debug=True)
