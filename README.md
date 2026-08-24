# 🛡️ Malicious AD Network Detection

## 🔍 Overview

**Malicious AD Network Detection** is a Machine Learning-based web application designed to identify whether a given URL is **safe or malicious**.

Malicious URLs can be used for phishing, malware distribution, fake advertisements, and other cyber threats. This project analyzes different characteristics of a URL and uses a trained **Random Forest Classifier** to predict its security status.

The prediction is integrated into a **Flask web application**, where users can enter a URL and receive a classification along with a risk score.

---

## 🎯 Objectives

* Detect potentially malicious URLs.
* Analyze URL characteristics using feature extraction.
* Apply Machine Learning for URL classification.
* Provide a simple web interface for users.
* Display the prediction and risk score.
* Demonstrate the practical application of Machine Learning in cybersecurity.

---

## 🚨 Problem Statement

Internet users may encounter malicious URLs through advertisements, emails, messages, and suspicious websites.

Manually identifying whether a URL is trustworthy can be difficult for normal users. Therefore, this project aims to provide an automated approach that analyzes URL-based characteristics and predicts whether the URL is **Safe** or **Malicious**.

---

## 💡 Proposed Solution

The system takes a URL from the user and performs the following operations:

1. Accepts the URL through the web interface.
2. Extracts important URL-based features.
3. Passes the extracted features to the trained Machine Learning model.
4. Uses a Random Forest Classifier to predict the URL category.
5. Calculates a risk score using the model's prediction probability.
6. Displays the result to the user.

---

## 🧠 Machine Learning Approach

The project uses a **Random Forest Classifier** for binary classification.

### Classification


0 → Safe URL
1 → Malicious URL


The model is trained using URL-related features extracted from the dataset.

The training process includes:

* Dataset loading
* Feature extraction
* Training/testing split
* Random Forest model training
* Prediction
* Accuracy evaluation
* Model serialization using Joblib

The model is saved as model.pkl and later loaded by the Flask application.

---

## 🔎 URL Features

The application extracts the following features from each URL:

| Feature            | Description                             |
| ------------------ | --------------------------------------- |
| URL Length         | Total number of characters in the URL   |
| Hostname Length    | Length of the hostname                  |
| Number of Dots     | Number of `.` characters                |
| Number of Hyphens  | Number of `-` characters                |
| Number of Digits   | Number of numeric characters            |
| HTTPS              | Checks whether HTTPS is used            |
| IP Address         | Checks whether an IP address is present |
| Special Characters | Counts selected special characters      |

These features are extracted using Python's urlparse and regular expressions.

---
## 🔄 Project Workflow


                    ┌─────────────────────┐
                    │     User Input      │
                    │        URL          │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │  Feature Extraction │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │  Random Forest      │
                    │     Classifier      │
                    └──────────┬──────────┘
                               ↓
                   ┌───────────┴───────────┐
                   ↓                       ↓
            ┌─────────────┐         ┌──────────────┐
            │   Safe URL  │         │ Malicious URL│
            └──────┬──────┘         └──────┬───────┘
                   ↓                       ↓
                   └───────────┬───────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Prediction + Risk   │
                    │       Score         │
                    └─────────────────────┘
---

## ⚙️ Technologies Used

### Programming Language

* Python

### Backend

* Flask

### Machine Learning

* Scikit-learn
* Random Forest Classifier

### Data Processing

* Pandas
* NumPy

### Model Management

* Joblib

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

---

## 🔄 How the System Works

### 1. Dataset Generation

The project generates a dataset containing safe and malicious URL examples with corresponding labels.


Safe URL       → 0
Malicious URL  → 1


The generated dataset is stored in dataset.csv.

### 2. Feature Extraction

The URL is processed using the extract_features() function.

The system extracts characteristics such as:

* URL length
* Hostname length
* Number of dots
* Number of hyphens
* Number of digits
* HTTPS usage
* IP address presence
* Special characters

### 3. Model Training

The extracted features are divided into training and testing data.

A Random Forest Classifier is trained using the training dataset.

Model:
 Dataset
   ↓
Feature Extraction
   ↓
Train/Test Split
   ↓
Random Forest
   ↓
Model Evaluation
   ↓
model.pkl


### 4. Prediction

When a user submits a URL, Flask extracts its features and sends them to the trained model.

The application then generates:

text
Prediction
+
Risk Score


## 📊 Output

The application provides:

* URL classification
* Safe/Malicious prediction
* Risk score
* User-friendly web interface
* Real-time prediction through Flask

---

## 📚 Learning Outcomes

Through this project, I gained practical knowledge in:

* Python programming
* Machine Learning classification
* Feature engineering
* Random Forest
* Flask web development
* Frontend development
* Model integration
* Dataset preparation
* Debugging and troubleshooting
* Cybersecurity fundamentals

---

## 🔮 Future Enhancements

Future versions of this project can be improved by:

* Using larger real-world URL datasets.
* Adding more URL and domain-based features.
* Comparing multiple Machine Learning algorithms.
* Improving model evaluation using additional metrics.
* Adding a database for storing scan history.
* Implementing authentication.
* Improving the deployment architecture.
* Adding more advanced cybersecurity detection techniques.

---

## 👩‍💻 Project Role

**Role:**  Team Member

My contribution included:

* Dataset preparation
* URL feature extraction
* Machine Learning model implementation
* Flask backend development
* Frontend integration
* Testing and debugging
* Model integration with the web application

---

## 📌 Disclaimer

This project is developed for **educational and demonstration purposes**. The prediction should not be considered a definitive security assessment of a URL.

---

## ⭐ Conclusion

**Malicious AD Network Detection** demonstrates how Machine Learning can be integrated with a web application to analyze URL characteristics and identify potentially malicious URLs.

The project provided practical exposure to the integration of **Machine Learning, Python, Flask, frontend technologies, and cybersecurity concepts** in a single application.

---
