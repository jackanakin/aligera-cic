import json
from typing import List

from app.models.Device import Device 
from app.models.Slot import Slot 

def run():
    deviceList: List[Device] = []
    file = open("json/devices.json", "r")
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
        slotList: List[Slot] = []

        for eachSlot in each['slotList']:
            NAME = eachSlot['NAME']
            CIC_START = eachSlot['CIC_START']
            CIC_COUNT = eachSlot['CIC_COUNT']
            CIC_MATCH = eachSlot['CIC_MATCH']

            slot = Slot(NAME, CIC_START, CIC_COUNT, CIC_MATCH)
            slotList.append(slot)

        device.slotList = slotList
        deviceList.append(device)

    return deviceList