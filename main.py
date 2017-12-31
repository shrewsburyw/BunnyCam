import cv2
import sys
from flask import Flask, render_template, Response
from camera import VideoCamera
import time


video_camera = VideoCamera(flip=False) # creates a camera object, flip vertically

# App Globals (do not edit)
app = Flask(__name__)
last_epoch = 0



@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
