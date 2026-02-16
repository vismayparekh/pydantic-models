from pydantic import BaseModel, field_validator, model_validator # Importing BaseModel and field_validator from the pydantic library to create data models with validation and to define custom validation logic for fields


class User(BaseModel): # Defining a User class that inherits from BaseModel, which will allow us to create instances of User with automatic validation and type checking
    username: str

    @field_validator('username') # Using the field_validator decorator to define a custom validation method for the 'username' field
    def username_length(cls, value): # The validation method takes the class and the value of the field as parameters
        if len(value) < 4: # Checking if the length of the username is less than 4 characters
            raise ValueError('Username must be at least 4 characters long') # If the validation fails, a ValueError is raised with a descriptive message
        return value # If the validation passes, the original value is returned
    

class SignupForm(BaseModel): # Defining a SignupForm class that inherits from BaseModel, which will allow us to create instances of SignupForm with automatic validation and type checking
    
    password: str
    confirm_password: str

    @model_validator(mode='after') # Using the model_validator decorator to define a custom validation method that runs after all fields have been validated
    def passwords_match(cls, values): # The validation method takes the class and the entire model as parameters
        if values.password != values.confirm_password: # Checking if the password and confirm_password fields match
            raise ValueError('Passwords do not match') # If the validation fails, a ValueError is raised with a descriptive message
        return values # If the validation passes, the original model is returned
    

user = User(username="abcd")

signup_form = SignupForm(
    password="secret123",
    confirm_password="secret1234"
)

print(user)
print(signup_form)