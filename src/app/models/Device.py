from typing import List
from app.models.Cic import Cic 

class Device:
  def __init__(self, name, address, port, user, password, command):
    self.name:str = name
    self.address:str = address
    self.port:int = port
    self.user:str = user
    self.password:str = password
    self.command:str = command
    self.cicList:List[Cic] = []