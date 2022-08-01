import re
from typing import List, Match
from app.models.Device import Device
from app.models.DeviceDTO import DeviceDTO
from app.models.SlotDTO import SlotDTO
from app.models.CicDTO import CicDTO

from app.util.SshClientUtil import SshClient

def run(device: Device):
    #################################################################
    ### EXTRAIR DADOS
    cicInUseList: List[Match[str]] = []
    cicRegex = re.compile(device.regex)

    ssh = SshClient(device.address, device.user, device.password, device.port)
    response = ssh.executeAndClose(device.command)  

    for row in response:
        line = str(row).strip()
        foundCic = cicRegex.search(line)
        if foundCic != None:
            cicInUseList.append(foundCic)
    #################################################################

    #################################################################
    ### FORMATAR DADOS
    deviceDTO = DeviceDTO(device.name)
    slotDTOList: List[SlotDTO] = []

    for slot in device.slotList:
        slotDTO = SlotDTO(slot.NAME, slot.CIC_MATCH)
        cicDTOList: List[CicDTO] = []
        start = slot.CIC_START
        count = slot.CIC_COUNT
        index = 0

        while (index <= count):
            cicDTO = CicDTO(CIC_NAME="{}".format(start+index), TS_NAME="{}".format(index+1))
            cicDTOList.append(cicDTO)
            index = index + 1
        
        slotDTO.CICS = cicDTOList
        slotDTOList.append(slotDTO)

    deviceDTO.slotList = slotDTOList

    for slot in deviceDTO.slotList:
        for cic in slot.CICS:
            for eachCicInUse in cicInUseList:
                if (slot.CIC_MATCH in eachCicInUse.group() and int(cic.TS_NAME) == int(eachCicInUse.group(1))):
                    cic.CIC_STATUS = 1
                    #print("Slot {} TS {}".format(slot.NAME, cic.TS_NAME))

    #print('cics found')
    print(cicInUseList)
    return deviceDTO
