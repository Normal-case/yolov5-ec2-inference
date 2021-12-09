import time
import detect

start = time.time()

detect.run(source='resize.jpg', imgsz=(640, 640), device='cpu')

print(f'inference time : {round((time.time() - start), 2)}s')