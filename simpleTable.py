from http.server import HTTPServer, BaseHTTPRequestHandler
from json2html import *
from json2table import convert
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            fh=open("mouse_log.txt","r")
            json_data={}
            json_data["mouseActions"]=[]
            while True:     
                line=fh.readline()
                if ("" == line):
                    print("file finished")
                    break;
                lis=line.split(" ",2)
                
                json_data["mouseActions"].append({
                        'date':lis[0],
                        'time':lis[1],
                        'action':lis[2]
                    })
#                json_str=json.loads(json_data)

        except:
            self.send_response(404)
            
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "class" : "table table-striped"}
        html = convert(json_data, build_direction=build_direction, table_attributes=table_attributes)
        table = json2html.convert(json=json_data)

        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(table,"utf-8"))


httpd = HTTPServer(('localhost', 12345), SimpleHTTPRequestHandler)
httpd.serve_forever()
