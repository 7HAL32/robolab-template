#!/usr/bin/env python3

'''
Simple stub that calls the 'real' deploy.py in the git submodule without an
additional path prefix. Passes along any parameters without modification.

For usage, optional arguments, syntax, et cetera please refer to the README.md
of this repository, the 'robolab-deploy' submodule or the RoboLab Docs which
are accessible through the campus network of TU Dresden via
http://robolab.inf.tu-dresden.de.

This module: https://github.com/7HAL32/robolab-template
The submodule: https://github.com/7HAL32/robolab-deploy

Part of the RoboLab project.
Released under the MIT License.
Copyright (c) 2017 Lutz Thies
'''

import sys
import subprocess
import urllib.request as urllib
import zipfile
import shutil
import os

# get the full executable path, because windows can't handle our shebang
PYTHON_EXECUTABLE = sys.executable
# it's basically a one-liner \o/
try:
    with open("./robolab-deploy/deploy.py") as f:
        pass
except FileNotFoundError:
    urllib.urlretrieve("https://github.com/7hal32/robolab-deploy/archive/master.zip", "master.zip")
    with zipfile.ZipFile("master.zip", "r") as zip_ref:
        zip_ref.extractall()
    os.rmdir("robolab-deploy")
    os.remove("master.zip")
    shutil.move("robolab-deploy-master", "robolab-deploy")
subprocess.call([PYTHON_EXECUTABLE,
                './robolab-deploy/deploy.py'] + sys.argv[1:])
