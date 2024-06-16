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
    os.system("python /data/app/main.py --listen 0.0.0.0 --port 7860 --cpu")
else:
    print(f"ComfyUI installation not found. cloning from {comfyui_repo_url}")
    os.system("python /data/app/main.py --listen 0.0.0.0 --port 7860 --cpu")
