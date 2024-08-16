## AgroSmart

AgroSmart is a **free and user-friendly application** designed to help farmers in India. It offers tools to diagnose crop diseases, find effective treatments, receive expert advice, and maximize crop yields. AgroSmart provides tailored recommendations to enhance productivity and profitability for Indian farmers.

Try 🔗 [AgroSmart](https://agrosmarts.streamlit.app/) 
### Features

- **Diagnose Crop Diseases**: Upload a photo of your affected crop to get a detailed diagnosis and treatment suggestions tailored to Indian farming conditions.
- **Find the Right Treatment**: Input details about your crop issue to receive customized treatment recommendations, including product names, application methods, and prices in Indian Rupees.
- **Expert Advice**: Access personalized advice on topics like pest management, soil health, and water management.
- **Maximize Crop Yields**: Get tips and strategies to optimize yields based on your farm's specific conditions, including soil type, climate, and region.
- **Best Product Deals**: Discover the best deals on agricultural products like fertilizers, seeds, herbicides, pesticides, and farm equipment available in your area.
- **Sell at Your Price**: Connect with potential buyers for your produce, including pricing and terms, and explore popular online marketplaces and local mandis for selling your products.

### How to Download and Install on Your Local Server

Follow these simple steps to download and install the AgroSmart app on your local server:

#### Prerequisites

- Python 3.8 or later
- [pip](https://pip.pypa.io/en/stable/) package manager
- A GitHub account to clone the repository

#### Step 1: Clone the Repository

Clone the repository to your local machine using Git. Open your terminal and run:

```bash
git clone https://github.com/yourusername/agrosmart.git
```

#### Step 2: Navigate to the Project Directory

Move into the project directory:

```bash
cd agrosmart
```

#### Step 3: Create a Virtual Environment

Use a virtual environment to manage dependencies. Create one by running:

```bash
python3 -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

#### Step 4: Install the Required Dependencies

Install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

#### Step 5: Set Up Environment Variables

Create a `.env` file in the root directory of the project and add your OpenAI API key:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

#### Step 6: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Contact

Created by [Shivam Sharma](https://www.linkedin.com/in/theshivam7/). Feel free to connect on LinkedIn for more projects and collaborations.