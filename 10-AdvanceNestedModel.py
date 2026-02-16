from pydantic import BaseModel
from typing import Optional, List, Union

class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None

class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str

class Article(BaseModel):
    title: str
    content: List[Union[TextContent, ImageContent]]  # A list that can contain either TextContent or ImageContent instances


class Country(BaseModel):
    name: str
    code: str

class state(BaseModel):
    name: str
    country: Country  # Nested model to represent the relationship between state and country

class city(BaseModel):
    name: str
    state: state  # Nested model to represent the relationship between city and state

class Address(BaseModel):
    street: str
    city: city  # Nested model to represent the relationship between address and city
    zip_code: str

class Organization(BaseModel):
    name: str
    address: Address  # Nested model to represent the relationship between organization and address
    branches: List['Organization'] = []  # Self-referential model to represent branches of the organization

    