import streamlit as st
from streamlit_lottie import st_lottie
import requests
from datetime import datetime, time, timedelta
import json
import os
from security import safe_requests

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    try:
        r = safe_requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except requests.exceptions.RequestException:
        return None

def load_scheduled_calls():
    if os.path.exists('scheduled_calls.json'):
        with open('scheduled_calls.json', 'r') as f:
            return json.load(f)
    return []

def save_scheduled_calls(calls):
    with open('scheduled_calls.json', 'w') as f:
        json.dump(calls, f, indent=2, default=str)

def save_user_info(company_name, contact_name, email, phone, preferred_date, preferred_time):
    scheduled_calls = load_scheduled_calls()
    scheduled_calls.append({
        "company_name": company_name,
        "contact_name": contact_name,
        "email": email,
        "phone": phone,
        "preferred_date": str(preferred_date),
        "preferred_time": preferred_time
    })
    save_scheduled_calls(scheduled_calls)

def generate_time_slots():
    start = time(9, 0)  # 9:00 AM
    end = time(21, 0)   # 9:00 PM
    slot_duration = timedelta(minutes=30)
    current = datetime.combine(datetime.today(), start)
    end = datetime.combine(datetime.today(), end)
    
    time_slots = []
    while current <= end:
        time_slots.append(current.time().strftime("%I:%M %p"))
        current += slot_duration
    
    return time_slots

def show_get_started_process():
    st.header("Getting Started with InStack AI Chatbots")
    st.write("Follow these simple steps to revolutionize your customer service:")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Discovery Call")
        st.write("We'll schedule a free 30-minute call to understand your business needs.")
        st.markdown("- Discuss your current customer service challenges")
        st.markdown("- Explore potential AI chatbot solutions")
        st.markdown("- Answer any questions you have about our services")
        
        st.subheader("2. Custom Proposal")
        st.write("Based on our discussion, we'll create a tailored proposal for your business.")
        st.markdown("- Outline recommended chatbot features")
        st.markdown("- Provide clear pricing and timeline")
        st.markdown("- Explain expected ROI and benefits")

    with col2:
        st.subheader("3. Design and Development")
        st.write("Once you approve the proposal, we'll start creating your custom AI chatbot.")
        st.markdown("- Develop chatbot dialogue flows")
        st.markdown("- Integrate with your existing systems")
        st.markdown("- Train the AI on your specific business knowledge")
        
        st.subheader("4. Launch and Support")
        st.write("We'll help you deploy the chatbot and provide ongoing support.")
        st.markdown("- Assist with smooth implementation")
        st.markdown("- Train your team on chatbot management")
        st.markdown("- Provide continuous optimization and updates")

    st.markdown("---")

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.subheader("Ready to transform your customer service?")
        if st.button("Schedule Your Discovery Call", key="discovery_call"):
            st.session_state.show_form = True

    # Display Lottie animation with fallback
    lottie_url = "https://lottie.host/a9b2d23a-a15d-428f-8ec5-75bebb3ac06b/MJUBDOzyzc.json"  # Example chatbot animation
    lottie_animation = load_lottieurl(lottie_url)
    if lottie_animation is not None:
        st_lottie(lottie_animation, height=300)
    else:
        st.image("https://via.placeholder.com/400x300.png?text=Getting+Started", caption="Getting Started")

