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


    filenames = os.listdir(script_dir)

    filenames = [filename for filename in filenames if filename not in blacklist_files and "pyc" not in filename and "swp" not in filename]
    filenames.sort()
    for filename in filenames:
        obj["script_list"].append(
            {
                "author": "Default",
                "pattern": filename,
                "filename": filename
            }
        )
    for item in obj["script_list"]:
        item_path = os.path.join(script_dir, item["filename"])
        file = open(item_path)
        name_line = file.readline().strip()
        pattern_line = file.readline().strip()
        if name_line[0] == "#" and pattern_line[0] == "#":
            name = name_line[2:]
            pattern = pattern_line[2:]
            item["author"] = name
            item["pattern"] = pattern


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