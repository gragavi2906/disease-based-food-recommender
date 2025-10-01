# Disease-Based Food Recommender

## Project Description
The **Disease-Based Food Recommender** is a Python application that suggests suitable foods based on specific diseases and nutritional requirements. It helps users make informed dietary choices for better health management.

---

## Features
- Suggests foods based on the disease input
- Provides nutritional information for recommended foods
- Easy-to-use command-line interface
- Works with CSV-based datasets for diseases and foods

---
## Folder Structure

disease-based-food-recommender/
│
├── data/ # All dataset CSV files
│ ├── disease_data.csv
│ └── food_data.csv
│
├── src/ # Python source code
│ ├── main.py
│ ├── preprocessing.py
│ └── recommender.py
│
├── .gitignore # Files/folders to ignore in Git
├── LICENSE # License file
├── README.md # Project documentation
└── requirements.txt # Required Python libraries

Usage

Run the main script to start the recommender:

python src/main.py


Follow the prompts to enter a disease and get food recommendations.

Requirements

Python 3.8+
pandas
numpy
scikit-learn 
tkinter
DecisionTreeClassifier





