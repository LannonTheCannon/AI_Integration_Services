import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url, timeout=60)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    # Page config
    st.set_page_config(page_title="InStack AI Chatbot Integration Services", page_icon="🤖", layout="wide")

    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    h1 {
        color: #2E86C1;
        font-size: 48px;
        text-align: center;
        margin-bottom: 30px;
    }
    h2 {
        color: #2874A6;
        font-size: 32px;
    }
    p {
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("Welcome to InStack AI Chatbot Integration Services")

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Revolutionize Your Customer Experience")
        st.write("""
        Our AI-powered chatbot solutions are designed to transform your customer interactions, 
        providing seamless support and engagement 24/7. With cutting-edge natural language 
        processing and machine learning algorithms, our chatbots understand and respond to 
        your customers' needs with unprecedented accuracy and efficiency.
        """)
        st.button("Get Started")

    with col2:
        lottie_url = "https://assets5.lottiefiles.com/packages/lf20_9e8yoqkm.json"
        lottie_animation = load_lottieurl(lottie_url)
        st_lottie(lottie_animation, height=300)

    # Features section
    st.header("Key Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📚 Natural Language Understanding")
        st.write("Our chatbots comprehend context and intent, providing accurate responses.")

    with col2:
        st.subheader("🔄 Seamless Integration")
        st.write("Easily integrate our chatbots with your existing systems and platforms.")

    with col3:
        st.subheader("📊 Analytics Dashboard")
        st.write("Gain valuable insights into customer interactions and chatbot performance.")

    # Call to action
    st.markdown("---")
    st.header("Ready to elevate your customer service?")
    if st.button("Contact Us"):
        st.success("Thanks for your interest! We'll be in touch soon.")

if __name__ == "__main__":
    main()
