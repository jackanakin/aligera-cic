from typing import List
from app.models.DeviceDTO import DeviceDTO
import app.services.GetCicService as GetCicService
import app.services.ParseDevicesService as ParseDevicesService

def extractData():
    deviceList = ParseDevicesService.run()
    deviceDTOList: List[DeviceDTO] = []

    for device in deviceList:
        deviceDTO = GetCicService.run(device)
        deviceDTOList.append(deviceDTO)

    return deviceDTOList
