import sys
import app.services.AppService as AppService
import app.testdb as TestDB


help = "Comando inválido!\nDigite 'help' para mostrar ajuda"
commandList = "start - Rodar o programa"
commandList = commandList + '\ntestdb - Executar teste no banco de dados'

argc = len(sys.argv)
if argc < 2:
   print(help)
   exit()

command = sys.argv[1]

if command == 'help':
   print(commandList)
elif command == 'start':
   AppService.extractData()
elif command == 'testdb':
   TestDB.run()
else:
   print(help)
   exit()
