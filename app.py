import subprocess

import streamlit as st

from setting import OPTIONS


def main():
    st.title("Streamlit App - Multiselection")
    options = st.multiselect("Select one or more options:", list(OPTIONS.keys()))
    op_list = [OPTIONS[x] for x in options]
    try:
        # Execute the Python script with the Excel file as an argument
        args = ["python", "main.py"] + op_list
        result = subprocess.run(args, capture_output=True, text=True)
        st.write("Execution output:")
        st.code(result.stdout, language="python")
    except Exception as e:
        st.error(f"Error executing the script: {e}")


if __name__ == "__main__":
    main()
