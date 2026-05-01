# 🤖 FAQ Chatbot using NLP (TF-IDF + Cosine Similarity)

This project is part of my **AI Python Internship at CodeAlpha**.
It is a simple but effective **FAQ Chatbot** built using Natural Language Processing (NLP) techniques to match user questions with the most relevant answers from a dataset.

---

## 🚀 Project Overview

The chatbot works by:

* Preprocessing user input (lowercasing, removing punctuation, stopwords)
* Converting text into numerical form using **TF-IDF Vectorization**
* Comparing similarity using **Cosine Similarity**
* Returning the most relevant answer from a CSV-based FAQ dataset

If no good match is found, it responds with a fallback message.

---

## 🧠 Technologies Used

* Python 🐍
* Pandas
* NLTK (Natural Language Toolkit)
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## 📁 Project Structure

```
FAQ-Chatbot/
│
├── faq_chatbot.py        # Main chatbot script
├── faqs.csv              # Dataset containing Questions & Answers
└── README.md             # Project documentation
```

---

## 📊 How It Works

1. Load FAQ dataset (`faqs.csv`)
2. Preprocess all questions using NLP techniques
3. Convert text into TF-IDF vectors
4. Take user input and preprocess it the same way
5. Compute similarity between input and dataset questions
6. Return the best matching answer

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/faq-chatbot.git
cd faq-chatbot
```

### 2. Install dependencies

```bash
pip install pandas nltk scikit-learn
```

### 3. Run the chatbot

```bash
python faq_chatbot.py
```

---

## 📌 Example Usage

```
FAQ CHATBOT READY 🤖 (type 'exit' to stop)

You: What is AI?
Bot: Artificial Intelligence is the simulation of human intelligence in machines.

You: How does this work?
Bot: It matches your question using NLP techniques.

You: exit
Bot: Goodbye!
```

---

## ⚠️ Notes

* Make sure `faqs.csv` contains two columns:

  * `Question`
  * `Answer`
* NLTK datasets (`punkt`, `stopwords`) will be downloaded automatically on first run.

---

## 🎯 Internship Context

This project was developed as part of my **CodeAlpha AI Python Internship**, focusing on:

* Natural Language Processing basics
* Real-world chatbot development
* Text similarity and vector space models

---

## 📈 Future Improvements

* Add deep learning-based intent recognition
* Improve accuracy with embeddings (Word2Vec / BERT)
* Build web interface using Flask or Streamlit
* Add voice input/output support

---

## 👨‍💻 Author

**Abdul Moeed**
AI Python Intern @ CodeAlpha

