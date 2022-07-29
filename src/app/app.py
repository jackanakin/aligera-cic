from app.util.SshClientUtil import SshClient
import app.services.GetCicService as GetCicService
import app.services.ParseDevicesService as ParseDevicesService

def run():
    print("app started")
    deviceList = ParseDevicesService.run()

    for device in deviceList:
        GetCicService.run(device)

    print("app finished")