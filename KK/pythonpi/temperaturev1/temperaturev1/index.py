##
##  filename: demo.py
## 
##  this is a wrapper for your main program, its primary purpose is to 
##  manage error messages and output your HTML, XML or JSON as required
##

from flask import Flask, request, make_response
application = Flask(__name__)

import traceback 
import os
import sys
CURRENTDIR = os.path.dirname(os.path.abspath(__file__))
if CURRENTDIR not in sys.path:
    sys.path.append(CURRENTDIR)
    
def wsErrorTextHTML(txt):
    ## displays the python error on the web page - useful for debugging
    ## but on a live system would have it save the error to a database and give the user an error number
    err = "<p>ERROR!</p>"
    err += "<pre>"+ txt + "</pre>"
    return err

@application.errorhandler(500)
def internalServerError(error): 
    err = "<p>ERROR! 500</p>"
    err += "<pre>"+ str(error) + "</pre>"
    err += "<pre>"+ str(traceback.format_exc()) + "</pre>"
    return err

@application.route('/', methods=['POST', 'GET'])
def indexApp():
    
    try:
        ##
        ## ...your code goese here...
        ## I normally create a seperate 'core' application, in this case demoCore.py
        ##
        from demoCore import DemoCore
        demoCore = DemoCore()
        htmlData = demoCore.index(request)

        ## output your html code
        response = make_response(htmlData)
        response.headers['Content-Type'] = 'text/html'
        return response
    except:
        ## for when you get an error message
        response = make_response(wsErrorTextHTML(traceback.format_exc()))
        response.headers['Content-Type'] = 'text/html'
        return response

    response = make_response("unkown!")
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == "__main__":
    application.debug = True
    application.run()