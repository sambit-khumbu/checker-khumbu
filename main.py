from flask import Flask,request,jsonify
import logging
from logging.handlers import RotatingFileHandler
app=Flask(__name__)
file_handler = RotatingFileHandler('python.log')
file_handler.setLevel(logging.ERROR)
app.logger.setLevel(logging.ERROR)
app.logger.addHandler(file_handler)
@app.route("/liOnboarding")
def onboarding():
    arg1=request.args['hiringcontext']
    arg2=request.args['extensiontype']
    arg3=request.args['redirecturl']
    arg4=request.args['signature']
    return 'hiringcontext:'+ arg1 +'extensiontype:'+arg2+'redirecturl'+arg3+'signature:'+arg4



@app.route("/liExtension")
def extension():
    return "learn more"

@app.route("/liCallback",methods=['POST'])
def callback():
    if request.method == 'POST':
        return "Request Processed"

if __name__ == "__main__":
    app.run(debug=True)
