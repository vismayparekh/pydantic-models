from pydantic import BaseModel # Importing the BaseModel class from the pydantic library to create data models with validation
from typing import Optional, List, Dict # Importing Optional, List, and Dict from the typing module to use for type annotations in our data models


# Defining a CartItem class that inherits from BaseModel, which will allow us to create instances of CartItem with automatic validation and type checking
class Cart(BaseModel):
    user_id: int
    items: List[str] # A list to store the names of the items in the cart
    quantities: Dict[str, int] # A dictionary to store the quantity of each item in the cart, where the key is the item name and the value is the quantity


# Defining a BlogPost class that inherits from BaseModel, which will allow us to create instances of BlogPost with automatic validation and type checking. This class includes optional fields for image URL, tags, and metadata, demonstrating how to use Optional and complex data types in pydantic models.
class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None  # An optional field for the URL of an image associated with the blog post. If not provided, it will default to None.



# An optional field for tags associated with the blog post. This is a list of strings, and if not provided, it will default to an empty list.
cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Smartphone", "Headphones"],
    "quantities": {"Laptop": 1, "Smartphone": 2, "Headphones": 3}
}

cart_item = Cart(**cart_data) # This will create a Cart instance with the provided data. If any of the fields are missing or have incorrect types, pydantic will raise a validation error.
print(cart_item)