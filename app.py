import streamlit as st
import io
from PIL import Image
import base64
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI API client with the custom base URL
client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

def main():
    st.title("AgroSmart: Your Free Crop Diagnosis and Treatment App")
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Welcome to AgroSmart India</h1>", unsafe_allow_html=True)

    st.sidebar.title("Features")
    st.sidebar.header("Explore Our Features")
    feature = st.sidebar.radio(
        "Choose a feature:",
        ("Diagnose Your Sick Crop", "Find the Right Treatment", "Expert Advice",
         "Maximize Your Crop Yields", "Best Product Deals", "Sell at Your Price")
    )
    
    if feature == "Diagnose Your Sick Crop":
        diagnose_crop()
    elif feature == "Find the Right Treatment":
        find_treatment()
    elif feature == "Expert Advice":
        expert_advice()
    elif feature == "Maximize Your Crop Yields":
        maximize_yields()
    elif feature == "Best Product Deals":
        best_deals()
    elif feature == "Sell at Your Price":
        sell_produce()

    # Footer with links
    st.markdown("""
    <style>
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    .footer-left {
        text-align: left;
        flex: 1;
    }
    .footer-center {
        text-align: center;
        flex: 1;
    }
    .footer-right {
        text-align: right;
        flex: 1;
    }
    .footer-disclaimer {
        text-align: center;
        font-size: 10px;
        margin-top: 5px;
        color: lightgrey;
    }
    </style>
    <footer>
        <div class="footer-container">
            <div class="footer-left">
                &copy; 2024 AgroSmart India
            </div>
            <div class="footer-center">
                Made with ❤️ by <a href="https://www.linkedin.com/in/theshivam7/" style="color: white; text-decoration: none;">Shivam 🍁</a>
            </div>
            <div class="footer-right">
                <a href="https://www.linkedin.com/in/theshivam7/" style="color: white; text-decoration: none; margin-right: 15px;">LinkedIn</a>
                <a href="https://github.com/theshivam7" style="color: white; text-decoration: none; margin-right: 15px;">GitHub</a>
            </div>
        </div>
        <div class="footer-disclaimer">
            AgroSmart can make mistakes. Check important info.
        </div>
    </footer>
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
    st.header("Diagnose Your Sick Crop")
    uploaded_file = st.file_uploader("Upload an image of your crop", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.write("Analyzing...")
            
            # Resize the image
            max_size = (800, 800)  # You can adjust this size
            image.thumbnail(max_size, Image.LANCZOS)
            
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG', quality=85)  # Use JPEG format with slightly reduced quality
            img_byte_arr = img_byte_arr.getvalue()
            img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

            messages = [
                {"role": "system", "content": "You are an expert in diagnosing crop diseases in India. Provide detailed diagnoses and solutions suitable for Indian agriculture."},
                {"role": "user", "content": f"Diagnose any issues with this crop and provide detailed solutions suitable for Indian farming conditions. Include common names of diseases in Hindi if applicable. [IMAGE]{img_base64}[/IMAGE]"}
            ]
            response = call_openai(messages)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred while processing the image: {str(e)}")

def find_treatment():
    st.header("Find the Right Treatment")
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
    st.header("Expert Advice")
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
    st.header("Maximize Your Crop Yields")
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
    st.header("Best Product Deals")
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
    st.header("Sell at Your Price")
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