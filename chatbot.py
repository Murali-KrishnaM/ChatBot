import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("intents.json", "r") as f:
    data = json.load(f)

patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X)
    index = similarities.argmax()

    if similarities[0][index] < 0.2:
        return "Sorry, I didn't understand that."

    tag = tags[index]
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
