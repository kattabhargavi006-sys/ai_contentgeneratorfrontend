import streamlit as st
import requests

st.title("Ai Content Generator",
st.write("Generate Blogs, LinkedIn Posts, Captions, Emails and more")
)
topic = st.text_input(
    "Enter Topic"
)
technology= st.selectbox(
    "select technology",
    [
        "python",
        "sql",
        "react",
        "java script",
        "node js",
        "AI",
        "GenAi"
    ]
)
content_type =st.selectbox(
    "content type",
    [
        "instagram post",
        "linkedin  caption",
        "email"
        "youtube description"
    ]
)
tone = st.selectbox(
    "tone",
    [
        "Professional",
        "Technical",
        "Friendly",
        "Casual",
        "Marketing""
    ]
)
generate = st.button(" Generate Content")
if generate:
    if topic =="":
        st.warning("please enter topic")
    else:
         with st.spinner("Generating Content..."):
           response=requests.post(
            f"{backend_url}/generate",
            params{
                "topic": topic,
                    "technology": technology,
                    "content_type": content_type,
                    "tone": tone
                 }
           )
           st.write("Status Code:", response.status_code)
            st.write("Response Text:", response.json()["content"])

            st.success("Content Generated Successfully")

            st.subheader("Generated Content")
