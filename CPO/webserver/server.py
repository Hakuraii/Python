#from http.server import HTTPServer, BaseHTTPRequestHandler
#import cgi
#import re
from flask import Flask, request, make_response, redirect, url_for
import mysql.connector as MC
from functools import wraps

app = Flask(__name__)



"""
dataArray = {}
class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path.endswith("/intervention")):
            self.send_response_only(200, dataArray['proxy'] + "." + dataArray['value'] + "." + dataArray['sides'])
            self.send_header('content-type', 'text/html')
            self.end_headers()
    
    def do_POST(self):
        if(self.path.endswith("/intervention")):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            ###pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-Length'))
            pdict['CONTENT-LENGTH'] = content_len

            data = str(self.rfile.read(pdict['CONTENT-LENGTH']))[1:].replace('\'','').replace("%40", '@')
            dataRawArray = re.split('[=&]', data)
            dataArray.clear()
            while len(dataRawArray) > 1:
                dataArray[dataRawArray[0]] = dataRawArray[1]
                dataRawArray = dataRawArray[2:]
            print(dataArray)
            self.send_response_only(301, data)
            self.end_headers()
"""

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)

        return redirect(url_for('index'))
        
    return decorated

@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return redirect(url_for('computerslist'))
    
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route('/computerslist')
@auth_required
def computerslist():
    try:
        page = "<table style=\"border:1px solid #333;\"><thead><tr><th style=\"border:1px solid #333;\">Com ID</th><th style=\"border:1px solid #333;\">Com Name</th><th style=\"border:1px solid #333;\">Com Proxy</th></thead><tbody>"
        con = MC.connect(host='xxxxx', database='RemoteOCComponents', user='xxxxx', password='xxxxx')
        cursor = con.cursor()

        query = 'SELECT * FROM Computers'
        cursor.execute(query)

        ComputersList = cursor.fetchall()

        for computer in ComputersList:
            page += "<tr><td style=\"border:1px solid #333;\">" + str(computer[0]) + "</td><td style=\"border:1px solid #333;\">" + str(computer[1]) + "</td><td style=\"border:1px solid #333;\">" + str(computer[2]) + "</td></tr>"
        page += "</tbody></table>"
            
    except MC.Error as err:
        return err
    finally:
        if(con.is_connected):
            cursor.close()
            con.close()
        return page

def main():
    """
    PORT = 8635
    server = HTTPServer(('', PORT), echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()"""
    app.run(debug=True,port=8635,host="0.0.0.0")

if __name__ == '__main__':
    main()

#Small test
