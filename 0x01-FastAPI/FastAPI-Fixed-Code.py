
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.networks import EmailStr
import hashlib

app = FastAPI()

class User(BaseModel):
	email: EmailStr
	password: str
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		password_hash = hashlib.sha512(self.password.encode('UTF-8')).hexdigest()
		object.__setattr__(self, "password" , password_hash)
		object.__setattr__(self, "role" , "user")
		object.__setattr__(self, "disabled" , False)
		object.__setattr__(self, "is_user_verified" , False)


@app.put("/user/auth/signup/")
def user_signup(user: User):
	db.collection("users").insert(user.dict())
	return {
		"success": True,
		"message": "your account has been created successfully"
	}
