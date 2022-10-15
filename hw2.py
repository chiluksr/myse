from flask import Flask
import requests

r =requests.get('https://api.openweathermap.org/data/2.5/weather?q=Corvallis,us&APPID=8690c802a1c06c1d54a6d81e45acd971')

app = Flask(__name__)

@app.route('/')
def api_call():
    return r.text
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()