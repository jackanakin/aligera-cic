import re
from typing import List
from app.models.Device import Device

from app.util.SshClientUtil import SshClient

def run(device: Device):
    ssh = SshClient(device.address, device.user, device.password, device.port)
    response = ssh.executeAndClose(device.command)

    cicRegex = re.compile(r'\[\d+\/\d+\/\d+.\d+\]')
    cicStringList: List[str] = []

    for row in response:
        line = str(row).strip()
        foundCic = cicRegex.search(line)
        if foundCic != None:
            cicStringList.append(foundCic.group())

    print('cics found')
    print(cicStringList)
