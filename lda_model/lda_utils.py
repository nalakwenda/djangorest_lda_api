import os
from pathlib import Path

import nltk
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# 💅 Define where the downloads go — make it fashion
nltk_data_dir = Path("nltk_data")
nltk.download("punkt", download_dir=str(nltk_data_dir))
nltk.download("punkt_tab", download_dir=str(nltk_data_dir))  # You needed that VIP!
nltk.download("wordnet", download_dir=str(nltk_data_dir))
nltk.download("stopwords", download_dir=str(nltk_data_dir))

# 🎀 Tell NLTK where to find its fabulous resources
nltk.data.path.append(str(nltk_data_dir))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, 'lda_model_data')

lda_model = LdaModel.load(os.path.join(MODEL_DIR, 'lda_model.gensim'))
dictionary = Dictionary.load(os.path.join(MODEL_DIR, 'dictionary.dict'))

stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return tokens

def get_topic_distribution(text):
    tokens = preprocess(text)
    bow = dictionary.doc2bow(tokens)
    return lda_model.get_document_topics(bow)