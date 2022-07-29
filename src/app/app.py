from app.util.SshClientUtil import SshClient
import app.services.GetCicService as GetCicService

def run():
    print("app started")
    GetCicService.run(address='172.16.254.194', port=22, user='bradmin', password='brasrede')
    print("app finished")