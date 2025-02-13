from fastapi import FastAPI
from starlette.staticfiles import StaticFiles


# from routers import users, authentication, pin, comment

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)
app.include_router(authentication.router)
# app.include_router(pin.router)
# app.include_router(comment.router)
