import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

# 체크박스 만들기
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    img = img[:,::-1,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")
# 함수 통과한 후 실행
webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
#webrtc_streamer(key="sample")
