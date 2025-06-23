# ✈️ AI-Powered Travel Planner

An intelligent travel planning web app built using **Streamlit**, **Gemini AI**, **Agno agent** and **SerpAPI**.  
It provides personalized flight, hotel, and activity recommendations based on your preferences.

## 🔥 Features
- ✈️ Search real-time flight data via SerpAPI
- 🏨 Hotel and budget customization
- 🗺️ Themed trip planning (Couple, Family, Solo, Adventure)
- 📅 Interactive date selection and trip duration
- 🎒 Smart packing checklist
- 🛂 Visa, insurance, and currency helper

## 🚀 Tech Stack
- Python
- Streamlit
- SerpAPI
- agno.tools Agent
- Gemini (Google AI)

To set up the **Travel-Planner-AI-Agent** locally, follow these steps:

### Prerequisites
- **Python**: Ensure you have Python 3.7 or later installed on your system.
- **Pip**: Make sure you have pip installed to manage Python packages.

### Steps to Set Up Locally

1. **Clone the Repository**
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone https://github.com/Danish137/Travel-Planner-AI-Agent.git
   ```

2. **Navigate to the Project Directory**
   Change into the project directory:
   ```bash
   cd Travel-Planner-AI-Agent
   ```

3. **Create a Virtual Environment (Optional but Recommended)**
   Create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
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

4. **Install Dependencies**
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up API Keys**
   You need to set up API keys for SerpAPI.
6. **Run the Application**
   Start the Streamlit application with the following command:
   ```bash
   streamlit run app.py
   ```


7. **Access the Application**
   Open your web browser and go to `http://localhost:8501` to access the Travel Planner AI Agent.

### Troubleshooting
- If you encounter errors, check the terminal for messages and ensure all dependencies are correctly installed.
- Make sure your API keys are correctly set up and that you have internet access for the app to fetch data.

  


