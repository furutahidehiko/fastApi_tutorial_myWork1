from fastapi import APIRouter
from enumModel import ModelName
router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the  current user"}


@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):

    task = {"model_name": model_name, "message": "Have some residuals"}

    if model_name is ModelName.alexnet:
        task = {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name.value == "lenet":
        task = {"model_name": model_name, "message": "LeCNN all the images"}
    else:
        pass
    return task
