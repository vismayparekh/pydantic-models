from pydantic import BaseModel # Importing the BaseModel class from the pydantic library to create data models with validation

# Defining a User class that inherits from BaseModel, which will allow us to create instances of User with automatic validation and type checking
class User(BaseModel):
    id: int
    name: str
    is_active: bool

# Creating an instance of the User class using a dictionary of input data. The ** operator is used to unpack the dictionary into keyword arguments for the User constructor.
input_data = {
    "id": 101,
    "name": "Alice",
    "is_active": True
}

user = User(**input_data) # This will create a User instance with the provided data. If any of the fields are missing or have incorrect types, pydantic will raise a validation error.
print(user)