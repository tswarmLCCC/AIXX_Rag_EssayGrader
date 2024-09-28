#from openai import OpenAI
import streamlit as st
import ollama
from time import sleep
from utilities.icon import page_icon
from utilities.promptUtils import promptStringFromFiles, promptStringFromStrings, getStringFromFile
from openai import OpenAI

BASE_PROMPT = 'prompts/programmingPrompt.txt'
ESSAY_PROMPT =  'prompts/essay.txt'
RUBRIC_PROMPT = "prompts/checkInRubric.txt"


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required, but unused
)
selected_model = "Llama3.1:latest"

st.title("ChatGPT-like clone")
testPrompt =  promptStringFromFiles(BASE_PROMPT,ESSAY_PROMPT,RUBRIC_PROMPT)


essayInput = st.text_area("Student Essay", getStringFromFile(ESSAY_PROMPT))
rubricInput = st.text_area("Rubric", getStringFromFile(RUBRIC_PROMPT))

basePrompt = getStringFromFile(BASE_PROMPT)
testPrompt = promptStringFromStrings(basePrompt, essayInput, rubricInput)

agree = st.checkbox("Retain History")

if not agree:
    st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

subButton  = st.button("Submit Student Essay", type="primary")

if subButton:
    st.session_state.messages.append({"role": "user", "content": " " + testPrompt})
    with st.chat_message("user"):
        st.markdown(" " + testPrompt)

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


