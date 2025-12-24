import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# === Sample Training Data ===
texts = [
    "The room was clean and spacious",
    "Amazing food and great service",
    "The hotel staff was rude",
    "Very bad experience, room was dirty",
    "Excellent ambience, loved the stay",
    "Terrible location and noisy environment"
]

labels = [
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Positive",
    "Negative"
]

# === Vectorization ===
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# === Train Model ===
model = LogisticRegression()
model.fit(X, labels)

# === Save Vectorizer ===
with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# === Save Model ===
with open("model/absa_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model and vectorizer saved successfully!")
