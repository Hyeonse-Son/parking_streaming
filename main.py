from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# camera = cv2.VideoCapture('rtsp://admin:1234556@10.252.29.21/stream0')  # use IP camera
# camera = cv2.VideoCapture(0) # use 0 for local webcam
# for local webcam use cv2.VideoCapture(0)


def area2_frames():  # generate frame by frame from camera
    camera = cv2.VideoCapture('rtsp://admin:1234556@10.252.73.31/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def area3_frames():  # generate frame by frame from camera
    camera = cv2.VideoCapture('rtsp://admin:1234556@10.252.73.32/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def area4_frames():  # generate frame by frame from camera
    camera = cv2.VideoCapture('rtsp://admin:1234556@10.252.11.37/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def area5_1_frames():  # generate frame by frame from camera
    camera= cv2.VideoCapture('rtsp://admin:1234556@10.252.11.34/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result



def area5_2_frames():  # generate frame by frame from camera
    camera= cv2.VideoCapture('rtsp://admin:1234556@10.252.11.35/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def area6_frames():  # generate frame by frame from camera
    camera= cv2.VideoCapture('rtsp://admin:1234556@10.252.11.38/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def area7_frames():  # generate frame by frame from camera
    camera= cv2.VideoCapture('rtsp://admin:1234556@10.252.11.36/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def area8_frames():  # generate frame by frame from camera
    camera= cv2.VideoCapture('rtsp://admin:1234556@10.252.11.40/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def area_visitor_frames():  # generate frame by frame from camera
    camera= cv2.VideoCapture('rtsp://admin:1234556@10.252.11.39/stream0')  # use IP camera

    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/parking_area2')
def parking_area2():
    return Response(area2_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/parking_area3')
def parking_area3():
    return Response(area3_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/parking_area4')
def parking_area4():
    return Response(area4_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/parking_area5_1')
def parking_area5_1():
    return Response(area5_1_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/parking_area5_2')
def parking_area5_2():
    return Response(area5_2_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/parking_area6')
def parking_area6():
    return Response(area6_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/parking_area7')
def parking_area7():
    return Response(area7_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/parking_area8')
def parking_area8():
    return Response(area8_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/parking_area_vistor')
def parking_area_vistor():
    return Response(area_visitor_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """KETI parking home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)