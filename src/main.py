import tkinter as tk
from tkinter import ttk
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd

# Load your sample dataset
sample_data = pd.read_csv("Sample.csv")



# Fill missing values in the dataset (you can use more advanced imputation methods if needed)
sample_data.fillna(0, inplace=True)  # Replace missing values with zeros; modify as needed



# Create a DataFrame with one-hot encoded disease columns
disease_df = pd.DataFrame(disease_encoded, columns= disease_encoded_columns)

# Concatenate the one-hot encoded disease columns with the original dataset
sample_data_encoded = pd.concat([sample_data, disease_df], axis=1)

# Define features (X) and target (y) for the Decision Tree Classifier
X = sample_data_encoded[['AGE', 'GENDER'] + disease_encoded_columns]
y = sample_data_encoded['VITAMIN DEFECIENCY']

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the model
clf.fit(X, y)

# Load the Final.csv dataset with ISO-8859-1 encoding
final_data = pd.read_csv("Final.csv", encoding='ISO-8859-1')

# Function to open the second module in a new window
def open_second_module():
    # Close the main window
    root.destroy()

    # Create a new window for the second module
    second_window = tk.Tk()
    second_window.title("Richfoods Suggestions")
    second_window.geometry("500x600")

    # Apply the same background color as the first window
    second_window.configure(bg="lightblue")

    # Create labels and entry for the second module
    vitamin_label = ttk.Label(second_window, text="Enter vitamin deficiencies (comma-separated):", style="Hospital.TLabel")
    vitamin_label.pack(pady=10)

    vitamin_entry = ttk.Entry(second_window)
    vitamin_entry.pack()

    # Function to suggest rich foods based on vitamin deficiencies
    def suggest_rich_foods():
        user_vitamins = vitamin_entry.get().split(',')
        user_vitamins = [vitamin.strip() for vitamin in user_vitamins]

        # Filter the dataset based on user's vitamin deficiencies
        filtered_data = final_data[final_data['Vitamins'].isin(user_vitamins)]

        rich_foods = []

        # Suggest rich foods based on the filtered dataset
        for index, row in filtered_data.iterrows():
            rich_food = row['Richfoods']
            if rich_food not in rich_foods:
                rich_foods.append(rich_food)

        # Limit the number of rich food suggestions to 7
        rich_foods = rich_foods[:7]

        # Display the rich food suggestions
        rich_foods_label.config(text="Suggested Rich Foods:")
        for i, rich_food in enumerate(rich_foods, start=1):
            rich_foods_label.config(text=f"{rich_foods_label.cget('text')}\n{i}. {rich_food}")

    # Create a "Suggest Rich Foods" button
    suggest_button = ttk.Button(second_window, text="Suggest Rich Foods", style="Hospital.TButton", command=suggest_rich_foods)
    suggest_button.pack(pady=10)

    # Create a label for displaying the rich food suggestions
    rich_foods_label = ttk.Label(second_window, text="", style="Hospital.TLabel")
    rich_foods_label.pack()

    second_window.mainloop()

# Function to predict vitamin deficiency based on user input
def predict_vitamin_deficiency():
    user_age = float(age_entry.get())
    user_gender = gender_entry.get()
    user_gender_encoded = gender_encoding.get(user_gender, -1)

    if user_gender_encoded == -1:
        result_label.config(text="Invalid gender input. Please enter 'Male' or 'Female'.", foreground="red")
        return

    user_disease = disease_entry.get()

    try:
        # Attempt to perform one-hot encoding for the user's input disease
        user_disease_encoded = disease_encoder.transform([[user_disease]])[0]
    except ValueError:
        result_label.config(text=f"Unknown disease category: {user_disease}", foreground="red")
        return

    user_input = [user_age, user_gender_encoded] + list(user_disease_encoded)

    predicted_vitamin_deficiencies = clf.predict([user_input])
    predicted_vitamin_deficiencies = label_encoder.inverse_transform(predicted_vitamin_deficiencies)

    result_label.config(text=f"Predicted Vitamin Deficiencies: {', '.join(predicted_vitamin_deficiencies)}", foreground="green")

# Create the main window
root = tk.Tk()
root.title("Vitamin Deficiency Predictor")
root.geometry("500x500")

# Hospital-style appearance
style = ttk.Style()
style.configure("Hospital.TLabel", font=("Arial", 12), foreground="blue")
style.configure("Hospital.TButton", font=("Arial", 12), foreground="red")

# Set background color
root.configure(bg="lightblue")

# Create labels and entry for the first module
age_label = ttk.Label(root, text="Enter your age:", style="Hospital.TLabel")
age_label.pack(pady=10)

age_entry = ttk.Entry(root)
age_entry.pack()

gender_label = ttk.Label(root, text="Enter your gender (Male/Female):", style="Hospital.TLabel")
gender_label.pack(pady=10)

gender_entry = ttk.Entry(root)
gender_entry.pack()

disease_label = ttk.Label(root, text="Enter one disease:", style="Hospital.TLabel")
disease_label.pack(pady=10)

disease_entry = ttk.Entry(root)
disease_entry.pack()

# Create a "Predict" button for the first module
predict_button = ttk.Button(root, text="Predict", style="Hospital.TButton", command=predict_vitamin_deficiency)
predict_button.pack(pady=10)

# Create a label for displaying the prediction result
result_label = ttk.Label(root, text="", style="Hospital.TLabel")
result_label.pack()

# Create a "Continue" button for opening the second module
continue_button = ttk.Button(root, text="Continue", style="Hospital.TButton", command=open_second_module)
continue_button.pack(pady=10)

root.mainloop()