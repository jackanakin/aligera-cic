

class CicDTO:
  def __init__(self, TS_NAME, CIC_NAME):
    self.TS_NAME:str = TS_NAME
    self.CIC_NAME:str = CIC_NAME
    self.CIC_STATUS:int = 0 # 0 - livre, 1 - ocupado

