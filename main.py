import os
import argparse
import math
import time
import numpy as np

# VARIABLES
ismuseio = False


from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server, udp_client
# i <3 global variables
global ALPHA
global ALPHARIGHT
global ALPHALEFT
global BETA
global BETARIGHT
global BETALEFT
global DELTA
global GAMMA
global THETA
global THETARIGHT
global THETALEFT
global BLINK
global JAW
global FOCUS
global FOCUSRIGHT
global FOCUSLEFT
global RELAX
global printrelay
global timesent
global timesent2
printrelay = ""
FOCUS = 0.0
FOCUSRIGHT = 0.0
FOCUSLEFT = 0.0
RELAX = 0.0
timesent = round(time.time(), 1)
timesent2 = round(time.time(), 1)



  # HI THERE, THANKS FOR LOOKING AT MY AWFUL CODE, I WROTE THIS IN 3 HOURS AND IT FUNCTIONS WELL ENOUGH, WILL FIX LATER, \
    # MATH NEEDS A LITTLE BIT MORE FINE TUNING BUT ITS ALL GOOD
  
def printvalues(wave):
   #SENDS THE MESSAGES OUT WITHOUT WAITING FOR THE PRINT BUFFER
  sendmessages()
  
  #PRINTING IS A GOD AWFUL MESS, VALUES CHANGE PLACES THROUGHOUT TESTING AND I NEED A BETTER SYSTEM FOR THIS
  if "Blinking?" in wave:
    sendblink()
  if "Jaw?" in wave:
    sendjaw()
  globals()["FOCUS"] = abs(calculate_ratio(globals()["BETA"], globals()["THETA"]))
  globals()["FOCUSLEFT"] = abs(calculate_ratio(globals()["BETALEFT"], globals()["THETALEFT"]))
  globals()["FOCUSRIGHT"] = abs(calculate_ratio(globals()["BETARIGHT"], globals()["THETARIGHT"]))
  globals()["RELAX"] = calculate_ratio(globals()["ALPHA"], globals()["THETA"])
  print("it is working, you can be at peace with that knowledge right?")
  
 
                  
            
  
 
  
    
    #USED TO SET THE GLOBAL VALUES, FROM -1 TO UNKNOWN; MAX IVE SEEN THESE VALUES GO IS 1.6)
    #we use the normalize function to account for this while calculating focus, as
    #Charles' math doesnt account for numbers above 1 or in the negatives
    #we do lose a bit of accuracy with this method, assuming 2 is the max

def setalpha(unused_addr, args, a, b ,c, d):
  globals()["ALPHA"] = getaverage(a, b, c, d)
  globals()["ALPHALEFT"] = getaverage(a, b, a, b)
  globals()["ALPHARIGHT"] = getaverage(c, d, c, d,)
  printvalues(str(ALPHA) + " Alpha")

def setbeta(unused_addr, args, a, b ,c, d):
  globals()["BETA"] = getaverage(a, b, c, d)
  globals()["BETALEFT"] = getaverage(a, b, a, b)
  globals()["BETARIGHT"] = getaverage(c, d, c, d)
  printvalues(str(BETA) + " Beta")
  

def setdelta(unused_addr, args, a, b ,c, d):
  globals()["DELTA"] = getaverage(a, b, c, d)
  printvalues(str(DELTA) + " Delta")

def setgamma(unused_addr, args, a, b ,c, d):
  globals()["GAMMA"] = getaverage(a, b, c, d)
  printvalues(str(GAMMA) + " Gamma")

def settheta(unused_addr, args, a, b ,c, d):
  globals()["THETA"] = getaverage(a, b, c, d)
  globals()["THETALEFT"] = getaverage(a, b, a, b)
  globals()["THETARIGHT"] = getaverage(c, d, c, d)
  printvalues(str(THETA) + " Theta")

