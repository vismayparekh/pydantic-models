from pydantic import BaseModel, field_validator, model_validator # Importing BaseModel and field_validator from the pydantic library to create data models with validation and to define custom validation logic for fields
from datetime import datetime # Importing the datetime class from the datetime module to work with date and time data in the validation logic


class Person(BaseModel): # Defining a Person class that inherits from BaseModel, which will allow us to create instances of Person with automatic validation and type checking
    first_name: str
    last_name: str

    @field_validator('first_name','last_name') # Using the field_validator decorator to define a custom validation method for the 'first_name' field
    def name_must_be_capitalized(cls, value): # The validation method takes the class and the value of the field as parameters
        if not value.istitle(): # Checking if the name is not capitalized (i.e., does not follow title case)
            raise ValueError('Name must be capitalized') # If the validation fails, a ValueError is raised with a descriptive message
        return value # If the validation passes, the original value is returned
    
    
class User(BaseModel): # Defining a User class that inherits from BaseModel, which will allow us to create instances of User with automatic validation and type checking
    email: str

    @field_validator('email') # Using the field_validator decorator to define a custom validation method for the 'email' field
    def normalize_email(cls, value): # The validation method takes the class and the value of the field as parameters
        return value.lower().strip() # Normalizing the email by converting it to lowercase and stripping any leading or trailing whitespace, and returning the normalized value
    

class Product(BaseModel): # Defining a Product class that inherits from BaseModel, which will allow us to create instances of Product with automatic validation and type checking
    price: float

    @field_validator('price', mode='before') # Using the field_validator decorator to define a custom validation method for the 'price' field that runs before the standard validation
    def parse_price(cls, value): # The validation method takes the class and the value of the field as parameters
        if isinstance(value, str): # Checking if the price is provided as a string
            return float(value.replace('$', '')) # If it is a string, remove any dollar signs and whitespace, convert it to a float, and return the parsed value
        return value # If it is not a string, return the original value (which will be validated as a float by pydantic)

    
class DateRange(BaseModel): # Defining a DateRange class that inherits from BaseModel, which will allow us to create instances of DateRange with automatic validation and type checking
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after') # Using the model_validator decorator to define a custom validation method that runs after all fields have been validated
    def check_date_range(cls, values): # The validation method takes the class and the entire model as parameters
        if values.start_date >= values.end_date: # Checking if the start date is not before the end date
            raise ValueError('Start date must be before end date') # If the validation fails, a ValueError is raised with a descriptive message
        return values # If the validation passes, the original model is returned
