import streamlit as st
#from streamlit import cached

# Define input variables
#essay_prompt = st.text_area("Essay Prompt", placeholder="Input essay title or question")
#rubric_prompt = st.text_area("Rubric Prompt", placeholder="Input rubric")
#essay_prompt = st.text_area("Essay Prompt", placeholder="Input essay title or question")
#category = st.selectbox("Category", ["Literature", "History", "Science"])
#topic_suggests = st.checkbox("Show Topic Suggestions")

#if topic_suggests:
    # Generate topic suggestions based on category (not implemented yet)
#    pass

# Define rubric variables
#rubric_criteria = {
#    "Content": st.slider("Content Score", 0, 10, 5),
#    "Organization": st.slider("Organization Score", 0, 10, 5),
#    "Writing Style": st.slider("Writing Style Score", 0, 10, 5)
#}
rubric_comments = {
    "Essay":  st.text_area("Essay Prompt", placeholder="Input essay title or question"),
    "Rubric":  st.text_area("Rubric Prompt", placeholder="Input rubric")
}

# Display output window
if st.button("Submit"):
    # Generate output response based on input variables (not implemented yet)
    pass

st.title("Output Window")

someOtherText = "Does just anyting show up here?"
# Render output response here
output_response = ""
if st.button("Generate Response"):
    output_response = "Generated output response"
else:
    output_response = "Please submit the prompt and rubric to generate a response"

st.write(output_response)