import json
from typing import List

from app.models.Device import Device 
from app.models.Cic import Cic 

def run():
    deviceList: List[Device] = []
    
    file = open("devices.json", "r")

    deviceDict: List[Device] = json.load(file)
    for each in deviceDict:
        name = each['name']
        address = each['address']
        port = each['port']
        user = each['user']
        password = each['password']
        command = each['command']
        regex = each['regex']

        device = Device(name, address, port, user, password, command, regex)
        cicList: List[Cic] = []

        for eachCic in each['cics']:
            CIC_NAME = eachCic['CIC_NAME']
            CIC_START = eachCic['CIC_START']
            CIC_COUNT = eachCic['CIC_COUNT']
            CIC_MATCH = eachCic['CIC_MATCH']

            cic = Cic(CIC_NAME, CIC_START, CIC_COUNT, CIC_MATCH)
            cicList.append(cic)

        device.cicList = cicList
        deviceList.append(device)

    return deviceList