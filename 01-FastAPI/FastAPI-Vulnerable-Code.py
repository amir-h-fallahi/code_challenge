
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

class User(BaseModel):
	email: str = ""
	password: str = ""
	role: Literal[ "user", "admin"]
	disabled: bool = False
	is_user_verified: bool = False


@app.put("/user/auth/signup/")
def user_signup(user: User):
	db.collection("users").insert(user.dict())
	return {
		"success": True,
		"message": "your account has been created successfully"
	}
