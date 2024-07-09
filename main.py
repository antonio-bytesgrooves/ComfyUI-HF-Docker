import os
import logging
from flask import Flask, render_template, request
import subprocess
import server
import shutil

isFile = False

# Path of persistent storage
comfyui_install_path = "/data/app"
entry_comfy_literals = "/data/app/custom_nodes/ComfyLiterals/"
target_comfy_literals = "/data/app/web/extensions/ComfyLiterals/"


entry_file_path = os.path.join(comfyui_install_path,"main.py")
custom_nodes_path = os.path.join(comfyui_install_path,"custom_nodes")
requirements_file_path = os.path.join(comfyui_install_path,"requirements.txt")

# ComfyUI Github repository url 
comfyui_repo_url = "https://github.com/comfyanonymous/ComfyUI.git"

# Check if installed
sFile = os.path.isfile(entry_file_path)

print(f"Copying")
shutil.copytree(entry_comfy_literals, target_comfy_literals)
print(f"Copied file from... {target_comfy_literals} to {target_comfy_literals}")
    
if sFile:
    print("Found ComfyUI installation, Starting ComfyUI......")
    os.system(f"pip install -r {requirements_file_path}")
    os.system(f"python {entry_file_path} --listen 0.0.0.0 --port 7860")
else:
    print(f"ComfyUI installation not found!!")
    print(f"Cloning from {comfyui_repo_url} .....")
    os.system(f"git clone {comfyui_repo_url} {comfyui_install_path}")
    print(f"Starting ComfyUI App......")
    os.system(f"python {entry_file_path} --listen 0.0.0.0 --port 7860")
