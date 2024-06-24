import streamlit as st
import openai
from openai import OpenAI

api_key = "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"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

st.set_page_config(page_title="NemoTron Chatbot", page_icon="🤖")

st.title("NemoTron Chatbot by NVIDIA (340B)")
st.markdown("""
Welcome to the NemoTron Chatbot interface! This chatbot uses the power of NVIDIA's 340B model to generate responses.\n
Enter your message in the text box below and get instant responses.
""")

def get_response_from_openai(prompt):
    messages = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model="meta/llama3-70b-instruct",
        messages=messages,
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )
    return completion

st.write("Type your message and press Enter:")

st.sidebar.title("NemoTron Chatbot")
st.sidebar.markdown("""
    Welcome to the NemoTron Chatbot interface! This chatbot uses the power of NVIDIA's 340B model to generate responses.
    Enter your message in the text box below and get instant responses.
""")

# Input prompt from the user
user_input = st.text_input("User:", placeholder="Type your message here...")

if user_input:
    response_placeholder = st.empty()
    response_text = ""

    with st.spinner("Generating response..."):
        for chunk in get_response_from_openai(user_input):
            if chunk.choices[0].delta.content is not None:
                response_text += chunk.choices[0].delta.content
                response_placeholder.text_area("Chatbot:", value=response_text, height=400, max_chars=None)

st.markdown("""
---
**Disclaimer:** This is a demo chatbot powered by NVIDIA's 340B model. The responses are generated by an AI and might not always be accurate.
""")

st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9;
        color: #333333;
        font-size: 16px;
    }

    .st-ba {
        background-color: #222831;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 15px;
        font-size: 15px;
    }
    </style>
    <div class="footer">
        © 2024 Naman Labhsetwar.
    </div>
    """, unsafe_allow_html=True
)
