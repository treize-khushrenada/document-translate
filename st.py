import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("📄 Medical Report - AI Translation")
st.write(
    "Upload a document below and see it translated in bahasa malaysia "
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# Create an OpenAI client.
client = OpenAI(api_key= "sk-G5TeY33FO8xSMpqLXVpoOcIKFak7NfgLBLt3a92KNrT3BlbkFJ3NUYkhGjtSOci1X3UFaIAEYl_vvbahUo4iwWMlh80A")

# Let the user upload a file via `st.file_uploader`.
uploaded_file = st.file_uploader(
    "Upload a document (.txt or .md)", type=("txt", "md")
)

# Ask the user for a question via `st.text_area`.
# question = st.text_area(
#     "Now ask a question about the document!",
#     placeholder="Can you give me a short summary?",
#     disabled=not uploaded_file,
# )

if uploaded_file:

    # Process the uploaded file.
    document = uploaded_file.read().decode()

    def get_answer_from_model(document, client):
        messages = [
            {
                "role": "user",
                "content": f"Here's a document: {document} \n\n---\n\n translate it to Bahasa Malaysia. Return directly with the translated output in your answer",
            }
        ]
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=False,
        )
        return response.choices[0].message.content

    # Generate an answer using the OpenAI API.
    answer = get_answer_from_model(document, client)

    # Display the answer in the Streamlit app.
    st.markdown(answer)
