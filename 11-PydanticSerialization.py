from pydantic import BaseModel, ConfigDict # Importing the BaseModel class from the pydantic library to create data models with validation, and ConfigDict for custom configuration of the model.
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    addresses: Address  # A of Address instances, demonstrating a nested model
    tags: List[str] = []  # A list of tags associated with the user

    model_config = ConfigDict(json_encoders={datetime: lambda v: v.isoformat()})  # Custom JSON encoder for datetime fields


user = User(
    id=1,
    name="Alice",
    email="alice@gmail.com",
    created_at=datetime.now(),
    addresses=Address(street="123 Main St", city="Anytown", zip_code="12345"), # Creating a User instance with a nested Address instance
    tags=["admin", "user"]  # Adding some tags to the user
)   


pythonDict = user.model_dump() 
print(pythonDict) # This will print the dictionary representation of the User instance, including the nested Address and the list of tags. The created_at field will be serialized using the custom JSON encoder defined in the model_config.


jsonString = user.model_dump_json()
print(jsonString) # This will print the JSON string representation of the User instance, with the created_at field serialized as an ISO 8601 string due to the custom JSON encoder defined in the model_config.
