from ast import For
from fastapi import FastAPI, Request, Form
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# 1. Definir la ruta base (donde está este archivo app.py)
BASE_DIR = Path(__file__).resolve().parent

# 2. Definir rutas a las carpetas hermanas
# Usamos .parent para subir a la carpeta 'A', y luego entramos a 'css' o 'templates'
css_dir = BASE_DIR.parent / "css"
templates_dir = BASE_DIR.parent / "templates"

templates = Jinja2Templates(directory=str(templates_dir))
app.mount("/static", StaticFiles(directory=str(css_dir)), name="static")

@app.get("/", response_class = HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = "index.html"
    )

@app.post("/predict", response_class = HTMLResponse)
async def predict(request: Request):

    # Extraer los datos del formulario
    longitude: float = Form(..., alias="longitude")
    latitude: float = Form(..., alias="latitude")
    housing_median_age: float = Form(..., alias="housing_median_age")
    total_rooms: float = Form(..., alias="total_rooms")
    total_bedrooms: float = Form(..., alias="total_bedrooms")
    population: float = Form(..., alias="population")
    households: float = Form(..., alias="households")
    median_income: float = Form(..., alias="median_income")
    median_house_value: float = Form(..., alias="median_house_value")
    ocean_proximity: str = Form(..., alias="ocean_proximity")

    # Aquí iría la lógica para predecir el precio usando un modelo ML
    # Por simplicidad, usaremos un valor fijo como predicción
    predicted_price = 250000  # Valor simulado

    return templates.TemplateResponse(
        request = request,
        name = "prediction.html",
        context = {
            "predicted_price": predicted_price
        }
    )



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)