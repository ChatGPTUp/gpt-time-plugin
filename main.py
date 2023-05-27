from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import pytz

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")

@app.get("/time")
def read_time():
    kst = pytz.timezone('Asia/Seoul')
    time_in_kst = datetime.now(kst)
    return {"time": time_in_kst.strftime('%Y-%m-%d %H:%M:%S')}
