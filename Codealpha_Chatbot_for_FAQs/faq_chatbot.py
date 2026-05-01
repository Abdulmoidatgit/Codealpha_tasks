import os
import pandas as pd
import nltk
import string
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')  
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

# -------------------------
# LOAD CSV SAFELY
# -------------------------
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "faqs.csv")

try:
    faq_data = pd.read_csv(file_path)
except Exception as e:
    print("❌ Error loading faqs.csv:", e)
    exit()

# Check columns
if "Question" not in faq_data.columns or "Answer" not in faq_data.columns:
    print("❌ CSV must have 'Question' and 'Answer' columns")
    exit()

questions = faq_data["Question"].tolist()
answers = faq_data["Answer"].tolist()

# -------------------------
# PREPROCESSING
# -------------------------
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)

    return " ".join([w for w in words if w not in stopwords.words('english')])

processed_questions = [preprocess_text(q) for q in questions]

# -------------------------
# VECTORIZE
# -------------------------
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

# -------------------------
# CHATBOT
# -------------------------
def chatbot_response(user_input):
    processed_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([processed_input])

    similarity = cosine_similarity(input_vector, question_vectors)

    index = similarity.argmax()
    score = similarity[0][index]

    if score > 0.2:
        return answers[index]
    else:
        return "Sorry, I could not understand your question."

# -------------------------
# CHAT LOOP
# -------------------------
print("\nFAQ CHATBOT READY 🤖 (type 'exit' to stop)\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    print("Bot:", chatbot_response(user))