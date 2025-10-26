
import streamlit as st
from prediction_helper import predict
import pandas as pd

# Configure page
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the page layout
st.title('🏥 Health Insurance Cost Predictor')
st.markdown("---")
st.markdown("### Enter your details to get an estimated health insurance premium")

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Add some spacing
st.markdown("---")

# Create two columns for the button and results
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Button to make prediction
    if st.button('🔮 Predict Insurance Cost', type="primary", use_container_width=True):
        try:
            # Validate inputs
            if age < 18:
                st.error("Age must be at least 18 years")
            elif income_lakhs < 0:
                st.error("Income cannot be negative")
            else:
                with st.spinner('Calculating your insurance premium...'):
                    prediction = predict(input_dict)
                    
                # Display result with formatting
                st.success("✅ Prediction Complete!")
                st.markdown(f"""
                <div style="
                    background: linear-gradient(90deg, #4CAF50, #45a049);
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    margin: 20px 0;
                ">
                    <h2 style="color: white; margin: 0;">
                        Estimated Premium: ₹{prediction:,}
                    </h2>
                </div>
                """, unsafe_allow_html=True)
                
                # Show input summary
                with st.expander("📋 Input Summary"):
                    df_summary = pd.DataFrame(list(input_dict.items()), columns=['Parameter', 'Value'])
                    st.dataframe(df_summary, use_container_width=True)
                    
        except Exception as e:
            st.error(f"❌ Error making prediction: {str(e)}")
            st.info("Please check your inputs and try again.")

# Add sidebar with information
with st.sidebar:
    st.markdown("## ℹ️ About")
    st.info("""
    This app predicts health insurance premiums based on:
    - Personal demographics
    - Health indicators
    - Insurance plan details
    - Risk factors
    """)
    
    st.markdown("## 📊 Model Info")
    st.write("""
    - **Young Adults (≤25)**: Linear Regression
    - **Adults (>25)**: XGBoost Regressor
    - **Features**: 17 engineered features
    - **Accuracy**: Optimized for different age groups
    """)
