import cv2
import numpy as np
from flask import Flask, render_template_string
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

HTML = """
<!doctype html>
<html>
<body>
<h3>Camera Bridge</h3>

<video id="video" autoplay playsinline style="width:90vw;"></video>
<canvas id="canvas" style="display:none;"></canvas>

<script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>
<script>
const socket = io();
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

async function start(){
    const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: "environment" },
        audio: false
    });

    video.srcObject = stream;

    setInterval(()=>{
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video,0,0);

        canvas.toBlob(async (blob)=>{
            const buf = await blob.arrayBuffer();
            socket.emit("frame", buf);
        }, "image/jpeg", 0.8);

    }, 100);
}

start();
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@socketio.on("frame")
def handle_frame(data):
    np_arr = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if frame is not None:
        cv2.imshow("WSL Camera", frame)
        cv2.waitKey(1)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, ssl_context="adhoc")