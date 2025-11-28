from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel




app = FastAPI()

# define el cuerpo de la respuesta que enviará la API al cliente
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/items/")
async def create_item(item: Item):
    return item



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)