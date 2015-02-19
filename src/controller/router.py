__author__ = 'chrisshroba'

from flask import *
import subprocess
import os

from config import config

p = None

script_dir = config.get("script_dir")

blacklist_files = ["__init__.py",
                   "stairs.py",
                   "stairs.pyc"]

app = Flask(__name__,
            static_folder="../../web/",
            static_path=""
            )



@app.route("/maestro")
def maestro():
    obj = {
        "script_list": [

        ]
    }


    files = os.listdir(script_dir)

    files = [file for file in files if file not in blacklist_files and "pyc" not in file and "swp" not in file]
    files.sort()
    for file in files:
        obj["script_list"].append(
            {
                "author": "Default",
                "pattern": file,
                "filename": file
            }
        )
    return render_template("maestro.html", **obj)

@app.route("/api/run_file/<filename>")
def foo(filename):
    script_path = "%s%s" % (script_dir, filename)
    run(script_path)
    print "running %s" % script_path
    return "Success"

@app.route("/api/killall")
def killall_route():
    killall()
    return "Success"

def run(cmd):
    global p
    killall()
    p = subprocess.Popen("exec python2 " + cmd, stdout=subprocess.PIPE, shell=True)

def killall():
    global p
    try:
        p.kill()
    except:
        pass

app.run(port=4445, host="0.0.0.0")