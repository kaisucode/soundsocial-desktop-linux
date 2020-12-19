
import time
import subprocess 

pipeline = "ffmpeg -f pulse -i default output.mp3"
p = subprocess.Popen(pipeline, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

time.sleep(3)
p.communicate(input=b'q')
p.terminate()

