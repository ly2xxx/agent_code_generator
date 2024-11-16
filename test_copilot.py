import streamlit as st
from streamlit.components.v1 import html

def render_copilot():
    html("""
        <div id="root" style="position: fixed; left: 0; top: 0; height: 100vh; width: 320px; z-index: 1000;"></div>
        <script src="http://localhost:4000/copilotkit/client.js"></script>
        <script>
            window.addEventListener('load', function() {
                const copilotEndpoint = 'http://localhost:4000/copilotkit';
                window.copilotKit = new CopilotKit({
                    endpoint: copilotEndpoint,
                });
                window.copilotKit.mount(document.getElementById('root'));
            });
        </script>
    """, height=1000, width=1000)  # Added explicit dimensions to ensure visibility

st.title("Hello World with Copilot Test")
st.write("This is a simple test page")
render_copilot()

st.write("If you see this text, Streamlit is working correctly")
