import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from mysql_connection import get_data_from_db, get_post_data_db

# MySQL에서 데이터 가져오기
df = get_data_from_db()

# 텍스트 결합
df['user_profile'] = df.apply(lambda x: ' '.join([
    str(x['careers']), str(x['certifications']), str(x['educations']),
    str(x['interests']), str(x['skills'])
]), axis=1)

# 포스트 데이터 예시 (실제 데이터베이스에서 가져오는 코드로 대체 가능)
post_data = get_post_data_db()

post_df = pd.DataFrame(post_data)

post_df['post_profile'] = post_df.apply(lambda x: ' '.join([
    x['title'], x['category'], x['detail'], x['summary']
]), axis=1)

# TF-IDF 벡터 생성
tfidf_vectorizer = TfidfVectorizer()
user_tfidf = tfidf_vectorizer.fit_transform(df['user_profile'])
post_tfidf = tfidf_vectorizer.fit_transform(post_df['post_profile'])

# 모델 저장
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)
with open('user_tfidf.pkl', 'wb') as f:
    pickle.dump(user_tfidf, f)
with open('post_tfidf.pkl', 'wb') as f:
    pickle.dump(post_tfidf, f)

print("모델 파일이 성공적으로 저장되었습니다.")
