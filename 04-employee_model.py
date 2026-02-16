from typing import Optional
from pydantic import BaseModel, Field # Importing BaseModel and Field from the pydantic library to create data models with validation and to define field constraints and metadata

# Defining an Employee class that inherits from BaseModel, which will allow us to create instances of Employee with automatic validation and type checking. The class includes fields for id, name, department, and salary, with specific constraints and default values where applicable.
class Employee(BaseModel):
    id: int
    name: str = Field(  
        ..., # The ellipsis (...) indicates that this field is required and must be provided when creating an instance of Employee.
        min_length=2,
        max_length=50,
        description="The full name of the employee, must be between 2 and 50 characters.",
        examples=["John Doe", "Jane Smith"]
    )
    department: Optional[str] = "General"  # Optional field with a default value of "General"
    slalary: float = Field(
        ...,
        ge=10000  # Salary must be greater than or equal to 10,000
        )  
    

emp = Employee(id=1, name="Alice Johnson", department="HR", slalary=55000) # Creating an instance of Employee with all fields provided
print(emp)