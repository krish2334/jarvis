import os
import eel
import subprocess

eel.init("style.css")

# Browser Open Karne ke liye
try:
    subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe", "--app=http://localhost:8000/index.html"])
except FileNotFoundError:
    print("Error: Microsoft Edge not found!")

os.system('start msedge.exe --app="http: // localhost:8000/index.html"')

# Eel start
eel.start('index.html', mode=None, host='localhost', block=True)

import eel
import webbrowser

eel.init("www")

# Manually Browser Open
webbrowser.open("http://localhost:8000/index.html")

eel.start('index.html', mode=None, host='localhost', block=True)

