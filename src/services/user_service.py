from src.schemas.user_schema import UserSchema, UserCreate
from src.config.db_config import db
import uuid

class UserService():
    """
        This service class is responsible to provide the internal services 
        related to USERS data
    """

    async def get_users(self):
        users = db.collection('users')
        documents = users.stream()

        return [UserSchema(**{"id": document.id, **document.to_dict()}) for document in documents]
    
    async def get_user_by_id(self, document_id: str):
        document = db.collection("users").document(document_id).get()
        user = UserSchema(**{"id": document.id, **document.to_dict()})

        return user
    
    async def post_user(self, user: UserCreate):
        document_id = str(uuid.uuid4())
        data = user.model_dump()

        return await db.collection("users").document(document_id).set(data)
    
    async def put_user(self, user: UserSchema):
        data = UserCreate(**user).model_dump()

        return await db.collection("users").document(str(user.id)).set(data)
    
    async def delete_user(self, document_id: str):
        return await db.collection("users").document(document_id).delete()