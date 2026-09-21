from pydantic import BaseModel 

class product(BaseModel):
    id : int
    name : str
    title : str
    price : float
    quantity : float

