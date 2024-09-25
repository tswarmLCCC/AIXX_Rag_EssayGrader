import ollama
import streamlit as st
from openai import OpenAI
from utilities.icon import page_icon
from utilities.promptUtils import promptStringFromFiles


MESSAGE_CONTAINER_HIEGHT = 250

st.set_page_config(
    page_title="Chat playground 2",
    page_icon="💬💬",
    layout="wide",
    initial_sidebar_state="expanded",
)


def extract_model_names(models_info: list) -> tuple:
    """
    Extracts the model names from the models information.

    :param models_info: A dictionary containing the models' information.

    Return:
        A tuple containing the model names.
    """

    return tuple(model["name"] for model in models_info["models"])


def main():
    """
    The main function that runs the application.
    """

    page_icon("💬💬")
    st.subheader("Ollama Playground 2", divider="red", anchor=False)

    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    )

    models_info = ollama.list()
    available_models = extract_model_names(models_info)

    if available_models:
        selected_model = st.selectbox(
            "Pick a model available locally on your system ↓", available_models
        )

    else:
        st.warning("You have not pulled any model from Ollama yet!", icon="⚠️")
        if st.button("Go to settings to download a model"):
            st.page_switch("pages/03_⚙️_Settings.py")


    rubric_comments = {
        "Content":  st.text_area("Essay Prompt", placeholder="Input essay title or question"),
        "Organization":  st.text_area("Rubric Prompt", placeholder="Input rubric")
    }


    message_container = st.container(height=MESSAGE_CONTAINER_HIEGHT, border=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar = "🤖" if message["role"] == "assistant" else "😎"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    promptString = promptStringFromFiles('prompts/prompt1.txt', 'prompts/essay.txt', "prompts/rubric.txt")
    promptString = "Enter a prompt here..."




    if essay_prompt := st.chat_input(promptString):
        try:
            st.session_state.messages.append(
                {"role": "user", "content": essay_prompt})

            #writing back the prompt to the message container 
            message_container.chat_message("user", avatar="😎").markdown(essay_prompt)
            

            with message_container.chat_message("assistant", avatar="🤖"):
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
            st.session_state.messages.append(
                {"role": "assistant", "content": response})

        except Exception as e:
            st.error(e, icon="⛔️")


if __name__ == "__main__":
    main()
