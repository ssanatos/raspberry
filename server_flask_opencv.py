from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    str = "Hello World!"
    return str

# host가 ip. 다른데서도 막 접속하게 0.0.0.0 ---
# 저 플라스크를 서버인양 동작하기
app.run(host = '0.0.0.0', port = '8000')
# 실행하면 터미널에 나오는 IP 클릭해서 들어가기.

import cv2 as cv
def capture_frame():
    # /dev/video
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('webcam',frame)
        cv.waitKey(1)
        pass
    return

import threading
if __name__ == '__main__':
    cap_thread = threading.Thread(target = capture_frame)
    cap_thread.daemon = True
    cap_thread.start()
    cap_thread.join()
    app.run(host='0.0.0.0', port='8000')