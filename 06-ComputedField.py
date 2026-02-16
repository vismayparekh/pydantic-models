from pydantic import BaseModel, computed_field, Field # Importing BaseModel and computed_field from the pydantic library to create data models with validation and to define computed fields that are calculated based on other fields


class Product(BaseModel): # Defining a Product class that inherits from BaseModel, which will allow us to create instances of Product with automatic validation and type checking
    price: float
    quantity: int

    @computed_field # Using the computed_field decorator to define a method that will be treated as a computed field, which means its value will be calculated based on other fields in the model
    @property # Using the property decorator to allow the computed field to be accessed like an attribute
    def total_price(self) -> float: # The method calculates the total price by multiplying the price and quantity fields
        return self.price * self.quantity # Returning the calculated total price
    

class Booking(BaseModel): # Defining a Booking class that inherits from BaseModel, which will allow us to create instances of Booking with automatic validation and type checking
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1) # Defining the nights field with a constraint that it must be greater than or equal to 1, and it is required (indicated by the ellipsis ...)
    rate_per_night: float

    @computed_field # Using the computed_field decorator to define a method that will be treated as a computed field, which means its value will be calculated based on other fields in the model
    @property # Using the property decorator to allow the computed field to be accessed like an attribute
    def total_cost(self) -> float: # The method calculates the total cost by multiplying the nights and rate_per_night fields
        return self.nights * self.rate_per_night # Returning the calculated total cost
    
booking = Booking(user_id=1, room_id=101, nights=3, rate_per_night=150.0) # Creating an instance of Booking with the required fields provided
print(booking.total_cost) # Accessing the computed field total_cost, which will calculate and return the total cost based on the nights and rate_per_night fields
print(booking.model_dump()) # Printing the model data, which will include the computed field total_cost along with the other fields of the Booking instance
