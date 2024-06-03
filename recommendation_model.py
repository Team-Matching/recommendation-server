import pickle
from sklearn.metrics.pairwise import cosine_similarity

# 모델 로드
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)
with open('user_tfidf.pkl', 'rb') as f:
    user_tfidf = pickle.load(f)
with open('post_tfidf.pkl', 'rb') as f:
    post_tfidf = pickle.load(f)

def recommend(user_profile):
    user_tfidf_new = tfidf_vectorizer.transform([user_profile])
    similarity = cosine_similarity(user_tfidf_new, post_tfidf)
    return similarity
