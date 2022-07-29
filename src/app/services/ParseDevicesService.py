import json
from typing import List
from app.models.Device import Device 

def run():
    file = open("devices.json", "r")
    deviceList: List[Device] = json.load(file)
    
    return deviceList