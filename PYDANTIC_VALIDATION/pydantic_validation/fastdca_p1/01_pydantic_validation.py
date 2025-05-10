from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  

user_data = {"id": 1, "name": "Sakeena", "email": "sakeenamajeed341@gmail.com", "age": 16}
user = User(**user_data)
print(user)
print(user.model_dump())  
try:
    invalid_user = User(id="not_an_int", name="ladybug", email="ladybug12@gmail.com")
except ValidationError as e:
    print(e)