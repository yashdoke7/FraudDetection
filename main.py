from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from services.location_services import get_location
from fraud_test import predict_transaction


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})

@app.get("/alert", response_class=HTMLResponse)
def get_alert(request: Request):
    return templates.TemplateResponse("alert.html", {"request": request})

@app.get("/map", response_class=HTMLResponse)
def serve_map_ui(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})


@app.post("/get-location")
def get_location_api():
    coords = get_location()
    return {"locations": [{"lat": loc[0], "long": loc[1]} for loc in coords]}



class TransactionInput(BaseModel):
    amt: float
    mode: str

@app.post("/predict")
def predict_fraud(data: TransactionInput):
    if data.mode == "fraud":
        merchant = "fraud_Morissette PLC"
        job = "Soil scientist"
        category = "shopping_pos"
    else:
        merchant = "fraud_Rutherford-Mertz"
        job = "IT trainer"
        category = "grocery_pos"

    prediction = predict_transaction(merchant, category, job, data.amt)
    return {"prediction": prediction}