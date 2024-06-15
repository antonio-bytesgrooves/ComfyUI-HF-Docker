import os
import logging

isFile = False

path = '/data/main.py'
sFile = os.path.isfile(path)

if sFile:
    print('python /data/main.py --listen 0.0.0.0 --port 7860')
    logging.info("ComfyUI installation found. Starting")
    logging.info("ComfyUI installation found. Starting")
else:
    logging.info("ComfyUI installation not found. pulling from 'https://github.com/antonio-bytesgrooves/ComfyUI-SV1.git'")
    print('git clone https://github.com/antonio-bytesgrooves/ComfyUI-SV1.git /data && python /data/main.py  --listen 0.0.0.0 --port 7860')