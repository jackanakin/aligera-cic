import re
from typing import List, Match
from app.models.Device import Device

from app.util.SshClientUtil import SshClient

def run(device: Device):
    ssh = SshClient(device.address, device.user, device.password, device.port)
    response = ssh.executeAndClose(device.command)

    cicInUseList: List[Match[str]] = []
    cicRegex = re.compile(device.regex)

    for row in response:
        line = str(row).strip()
        foundCic = cicRegex.search(line)
        if foundCic != None:
            cicInUseList.append(foundCic)

    for cic in device.cicList:
        for cicInUse in cicInUseList:
            if cic.CIC_MATCH in cicInUse.group():
                print('{} TS {}'.format(cic.CIC_NAME, cicInUse.group(1)))

    #print('cics found')
    print(cicInUseList)
