import os
import logging
from flask import Flask, render_template, request
import subprocess
import server

isFile = False

# Path of persistent storage
comfyui_install_path = "/data"

entry_file_path = os.path.join(comfyui_install_path,"main.py")
custom_nodes_path = os.path.join(comfyui_install_path,"custom_nodes")
# ComfyUI Github repository url 
comfyui_repo_url = "https://github.com/comfyanonymous/ComfyUI.git"

# Check if installed
sFile = os.path.isfile(entry_file_path)

if sFile:
    print("Starting ComfyUI...")
    subprocess.run(["python", f"{entry_file_path}", "--listen 0.0.0.0 --port 7860"])
else:
    print(f"ComfyUI installation not found. cloning from {comfyui_repo_url}")
    #subprocess.run("waitress-serve","--host=0.0.0.0","--listen=0.0.0.0:7860","--ident=ComfyUI-SV1")
    os.system("python /data/app/main.py --listen 0.0.0.0 --port 7860 --cpu")
    #server.start_server()
    #subprocess.run(["gunicorn", "-b", "0.0.0.0:7860", "main:app"])

    # if sFile:
    #     subprocess.run(["python", f"{entry_file_path}", "--listen 0.0.0.0 --port 7860 --cpu-only"])
    # else:
    #     print("App not installed")