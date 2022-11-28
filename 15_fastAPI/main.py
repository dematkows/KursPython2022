from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.counter = 0


class HelloResponse(BaseModel):
    msg: str


class Product(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)


# @app.get("/hello/{name}")
# async def hello_name(name):
#     return {f"Hello {name}! 👋"}


@app.get("/hello/{name}", response_model=HelloResponse)
async def hello_name(name: str):
    return HelloResponse(msg=f"Hello {name}! 👋")


@app.post("/product/", response_model=HelloResponse)
async def create_product(product: Product):
    return product
