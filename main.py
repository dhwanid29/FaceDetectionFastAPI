from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from routers import users

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)
# app.include_router(authentication.router)



# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}





# from routers import users, authentication, pin, comment


