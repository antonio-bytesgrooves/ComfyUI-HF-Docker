import os
import logging
import subprocess

isFile = False

# Path of persistent storage
comfyui_install_path = "/data"

entry_file_path = os.path.join(comfyui_install_path,"main.py")
custom_nodes_path = os.path.join(comfyui_install_path,"custom_nodes")
# ComfyUI Github repository url 
comfyui_repo_url = "https://github.com/antonio-bytesgrooves/ComfyUI-SV1.git"

# Check if installed
sFile = os.path.isfile(entry_file_path)

if sFile:
    print("Starting ComfyUI...")
    subprocess.run(["python", f"{entry_file_path}", "--listen 0.0.0.0 --port 7860 --cpu-only"])
else:
    print(f"ComfyUI installation not found. cloning from {comfyui_repo_url}")
    subprocess.run(["git", "clone", f"{comfyui_repo_url} {comfyui_install_path}"])
    subprocess.run(["git", "clone", "https://github.com/ltdrdata/ComfyUI-Manager.git", f"{custom_nodes_path}"])
    subprocess.run(["git", "clone", "https://github.com/antonio-bytesgrooves/Comfy-Terminal.git",f"{custom_nodes_path}"])
    subprocess.run(["git", "clone", "https://github.com/antonio-bytesgrooves/Chaosaiart-Nodes.git",f"{custom_nodes_path}"])
    subprocess.run(["git", "clone", "https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git",f"{custom_nodes_path}"])
    subprocess.run(["python", f"{entry_file_path}", "--listen 0.0.0.0 --port 7860 --cpu-only"])