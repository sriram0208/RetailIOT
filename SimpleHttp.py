from http.server import HTTPServer, BaseHTTPRequestHandler
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
            #    print(lis)
                
                json_data["mouseActions"].append({
                        'date':lis[0],
                        'time':lis[1],
                        'action':lis[2]
                    })            
            json_str=json.dumps(json_data)

        except:
            self.send_response(404)
        
        self.end_headers()
        self.wfile.write(bytes(json_str,'utf-8'))

httpd = HTTPServer(('localhost', 12345), SimpleHTTPRequestHandler)
httpd.serve_forever()