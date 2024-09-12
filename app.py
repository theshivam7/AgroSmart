import streamlit as st
import io
from PIL import Image
import base64
from dotenv import load_dotenv
import os
from openai import OpenAI
from streamlit_option_menu import option_menu
import time

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI API client with the custom base URL
client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

def main():
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1B5E20;
        text-align: center;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        font-weight: bold;
    }
    .feature-header {
        color: #2E7D32;
        font-size: 1.8rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 0.5rem;
        font-weight: bold;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #45a049;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .stSelectbox > div > div > div {
        background-color: #E8F5E9;
        border-radius: 5px;
        border: 1px solid #81C784;
    }
    .stTextInput > div > div > input {
        border-radius: 5px;
        border: 1px solid #81C784;
        background-color: #E8F5E9;
    }
    .stTextInput > div > div > input:focus {
        box-shadow: 0 0 0 2px #4CAF50;
    }
    .stSlider > div > div > div > div {
        background-color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-header'>AgroSmart: Your Free Crop Diagnosis and Treatment App</h1>", unsafe_allow_html=True)

    # Horizontal menu
    selected = option_menu(
        menu_title=None,
        options=["Diagnose Crop", "Find Treatment", "Expert Advice", "Maximize Yields", "Best Deals", "Sell Produce"],
        icons=["plant", "bandaid", "chat-square-text", "graph-up", "cart", "cash-coin"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#E8F5E9"},
            "icon": {"color": "#2E7D32", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#C8E6C9",
                "color": "#1B5E20",
                "font-weight": "bold",
            },
            "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
        }
    )
    
    if selected == "Diagnose Crop":
        diagnose_crop()
    elif selected == "Find Treatment":
        find_treatment()
    elif selected == "Expert Advice":
        expert_advice()
    elif selected == "Maximize Yields":
        maximize_yields()
    elif selected == "Best Deals":
        best_deals()
    elif selected == "Sell Produce":
        sell_produce()

    # Footer
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1B5E20;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        color: #E8F5E9;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class='footer'>
        <p>© 2024 AgroSmart India | Made with ❤️ by <a href="https://www.linkedin.com/in/theshivam7/">Shivam 🍁</a> | 
        <a href="https://www.linkedin.com/in/theshivam7/">LinkedIn</a> | 
        <a href="https://github.com/theshivam7">GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)

def call_openai(messages):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-instruct",
            messages=messages,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def diagnose_crop():
    st.markdown("<h2 class='feature-header'>Diagnose Your Sick Crop</h2>", unsafe_allow_html=True)
    
    with st.expander("How to use this feature"):
        st.info("Upload a clear image of your crop showing the affected areas. Our AI will analyze the image and provide a diagnosis along with treatment recommendations.")
    
    uploaded_file = st.file_uploader("Upload an image of your crop", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            with st.spinner("Analyzing your crop..."):
                # Simulate a delay for demonstration purposes
                time.sleep(2)
                
                # Resize the image
                max_size = (800, 800)  # You can adjust this size
                image.thumbnail(max_size, Image.LANCZOS)
                
                # Convert image to RGB if it's in RGBA mode
                if image.mode == 'RGBA':
                    image = image.convert('RGB')
                
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='JPEG', quality=85)  # Use JPEG format with slightly reduced quality
                img_byte_arr = img_byte_arr.getvalue()
                img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

                messages = [
                    {"role": "system", "content": "You are an expert in diagnosing crop diseases in India. Provide detailed diagnoses and solutions suitable for Indian agriculture."},
                    {"role": "user", "content": f"Diagnose any issues with this crop and provide detailed solutions suitable for Indian farming conditions. Include common names of diseases in Hindi if applicable. [IMAGE]{img_base64}[/IMAGE]"}
                ]
                response = call_openai(messages)
            st.success("Analysis complete!")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred while processing the image: {str(e)}")

def find_treatment():
    st.markdown("<h2 class='feature-header'>Find the Right Treatment</h2>", unsafe_allow_html=True)
    crop_type = st.selectbox("Select your crop type", ["Wheat", "Rice", "Corn", "Soybean", "Tomato", "Potato", "Cotton", "Barley"])
    issue = st.text_input("Describe the issue with your crop")
    region = st.selectbox("Select your region", ["North India", "South India", "East India", "West India", "Central India", "Northeast India"])
    soil_type = st.selectbox("Select your soil type", ["Alluvial", "Black", "Red", "Laterite", "Desert"])
    irrigation_method = st.selectbox("Select your irrigation method", ["Flood Irrigation", "Drip Irrigation", "Sprinkler Irrigation", "Rainfed"])

    if st.button("Get Treatment Recommendations"):
        messages = [
            {"role": "system", "content": "You are an expert in agricultural treatments suitable for Indian farming conditions. Provide detailed recommendations and prices in Indian Rupees."},
            {"role": "user", "content": f"Provide detailed treatment recommendations for {crop_type} with the following issue: {issue}. The farm is located in {region} with {soil_type} soil and uses {irrigation_method}. Include product names, application methods, and prices in Indian Rupees (₹). Also, suggest any government schemes or subsidies that might be applicable."}
        ]
        response = call_openai(messages)
        st.write(response)

