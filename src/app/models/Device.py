from typing import List
from app.models.Slot import Slot 

class Device:
  def __init__(self, name, address, port, user, password, command, regex):
    self.name:str = name
    self.address:str = address
    self.port:int = port
    self.user:str = user
    self.password:str = password
    self.command:str = command
    self.regex:str = regex
    self.slotList:List[Slot] = []