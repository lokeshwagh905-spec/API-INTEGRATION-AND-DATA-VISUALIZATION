# ============================================================
# MACHINE LEARNING MODEL IMPLEMENTATION
# PROJECT : SPAM EMAIL DETECTION USING SCIKIT-LEARN
# ============================================================

# =========================
# 1. IMPORT LIBRARIES
# =========================
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# =========================
# 2. CREATE SAMPLE DATASET
# =========================
# If you already have a dataset file,
# you can replace this section with:
# data = pd.read_csv("spam.csv")

data_dict = {
    "label": [
        "ham","spam","ham","spam","ham",
        "spam","ham","ham","spam","ham",
        "spam","ham","spam","ham","spam",
        "ham","spam","ham","spam","ham"
    ],

    "message": [
        "Hey, how are you doing today?",
        "Congratulations! You won a free lottery ticket",
        "Let's meet tomorrow for lunch",
        "Claim your free cash reward now",
        "Can you send me the assignment?",
        "Win money instantly by clicking here",
        "Good morning have a nice day",
        "Are we still meeting tonight?",
        "Exclusive offer just for you",
        "Please call me when you arrive",
        "Get free recharge by registering",
        "Happy Birthday! Have a great year",
        "Urgent! Your account has been selected",
        "See you in the class tomorrow",
        "Limited time offer claim now",
        "Don't forget to bring the documents",
        "You have won a brand new car",
        "Let's play cricket this evening",
        "Free vacation tickets available now",
        "Can you help me with coding?"
    ]
}

data = pd.DataFrame(data_dict)

# =========================
# 3. DISPLAY DATASET
# =========================
print("\n===== DATASET =====\n")
print(data.head())

# =========================
# 4. DATA PREPROCESSING
# =========================

# Convert labels into numbers
# ham = 0
# spam = 1
data['label_num'] = data['label'].map({
    'ham': 0,
    'spam': 1
})

# Features and target
X = data['message']
y = data['label_num']

# Convert text into numerical vectors
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(X)

# =========================
# 5. SPLIT DATASET
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# 6. TRAIN MODEL
# =========================
model = MultinomialNB()

model.fit(X_train, y_train)

# =========================
# 7. MAKE PREDICTIONS
# =========================
y_pred = model.predict(X_test)

# =========================
# 8. MODEL EVALUATION
# =========================
print("\n===== MODEL EVALUATION =====\n")

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy :", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# =========================
# 9. TEST WITH CUSTOM INPUT
# =========================
print("\n===== CUSTOM MESSAGE TEST =====\n")

sample_messages = [
    "Congratulations you won free tickets",
    "Hey bro are you coming to college today?"
]

sample_data = vectorizer.transform(sample_messages)

predictions = model.predict(sample_data)

for message, prediction in zip(sample_messages, predictions):

    print("Message :", message)

    if prediction == 1:
        print("Prediction : SPAM")
    else:
        print("Prediction : HAM")

    print("--------------------------------")

# =========================
# 10. SAVE MODEL (OPTIONAL)
# =========================
import pickle

pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nModel and Vectorizer saved successfully!")

# ============================================================
# END OF PROJECT
# ============================================================