from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "New App"
    admin_email: str = "yogesh@gmail.com"

def get_settings():
    return Settings()


@app.post('/signup')
def signup(user: UserSignup):
    return {'message': f'User {user.username} signed up successfully'}

@app.get('/settings')
def get_setttings_endpoint(settings: Settings = Depends(get_settings)):
    return settings