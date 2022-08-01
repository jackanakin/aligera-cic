from http.server import BaseHTTPRequestHandler, HTTPServer
import app.services.AppService as AppService


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        deviceDTOList = AppService.extractData()
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World!"
        
        ############################################
        ### Abertura do Html
        self.wfile.write(bytes("<html>", "utf8"))
        ### Definir o Head ###
        self.wfile.write(bytes("<head><meta http-equiv='refresh' content='60'></head>", "utf8"))
        ### Abertura do body
        self.wfile.write(bytes("<body>", "utf8"))
        ############################################

        ############################################
        ### INICIO DO CONTEÚDO
        #self.wfile.write(bytes(message, "utf8"))
        for device in deviceDTOList:
            self.wfile.write(bytes("<center><h1>{}</h1><div style=\"width: 90vw;\">".format(device.name), "utf8"))

            for slot in device.slotList:
                self.wfile.write(bytes("<h4>{}</h4>".format(slot.NAME), "utf8"))

                self.wfile.write(bytes("<div style=\"display: grid; grid-template-columns: repeat(6, 1fr 1fr); \">", "utf8"))
                for cic in slot.CICS:
                    status_color = "#08f308" if cic.CIC_STATUS == 0 else "#0178ef"
                    self.wfile.write(bytes("<div style=\"margin: 1px; border-style: solid; padding: 5px; width: 65px; height: 65px; background-color: {};\">".format(status_color), "utf8"))
                    self.wfile.write(bytes("<p>TS={}<br>CIC={}</p></div>".format(cic.TS_NAME, cic.CIC_NAME), "utf8"))
                self.wfile.write(bytes("</div>", "utf8"))

            self.wfile.write(bytes("</div></center>", "utf8"))
        ### FIM DO CONTEÚDO
        ############################################

        ############################################
        ### Fechamento do Html
        self.wfile.write(bytes("</html>", "utf8"))
        ### Fechamento do body
        self.wfile.write(bytes("</body>", "utf8"))
        ############################################

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()