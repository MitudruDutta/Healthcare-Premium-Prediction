#!/usr/bin/env python3
"""
Test script for Healthcare Premium Prediction App
Run this to verify everything is working correctly.
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported."""
    print("🧪 Testing imports...")
    try:
        import pandas as pd
        import joblib
        import streamlit as st
        print("✅ All dependencies imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_models():
    """Test if models can be loaded and predictions work."""
    print("🧪 Testing model loading and predictions...")
    
    # Add app directory to path
    sys.path.insert(0, 'app')
    
    try:
        from prediction_helper import predict
        print("✅ Models loaded successfully")
        
        # Test cases
        test_cases = [
            {
                'name': 'Young Adult (Linear Regression)',
                'data': {
                    'Age': 22,
                    'Number of Dependants': 0,
                    'Income in Lakhs': 3,
                    'Genetical Risk': 1,
                    'Insurance Plan': 'Bronze',
                    'Employment Status': 'Salaried',
                    'Gender': 'Female',
                    'Marital Status': 'Unmarried',
                    'BMI Category': 'Normal',
                    'Smoking Status': 'No Smoking',
                    'Region': 'Southeast',
                    'Medical History': 'No Disease'
                }
            },
            {
                'name': 'Adult (XGBoost)',
                'data': {
                    'Age': 35,
                    'Number of Dependants': 2,
                    'Income in Lakhs': 8,
                    'Genetical Risk': 3,
                    'Insurance Plan': 'Silver',
                    'Employment Status': 'Self-Employed',
                    'Gender': 'Male',
                    'Marital Status': 'Married',
                    'BMI Category': 'Overweight',
                    'Smoking Status': 'Occasional',
                    'Region': 'Northwest',
                    'Medical History': 'High blood pressure'
                }
            }
        ]
        
        for test_case in test_cases:
            try:
                result = predict(test_case['data'])
                print(f"✅ {test_case['name']}: ₹{result:,}")
            except Exception as e:
                print(f"❌ {test_case['name']}: Error - {e}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🏥 Healthcare Premium Prediction - System Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import test failed. Please install requirements:")
        print("pip install -r requirements.txt")
        return False
    
    print()
    
    # Test models
    if not test_models():
        print("\n❌ Model test failed. Check if artifacts directory exists.")
        return False
    
    print("\n🎉 All tests passed! Your app is ready to run.")
    print("\n🚀 To start the app, run:")
    print("streamlit run app/main.py")
    print("\nOr use the automated script:")
    print("./run.sh")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)