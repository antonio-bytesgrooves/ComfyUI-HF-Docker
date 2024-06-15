import os
import logging
import subprocess
import server

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
    server.start_server()
    
    # if sFile:
    #     subprocess.run(["python", f"{entry_file_path}", "--listen 0.0.0.0 --port 7860 --cpu-only"])
    # else:
    #     print("App not installed")