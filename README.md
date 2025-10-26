# 🏥 Healthcare Premium Prediction

A machine learning-powered web application that predicts health insurance premiums based on personal demographics, health indicators, and insurance plan details.

## 🌐 Live Demo

**Try the app now**: [https://predxhealth.streamlit.app/](https://predxhealth.streamlit.app/)

The application is deployed and ready to use! Simply enter your details to get an instant premium prediction.

## 🌟 Features

- **Age-Segmented Models**: Different models for young adults (≤25) and adults (>25)
- **Interactive Web Interface**: Built with Streamlit for easy use
- **Real-time Predictions**: Instant premium calculations
- **Comprehensive Input Validation**: Ensures data quality
- **Risk Assessment**: Normalized medical history risk scoring

## 🏗️ Project Structure

```
Healthcare-Premium-Prediction/
├── app/
│   ├── main.py                 # Streamlit web application
│   └── prediction_helper.py    # ML prediction logic
├── artifacts/
│   ├── model_young.joblib      # Linear Regression for ≤25 age
│   ├── model_rest.joblib       # XGBoost for >25 age
│   ├── scaler_young.joblib     # Scaler for young adults
│   └── scaler_rest.joblib      # Scaler for adults
├── notebooks/                  # Jupyter notebooks for model development
├── data/                       # Training data files
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Healthcare-Premium-Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas joblib scikit-learn xgboost
   ```

3. **Run the application**
   ```bash
   streamlit run app/main.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📊 Model Details

### Architecture
- **Young Adults (Age ≤ 25)**: Linear Regression
- **Adults (Age > 25)**: XGBoost Regressor
- **Feature Engineering**: 17 engineered features including categorical encoding and risk scoring

### Input Features
- **Demographics**: Age, Gender, Marital Status, Region
- **Financial**: Income (in Lakhs), Number of Dependants
- **Health**: BMI Category, Medical History, Genetical Risk
- **Lifestyle**: Smoking Status, Employment Status
- **Insurance**: Insurance Plan (Bronze/Silver/Gold)

### Risk Scoring System
Medical conditions are scored and normalized:
- Heart Disease: 8 points
- Diabetes: 6 points
- High Blood Pressure: 6 points
- Thyroid: 5 points
- No Disease: 0 points

## 🎯 Usage

1. **Fill in your details** in the web interface
2. **Select appropriate options** from dropdown menus
3. **Click "Predict Insurance Cost"** to get your estimate
4. **View the results** with formatted premium amount
5. **Check input summary** in the expandable section

## 🔧 Technical Implementation

### Data Preprocessing
- Categorical variables encoded using one-hot encoding
- Numerical features scaled using StandardScaler
- Medical history converted to normalized risk scores

### Model Training
- Age-based segmentation for better accuracy
- Separate scalers for different age groups
- Feature selection based on correlation analysis

### Prediction Pipeline
1. Input validation and preprocessing
2. Feature engineering and encoding
3. Scaling based on age group
4. Model selection (young vs. adult)
5. Prediction and post-processing

## 📈 Performance

The models are optimized for different age groups:
- **Young Adults**: Linear model captures simpler relationships
- **Adults**: XGBoost handles complex feature interactions
- **Validation**: Cross-validation used for model selection

## 🛠️ Development

### Adding New Features
1. Update `categorical_options` in `main.py`
2. Modify `preprocess_input()` in `prediction_helper.py`
3. Retrain models with new features
4. Update documentation

### Model Retraining
1. Prepare new training data
2. Run notebooks in `notebooks/` directory
3. Save new models to `artifacts/` directory
4. Test with sample predictions

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For questions or issues, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ using Python, Streamlit, and Machine Learning**
