from pydantic import BaseModel # Importing the BaseModel class from the pydantic library to create data models with validation

class Product(BaseModel): # Defining a Product class that inherits from BaseModel, which will allow us to create instances of Product with automatic validation and type checking
    id: int
    name: str
    price: float
    in_stock: bool = True

productOne = Product(id=1, name="Laptop", price=999.99, in_stock=True) # All fields are provided
productTwo = Product(id=2, name="Smartphone", price=499.99) # 'in_stock' will default to True since it's not provided
productThree = Product(name="Headphones") # This will raise a validation error because 'id' and 'price' are required fields