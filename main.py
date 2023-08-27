import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.background import BackgroundTasks
import uvicorn

from typing import Annotated

from fastapi import FastAPI, File, UploadFile

import CaptchaCracker as cc

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def remove_file(path: str) -> None:
    os.unlink(path)

#Target image data size
img_width = 100
img_height = 24
# Target image label length
max_length = 5
# Target image label component
characters = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

# Model weight file path
weights_path = "./model/weights.h5"

AM = None

@app.on_event("startup")
def startup():
    try:
        global AM
        if AM is None:
            AM = cc.ApplyModel(weights_path, img_width, img_height, max_length, characters)
    except Exception as e:
        print("Couldn't load the model properly! Closing...")
        exit(-1)

@app.get("/")
def root():
    return {"message": "Hi!"}

@app.post("/solve/")
def solve_captcha(file: Annotated[bytes, File()], background_tasks: BackgroundTasks):
    full_filename = 'image.png'
    with open(full_filename, 'wb') as image:
        image.write(file)
        image.close()
    
    pred = AM.predict(full_filename)

    background_tasks.add_task(remove_file, full_filename)

    return {"result": pred}

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8008, log_level="info", reload=True)
