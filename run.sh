#!/bin/bash

# Health Insurance Premium Prediction App Runner
echo "🏥 Starting Health Insurance Premium Prediction App..."

# Run system test first
echo "🧪 Running system tests..."
python test_app.py

if [ $? -ne 0 ]; then
    echo "❌ System tests failed. Please check the setup."
    exit 1
fi

echo ""
echo "📦 Installing dependencies..."

# Install requirements
pip install -r requirements.txt

echo ""
echo "🚀 Launching Streamlit app..."
echo "📱 Open your browser and go to: http://localhost:8501"
echo "📱 Press Ctrl+C to stop the app"

# Run the app
streamlit run app/main.py