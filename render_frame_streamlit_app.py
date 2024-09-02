import streamlit as st
import subprocess
import streamlit.components.v1 as components
import socket

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

st.title('Hello, World!')
st.write('This is my first Streamlit app!')

port = find_free_port()
# Start the Streamlit app in a separate process
subprocess.Popen(["streamlit", "run", "temp_streamlit_app.py", f"--server.port={port}"])

st.header('Streamlit App Preview')
components.iframe(src=f"http://localhost:{port}", height=600, scrolling=True)