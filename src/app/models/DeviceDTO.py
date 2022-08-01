from typing import List
from app.models.SlotDTO import SlotDTO 

class DeviceDTO:
  def __init__(self, name):
    self.name:str = name
    self.slotList:List[SlotDTO] = []