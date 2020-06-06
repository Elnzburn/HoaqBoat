import os
from pyfiglet import Figlet
from flask import Flask, send_file, jsonify
from subprocess import call
from sys import platform as _platform

f = Figlet(font='stop')
print(f.renderText('Avatar-Server'))

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

avatar_dir = "Avatars"  # no slash

# create avatars directory if it does not exist
if not os.path.exists(avatar_dir):
    os.makedirs(avatar_dir)

@app.route("/status")
def serverStatus():
    return jsonify({
        "response": 200,
        "status": 1
    })

@app.route("/<int:uid>")
def serveAvatar(uid):
    # Check if avatar exists
    if os.path.isfile("{}/{}.png".format(avatar_dir, uid)):
        avatarid = uid
    else:
        avatarid = -1

    # Serve actual avatar or default one
    return send_file("{}/{}.png".format(avatar_dir, avatarid))

@app.errorhandler(404)
def page_not_found(error):
    return send_file("{}/-1.png".format(avatar_dir))

# Run the server
app.run(host="0.0.0.0", debug=False, port=5000)