def setjaw(unused_addr, args, a): #blinking is the only one of these that is 0 to 1, easy.
  globals()["JAW"] = a
  printvalues(str(BLINK) + " Jaw?")

def setblink(unused_addr, args, a): #blinking is the only one of these that is 0 to 1, easy.
  globals()["BLINK"] = a
  printvalues(str(BLINK) + " Blinking?")

def getaverage(a, b, c, d): #we have 4 channels, gets the average of those.
  a = float(a)
  b = float(b)
  c = float(c)
  d = float(d)
  average = (a+b+c+d)/4
  normal_avg = normalize(average)
  return normal_avg

def tanh_normalize(data, scale, offset): #i think this is what charles meant when he told me he used a sigmoid function?
  return np.tanh(scale * (data + offset)) #ngl, i stole this from BFiVRC

def normalize(num, min_val=-1, max_val=2): #normalize from (-1 to 2) to (0 to 1)
    # Normalize the value
    normalized_value = (num + 1) / 2
    return normalized_value
    
  
def calculate_ratio(numerator, denominator): #calculates focus ratio!
        try: 
          #return tanh_normalize(numerator / denominator, .8, -5)
          return tanh_normalize(numerator / denominator, 1, -1)
        except:
          return 0.0 
        
def sendmessages():
  
  client = udp_client.SimpleUDPClient("127.0.0.1", 9000) # SENDS DATA TO VRCHAT OVER PARAMS FOCUS, FOCUSLEFT AND FOCUSRIGHT
  client.send_message("/avatar/parameters/FocusRight", globals()["FOCUSRIGHT"])
  client.send_message("/avatar/parameters/FocusLeft", globals()["FOCUSLEFT"])
  client.send_message("/avatar/parameters/Focus", globals()["FOCUS"])
  
  
def sendchatbox():
  focusr = str(round(globals()["FOCUSRIGHT"], 6))
  focusl = str(round(globals()["FOCUSLEFT"], 6))
  focusavg = str(round(globals()["FOCUS"], 6))
  messagestring = "←OSC Brain Control→\v╔══════════╗\vRightFocus: %s \vLeftFocus: %s \v╚══════════╝" % (focusr, focusl)
  client = udp_client.SimpleUDPClient("127.0.0.1", 9000) # SENDS DATA TO VRCHAT OVER PARAMS FOCUS, FOCUSLEFT AND FOCUSRIGHT
  currenttime = round(time.time(), 1)
  
  if currenttime > globals()["timesent"] + 1.7:
    client.send_message("/chatbox/input", [messagestring , True, False])
    globals()["timesent"] = currenttime
  

def sendblink():
  client = udp_client.SimpleUDPClient("127.0.0.1", 9000) # SENDS DATA TO VRCHAT OVER PARAMS blink
  client.send_message("/avatar/parameters/Blink", globals()["BLINK"])

def sendjaw():
  client = udp_client.SimpleUDPClient("127.0.0.1", 9000) # SENDS DATA TO VRCHAT OVER PARAMS blink
  client.send_message("/avatar/parameters/Jaw", globals()["JAW"])

if __name__ == "__main__":
  os.system("start cmd /c muse-io --osc osc.udp://localhost:1647")
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=1647, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = Dispatcher()
  #RECIEVES DATA FROM MUSE-IO (DEPRECATED SDK FROM 2015 LMAOOO)
 
  dispatcher.map("/muse/elements/alpha_absolute", setalpha, "dddd")
  dispatcher.map("/muse/elements/beta_absolute", setbeta, "dddd")
  dispatcher.map("/muse/elements/delta_absolute", setdelta, "dddd")
  dispatcher.map("/muse/elements/gamma_absolute", setgamma, "dddd")
  dispatcher.map("/muse/elements/theta_absolute", settheta, "dddd")
  dispatcher.map("/muse/elements/blink", setblink, "i")
  dispatcher.map("/muse/elements/jaw_clench", setjaw, "i")



  server = osc_server.OSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever(0.1)