def main():
    st.set_page_config(
        page_title="InStack AI Chatbots",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for a more modern look
    st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        color: #212529;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        font-size: 18px;
        border-radius: 25px;
        border: none;
        padding: 12px 30px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
    }
    h1, h2, h3 {
        color: #343a40;
    }
    .big-font {
        font-size: 24px !important;
    }
    .highlight {
        background-color: #e9ecef;
        padding: 20px;
        border-radius: 10px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Transform Your Customer Service with AI")
        st.markdown('<p class="big-font">Empower your small business with intelligent chatbots that understand and serve your customers 24/7.</p>', unsafe_allow_html=True)
        if st.button("Get Started"):
            st.session_state.show_get_started = True
    with col2:
        lottie_url = "https://lottie.host/08fb1d82-3f33-4381-a4ec-305710575a0f/zMgO7xHhQL.json"  # A more modern bot animation
        lottie_animation = load_lottieurl(lottie_url)
        if lottie_animation:
            st_lottie(lottie_animation, height=300)
        else:
            st.image("https://via.placeholder.com/400x300.png?text=AI+Chatbot", caption="AI Chatbot")

    # Get Started Process
    if st.session_state.get('show_get_started', False):
        show_get_started_process()
    else:
        # Key Benefits
        st.header("Why Choose InStack AI Chatbots?")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="card">
            <h3>🚀 Boost Efficiency</h3>
            <p>Handle multiple customer queries simultaneously, reducing wait times and improving satisfaction.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
            <h3>💰 Cut Costs</h3>
            <p>Reduce operational expenses by automating routine inquiries and support tasks.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="card">
            <h3>🔒 Ensure Consistency</h3>
            <p>Deliver uniform, accurate responses to customer queries, every time.</p>
            </div>
            """, unsafe_allow_html=True)

        # How It Works
        st.header("How InStack AI Chatbots Work")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="card">
            <h3>1. We Analyze</h3>
            <p>We study your business needs and customer interaction patterns.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
            <h3>2. We Customize</h3>
            <p>We design a chatbot tailored to your specific requirements.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="card">
            <h3>3. We Integrate</h3>
            <p>We seamlessly implement the chatbot into your existing systems.</p>
            </div>
            """, unsafe_allow_html=True)

        # Testimonial
        st.markdown("""
        <div class="highlight">
        <h3>What Our Clients Say</h3>
        <p><em>"InStack's AI chatbot has revolutionized our customer service. We're handling 50% more inquiries with 30% less staff time!"</em></p>
        <p>- Michael Han, CEO of Body RES Inc.</p>
        </div>
        """, unsafe_allow_html=True)

        # Call to Action
        st.header("Ready to Elevate Your Customer Service?")
        if st.button("Schedule Your Free Consultation"):
            st.session_state.show_form = True

    # Consultation Form
    if st.session_state.get('show_form', False):
        with st.form("consultation_form"):
            st.subheader("Schedule Your Discovery Call")
            company_name = st.text_input("Company Name")
            contact_name = st.text_input("Your Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            
            # Date selection (only allow Monday to Saturday)
            min_date = datetime.now().date() + timedelta(days=1)
            max_date = min_date + timedelta(days=30)  # Allow booking up to 30 days in advance
            
            while min_date.weekday() > 5:  # If it's Sunday, move to Monday
                min_date += timedelta(days=1)
            
            preferred_date = st.date_input(
                "Preferred Date", 
                min_value=min_date,
                max_value=max_date,
                value=min_date
            )
            
            # Only show time slots if a valid date is selected
            if preferred_date:
                if preferred_date.weekday() < 6:  # Monday to Saturday
                    time_slots = generate_time_slots()
                    preferred_time = st.selectbox("Preferred Time (PST)", time_slots)
                else:
                    st.warning("Please select a date from Monday to Saturday.")
            
            if st.form_submit_button("Confirm Discovery Call"):
                if company_name and contact_name and email and preferred_date and preferred_time:
                    if preferred_date.weekday() < 6:  # Ensure it's Monday to Saturday
                        save_user_info(company_name, contact_name, email, phone, preferred_date, preferred_time)
                        st.success(f"Thank you for scheduling a discovery call! We'll contact you shortly to confirm your appointment for {preferred_date.strftime('%A, %B %d, %Y')} at {preferred_time} PST.")
                        st.balloons()
                    else:
                        st.error("Please select a date from Monday to Saturday.")
                else:
                    st.error("Please fill out all required fields.")

if __name__ == "__main__":
    main()
