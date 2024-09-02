import streamlit as st
from streamlit.testing.v1 import AppTest
from unittest.mock import patch
import time

def test_main_python_streamlit():
    with patch('main.execute_python') as mock_execute_python:
        # Set up the mock response
        mock_execute_python.return_value = """
        Here's a sample Streamlit hello world application:

        ```python
        import streamlit as st

        def main():
            st.title("Hello, World!")
            st.write("Welcome to my Streamlit app!")

        if __name__ == "__main__":
            main()
        ```

        You can save this code in a file named `app.py` and run it using the command `streamlit run app.py`.
        """

        # Create an instance of AppTest
        at = AppTest.from_file("main_python_streamlit.py")

        # Run the app
        at.run()

        assert not at.exception

        # # Wait for app to load
        # time.sleep(2)

        # # Print all widget keys for debugging
        # print("Available widget keys:", at.get_widget_keys())

        # # Try to find the text input by a partial key match
        # text_inputs = at.get_widget_by_type(st.text_input)
        # if text_inputs:
        #     text_input = text_inputs[0]
        #     text_input.set_value("generate sample Streamlit helloworld application")
        # else:
        #     raise ValueError("No text input found in the app")

        # # Find and click the submit button
        # submit_button = at.get_widget_by_type(st.button)
        # if submit_button:
        #     submit_button[0].click()
        # else:
        #     raise ValueError("No button found in the app")

        # # Check if the mocked execute_python function was called
        # mock_execute_python.assert_called_once()

        # # Check if the response is displayed in the app
        # assert "Here's a sample Streamlit hello world application:" in at.get_text_data()
        # assert "import streamlit as st" in at.get_text_data()
        # assert "st.title(\"Hello, World!\")" in at.get_text_data()

if __name__ == "__main__":
    test_main_python_streamlit()
