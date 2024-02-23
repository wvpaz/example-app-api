from src.services.user_service import UserService
from src.schemas.user_schema import UserCreate

class UserController():
    """
        This controller is the main way to access USERS data via example-app API 
        and also is responsible to redirect calls to internal services.
    """

    def __init__(self) -> None:
        self.user_service = UserService()

    async def get_users(self):
        try:
            return await self.user_service.get_users()
        except Exception as exception:
            return exception
        
    async def get_user_by_id(self, document_id: str):
        try:
            return await self.user_service.get_user_by_id(document_id)
        except Exception as exception:
            return exception
        
    async def post_user(self, data: UserCreate):
        try:
            return await self.user_service.post_user(data)
        except Exception as exception:
            return exception
        
    async def put_user(self, data: UserCreate):
        try:
            return await self.user_service.put_user(data)
        except Exception as exception:
            return exception
        
    async def delete_user(self, document_id: str):
        try:
            return await self.user_service.delete_user(document_id)
        except Exception as exception:
            return exception