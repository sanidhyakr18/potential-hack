import streamlit as st
import cv2
from PIL import Image
import numpy as np
import tempfile
import time
import subprocess
from calculations import get_Score

def main():
    """Face Recognition App"""

    st.title("Kim Java Un project")

    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Movement recognition webapp</h2>
    </div>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    f = st.file_uploader("Upload file")
    if st.button("Recognise"):
        print("Yems")
        # cv2.imshow("oye",img)
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(f.read())
        vf = cv2.VideoCapture(tfile.name)

        stframe = st.empty()
        while vf.isOpened():
            ret, frame = vf.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            stframe.image(gray)
            time.sleep(0.002)

        g = get_Score("lookup_test.pickle")
        path = 'file.avi'
        g.calculate_Score(tfile.name ,"punch - side",path)

        vf = cv2.VideoCapture(path)

        stframe = st.empty()
        while vf.isOpened():
            ret, frame = vf.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            stframe.image(gray)
            time.sleep(0.002)

if __name__ == '__main__':
    main()
