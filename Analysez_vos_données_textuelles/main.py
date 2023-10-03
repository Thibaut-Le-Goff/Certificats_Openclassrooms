from entrees import *

"""
import os
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
"""

from transformers import pipeline
from datasets import load_dataset
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

hugging_face_model = "cardiffnlp/twitter-roberta-base-sentiment-latest"

hugging_face_model = pipeline("sentiment-analysis", model=hugging_face_model)

print(hugging_face_model("I don't like you."))

# Exploration des données :