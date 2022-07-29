import re
from typing import List, Dict

from app.util.SshClientUtil import SshClient
import app.services.ParseDevicesService as ParseDevicesService

def run(address: str, port: int, user: str, password: str):
    devices = ParseDevicesService.run()

    ssh = SshClient(address, user, password, port)
    response = ssh.executeAndClose("show call active voice brief")

    cicRegex = re.compile(r'\[\d+\/\d+\/\d+.\d+\]')
    cicList: List[str] = []

    for row in response:
        line = str(row).strip()
        foundCic = cicRegex.search(line)
        if foundCic != None:
            cicList.append(foundCic.group())

    print('cics found')
    print(cicList)
