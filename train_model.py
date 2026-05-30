import dataset_generator
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from utils import extract_features

# Load dataset
data = pd.read_csv("dataset.csv")

# Extract features dynamically
X = data['url'].apply(extract_features)
X = pd.DataFrame(X.tolist())

y = data['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, pred))

# Save model
joblib.dump(model, "model.pkl")
print("Model saved successfully!")