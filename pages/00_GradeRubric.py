#from openai import OpenAI
import streamlit as st
import ollama
from time import sleep
from utilities.icon import page_icon
from utilities.promptUtils import promptStringFromFiles
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required, but unused
)
selected_model = "Llama3.1:latest"

st.title("ChatGPT-like clone")
testPrompt =  promptStringFromFiles('prompts/prompt1.txt', 'prompts/essay.txt', "prompts/rubric.txt")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 



if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt  + " " + testPrompt})
    with st.chat_message("user"):
        st.markdown(prompt + " " + testPrompt)

    with st.chat_message("assistant"):
        with st.spinner("model working..."):
                    #the chat client is created withe the selected model, and the message, taking content from somewere
                    stream = client.chat.completions.create(
                        model=selected_model,
                        messages=[
                            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
                        ],
                        stream=True,
                    )
                # stream response
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})


