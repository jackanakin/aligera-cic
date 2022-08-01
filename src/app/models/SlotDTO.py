from typing import List
from app.models.CicDTO import CicDTO


class SlotDTO:
  def __init__(self, NAME, CIC_MATCH):
    self.NAME:str = NAME
    self.CICS:List[CicDTO] = []
    self.CIC_MATCH:str = CIC_MATCH
