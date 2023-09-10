from fastapi import FastAPI

app = FastAPI()

@app.get("/predict/")
def get_video_id(user_id: str, num_videos: int):
    # Здесь можно добавить логику для получения предзаготовленного значения "video_id"
    video_ids = "call func"

    return {"predictions": video_ids}

