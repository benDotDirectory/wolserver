# wolserver
Lightweight self-hosted wake-on-lan server written in python/flask.

## install
Install this on a device on your network that is always on, like a raspberry pi

```
# Dependancies
$ sudo apt install python3 python3-pip git
# Install app
$ git clone https://github.com/benDotDirectory/wolserver.git ~/wolserver
$ cd ~/wolserver
$ sudo pip3 install flask wakeonlan
# Run an instance
$ sudo python3 server.py
# It is recomended to run from a process scheduler, though
$ sudo npm install pm2 -g # Install pm2 process scheduler globally. You need nodejs/npm installed to use this
$ sudo pm2 start ~/wolserver/server.py --name "wolserver"
# Make sure it ran without errors
$ sudo pm2 status
```

## add devices
Edit ```server.py``` and add your devicename and mac address to the 'devices' variable.

## wake a device
Go to ```http://host_ip:port/deviceName``` in the browser

## to do
- improve documentation
- html5 ui
- clean up code
- shutdown/uptime reporting agent for local machines
- ui to add/remove devices