def expert_advice():
    st.markdown("<h2 class='feature-header'>Expert Advice</h2>", unsafe_allow_html=True)
    question_type = st.selectbox("Select a topic", [
        "Pest Management",
        "Soil Health",
        "Water Management",
        "Climate Resilient Agriculture",
        "Organic Farming",
        "Farm Mechanization",
        "Crop Insurance",
        "Government Schemes",
        "Other"
    ])
    
    if question_type == "Other":
        question = st.text_area("What agricultural advice do you need?")
    else:
        question = st.text_area("Provide more details about your question:")

    if st.button("Get Expert Advice"):
        messages = [
            {"role": "system", "content": "You are an expert agricultural advisor specializing in Indian farming practices and conditions. Provide detailed, practical advice with examples relevant to Indian agriculture."},
            {"role": "user", "content": f"Topic: {question_type}\nQuestion: {question}\nProvide expert advice on this topic, including relevant government schemes, best practices, and recent advancements in Indian agriculture."}
        ]
        response = call_openai(messages)
        st.write(response)

def maximize_yields():
    st.markdown("<h2 class='feature-header'>Maximize Your Crop Yields</h2>", unsafe_allow_html=True)
    crop_type = st.selectbox("Select your crop type", ["Wheat", "Rice", "Corn", "Soybean", "Tomato", "Potato", "Cotton", "Barley"])
    soil_type = st.selectbox("Select your soil type", ["Alluvial", "Black", "Red", "Laterite", "Desert"])
    climate = st.selectbox("Select your climate", ["Tropical", "Subtropical", "Arid", "Semi-arid", "Temperate"])
    region = st.selectbox("Select your region", ["North India", "South India", "East India", "West India", "Central India", "Northeast India"])
    farm_size = st.number_input("Enter your farm size (in acres)", min_value=0.1, step=0.1)

    if st.button("Get Yield Optimization Tips"):
        messages = [
            {"role": "system", "content": "You are an expert in crop yield optimization for Indian agriculture. Provide detailed, practical advice tailored to the specific inputs."},
            {"role": "user", "content": f"Provide comprehensive yield optimization tips for {crop_type} grown on a {farm_size}-acre farm in {region}, with {soil_type} soil in a {climate} climate. Include advice on soil preparation, seed selection, irrigation, fertilization, pest management, and harvesting. Suggest any relevant government schemes or subsidies. Include any product recommendations with prices in Indian Rupees (₹) and where to purchase them."}
        ]
        response = call_openai(messages)
        st.write(response)

def best_deals():
    st.markdown("<h2 class='feature-header'>Best Product Deals</h2>", unsafe_allow_html=True)
    product_type = st.selectbox("What are you looking for?", ["Fertilizers", "Seeds", "Herbicides", "Pesticides", "Farm Equipment"])
    region = st.selectbox("Select your region", ["North India", "South India", "East India", "West India", "Central India", "Northeast India"])

    if st.button("Find Best Deals"):
        messages = [
            {"role": "system", "content": "You are an AI assistant providing product deals for agricultural products available in India. All prices should be in Indian Rupees (₹). Present the information in a table format with columns for Product Name, Price, Description, and Where to Buy."},
            {"role": "user", "content": f"Generate 5 best deals for {product_type} available in {region} with product names, prices in Indian Rupees (₹), brief descriptions, and links to genuine online stores or local dealer information. Format the response as a markdown table."}
        ]
        response = call_openai(messages)
        st.write(response)

def sell_produce():
    st.markdown("<h2 class='feature-header'>Sell at Your Price</h2>", unsafe_allow_html=True)
    produce_type = st.selectbox("Select your produce", ["Tomatoes", "Apples", "Lettuce", "Carrots", "Potatoes", "Onions", "Wheat", "Rice", "Cotton"])
    quality = st.slider("Rate the quality of your produce", 1, 5, 3)
    quantity = st.number_input("Enter the quantity (in kg)", min_value=1)
    region = st.selectbox("Select your region", ["North India", "South India", "East India", "West India", "Central India", "Northeast India"])

    if st.button("Find Buyers"):
        messages = [
            {"role": "system", "content": "You are an AI assistant providing buyer information for agricultural produce in India. All prices should be in Indian Rupees (₹). Include information about popular online marketplaces and local mandis."},
            {"role": "user", "content": f"Generate 3 potential buyers in {region} for {quantity}kg of {produce_type} with quality rating {quality}/5. Include buyer names (or marketplace names), offered prices in Indian Rupees (₹), and brief terms. Also, suggest popular online platforms for selling produce in India and provide their website links. Include information about the nearest APMC mandi if applicable."}
        ]
        response = call_openai(messages)
        st.write(response)

if __name__ == "__main__":
    main()