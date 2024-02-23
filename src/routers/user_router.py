from fastapi import APIRouter
from src.schemas.user_schema import UserCreate
from src.controllers.user_controller import UserController

UserRouter = APIRouter(
    tags=['User']
)

controller = UserController()

@UserRouter.get("/users")
async def get_users():
    """
        Endpoint responsible to get USERS data

        Returns:
            (JSON): USERS data list
    """

    return await controller.get_users()

@UserRouter.get("/user/{id}")
async def get_user_by_id(id: str):
    """
        Endpoint responsible to get USER data by an specific ID

        Args:
            id (str): Id of USER to be loaded

        Returns:
            (JSON): selected USER data
    """

    return await controller.get_user_by_id(id)

@UserRouter.post("/user")
async def post_user(data: UserCreate):
    """
        Endpoint responsible to create USERS data

        Args:
            data (UserSchema): USERS data to be created
        
        Returns:
            (bool): if the USER was successfully created
    """

    return await controller.post_user(data)

@UserRouter.put("/user")
async def put_user(data: UserCreate):
    """
        Endpoint responsible to update USERS data

        Args:
            data (UserSchema): USERS data to be updated
        
        Returns:
            (bool): if the USER was successfully updated
    """

    return await controller.post_user(data)

@UserRouter.delete("/user/{id}")
async def delete_user(id: str):
    """
        Endpoint responsible to delete USERS data

        Args:
            id (str): Id of USER to be deleted
        
        Returns:
    """

    return await controller.delete_user(id)