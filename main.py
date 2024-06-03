from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
from recommendation_model import recommend  # 추천 함수 가져오기

app = FastAPI()

class UserProfile(BaseModel):
    user_profile: str

@app.post("/recommend-post")
def get_recommendations(user_profile: UserProfile):
    try:
        similarity = recommend(user_profile.user_profile)
        return {"similarity": similarity.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# FastAPI 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
