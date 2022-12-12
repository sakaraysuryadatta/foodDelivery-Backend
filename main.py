from fastapi import FastAPI
import models
from database import  engine
from routes import user,seller,authentication,order
app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(order.router)
app.include_router(user.router)
#app.include_router(seller.router)
