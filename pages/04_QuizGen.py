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
QUIZ_PROMPT = "prompts/quizPrompt.txt"

url = "https://canconvert.k-state.edu/qti/"
st.write("CSV to QTI Conversion: [https://canconvert.k-state.edu/qti/](%s)" % url)

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required, but unused
)
selected_model = "Llama3.2:latest"

qp_text = "concepts related to if/else statements in python"

st.title("QuizGen")
quizInput = st.text_area("Generate a quiz based on this stub:", qp_text)

testPrompt =  promptStringFromFiles(BASE_PROMPT,ESSAY_PROMPT,RUBRIC_PROMPT)


basePrompt = getStringFromFile(QUIZ_PROMPT)
testPrompt = promptStringFromStrings(basePrompt, quizInput, "")





if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

subButton  = st.button("Create Quiz", type="primary")

fileOut = " "
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
        fileOut = response
    st.session_state.messages.append({"role": "assistant", "content": response})


#https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-file-streamlit
text_contents = '''
Foo, Bar
123, 456
789, 000
'''

# Different ways to use the API

#st.download_button('Download CSV', fileOut, 'text/csv')
# Create a sample DataFrame
#import pandas as pd
#df = pd.DataFrame({'Name': ['John', 'Mary'], 'Age': [25, 30]})

# Convert DataFrame to CSV
csv = fileOut

# Create download button
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='data.csv',
    mime='text/csv',
)