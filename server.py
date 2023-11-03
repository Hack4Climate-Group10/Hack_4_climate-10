#my code
from flask import Flask, request
import threading 
import paho.mqtt.client as mqtt
import requests
import json
from mqtt_client import start_mqtt_subscriber
import random



app = Flask(__name__)

import os

response = ""
#identity = data_queue.get()
mqtt_data = {}




def calculating(amount):
    try:
        price = float(amount) * 1
    except Exception as e:
        raise Exception("Amount cannot be converted to valid number. Check and try again")
    return price

#///creating the methods of communiction

    
    
@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    
    print 
    global response
    global mqtt_data
    session_id = request.values.get("sessionId", None)#/////getting the session id
    service_code = request.values.get("serviceCode", None)#//////////getting the service code
    phone_number = request.values.get("phoneNumber", None)#getting the phone number that requested
    text =request.values.get("text", "default")#getting the request
    session_state = text.split('*')  
    
    current_level = len(session_state)
    

    
    
    
    
    if current_level == 1:
        response  = "CON Hello and welcome team Zuri Bin.We work with you to deliver your domestic waste prompty; when you need it.\n"
        response += "1. Report someone 's trash\n"
        response += "2. Report my own trash"
        
    elif current_level == 2 and session_state[1] == '1':
        response = "CON Hello and thank you  for reporting trash. Kindly choose location\n"
        response += "1:Nairobi\n"
        response += "2:We are currently not in other regions"
        
        
        
    elif current_level ==2 and session_state[1]== '2':
        response = "END Thanks we will try our best to get into your region."
    
    elif current_level ==3 and session_state[2]== '1':
        response = "CON Kindly specify  your region\n"
        response += "1:CBD\n"
        response += "2:Pipeline\n"
        response += "3:Kileleshwa\n"
        response += "4:Langata"
        
    elif current_level == 4 and session_state[3] == '1':
        response = "CON How big is your trash\n"
        response += "1:Big\n"
        response += "2:Medium\n"
        response += "3:Small"
        
    elif current_level == 5 and session_state[4] == '1':
        response = 'END Thank you. Your concern is noted.'  
                
    elif current_level == 5 and session_state[4] == '2':
        response = 'END Thank you. Your concern is noted.'
        
    elif current_level == 5 and session_state[4] == '3':
        response = 'END Thank you. Your concern is noted.'
        
    elif current_level == 5 and session_state[3] == '2':
        response = 'END Apparently we have not reached this region\n.'
    elif current_level == 5 and session_state[3] == '3':
        response = 'END Apparently we have not reached this region\n.'
    elif current_level == 5 and session_state[3] == '4':
        response = 'END Apparently we have not reached this region\n.'
    
    return response
      
        
   
#Receive response from africas talking
@app.route('/call', methods=['POST'])
def call_back_client():
    return '<Response> <Dial phoneNumbers="" maxDuration="5"/></Response>'


if __name__ == '__main__':
    mqtt_thread = threading.Thread(target=start_mqtt_subscriber)
 
    mqtt_thread.daemon = True
    # Daemonize the thread so it exits when the main thread exits
    mqtt_thread.start()
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))




