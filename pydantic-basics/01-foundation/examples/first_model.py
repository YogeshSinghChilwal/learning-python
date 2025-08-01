from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {"id": 123, "name": "Yogesh", "is_active": "false"}

user = User(**input_data)
print(user)


#* without pydantic
# class User:
#     def __init__(self, id, name, is_active):
#         self.id = id
#         self.name = name
#         self.is_active = is_active

#     def __repr__(self):
#         return f"User(id={self.id}, name='{self.name}', is_active={self.is_active})"
