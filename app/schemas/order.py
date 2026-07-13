from pydantic import BaseModel
from typing import List


class OrderCreate(BaseModel):
    items: List[str]
