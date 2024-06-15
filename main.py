import os
import logging

isFile = False

# Path of persistent storage
comfyui_install_path = "/data"

entry_file_path = os.path.join(comfyui_install_path,"main.py")
custom_nodes_path = os.path.join(comfyui_install_path,"custom_nodes")
# ComfyUI Github repository url 
comfyui_repo_url = "https://github.com/antonio-bytesgrooves/ComfyUI-SV1.git"

# Check if installed
sFile = os.path.isfile(comfyui_install_path)

if sFile:
    print(f'python {comfyui_install_path} --listen 0.0.0.0 --port 7860 --cpu-only')
    logging.info("ComfyUI installation found. Starting")
else:
    logging.info(f"ComfyUI installation not found. cloning from {comfyui_repo_url}")
    print(f'git clone {comfyui_repo_url} {comfyui_install_path} && python {entry_file_path}  --listen 0.0.0.0 --port 7860 --cpu-only  \
          && git clone https://github.com/ltdrdata/ComfyUI-Manager.git {custom_nodes_path} \
          && git clone https://github.com/antonio-bytesgrooves/Comfy-Terminal.git {custom_nodes_path} \
          && git clone https://github.com/antonio-bytesgrooves/Chaosaiart-Nodes.git {custom_nodes_path} \
          && git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git {custom_nodes_path}')