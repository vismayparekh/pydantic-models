from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    addresses: List[Address]  # A list of Address instances, demonstrating a nested model


address1 = Address(street="123 Main St", city="Anytown", zip_code="12345")

user = User(id=1, name="Alice", addresses=[address1]) # Creating a User instance with a nested list of Address instances

user_data = {
    "id": 2,
    "name": "Bob",
    "addresses": [
        {"street": "456 Elm St", "city": "Othertown", "zip_code": "67890"},
        {"street": "789 Oak St", "city": "Sometown", "zip_code": "54321"}
    ]
}   

user = User(**user_data) # Creating a User instance from a dictionary with nested address data. Pydantic will automatically validate and convert the nested dictionaries into Address instances.
print(user)