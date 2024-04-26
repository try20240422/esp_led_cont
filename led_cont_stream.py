import streamlit as st
import requests

st.title('LED Controller')

node_mcu_ip = "100.76.25.209"  # インターネットIPアドレス（外部IPアドレス）に置き換えてください42.151.114.219

def send_command(path):
    url = f"http://{node_mcu_ip}:81{path}"  # ポート番号をURLに含める
    try:
        response = requests.get(url)
        if response.status_code == 200:
            st.success('Command was successful')
        else:
            st.error('Failed to execute command')
    except Exception as e:
        st.error(f'Error: {str(e)}')

if st.button('Turn LED ON'):
    send_command("/led/on")

if st.button('Turn LED OFF'):
    send_command("/led/off")
