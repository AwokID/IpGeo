"""
 IP GEOLOCATION BY AWOK ID
"""

banner = '''
 \033[1;36m+        \033[1;36m+   \033[1;36m+          \033[1;36m+         \033[1;36m+
    \033[1;36m+  \033[1;36m+           \033[1;36m+          \033[1;36m+
  \033[1;37m__          \033[1;36m+        \033[1;37m___            
 \033[1;37m|\033[1;33m##\033[1;37m|  ___    _   __  |\033[1;33m###\033[1;37m|  __       
 \033[1;37m|\033[1;33m##\033[1;37m| |\033[1;33m###\033[1;37m|  |\033[1;33m#\033[1;37m| |\033[1;33m##\033[1;37m| |\033[1;33m###\033[1;37m| |\033[1;33m##\033[1;37m|      
 |\033[1;33m##\033[1;37m| |\033[1;33m###\033[1;37m|  |\033[1;33m#| |\033[1;33m##\033[1;37m| |\033[1;33m###\033[1;37m| |\033[1;33m##\033[1;37m|      
 |\033[1;33m##\033[1;37m| |\033[1;33m###\033[1;37m|  |\033[1;33m#\033[1;37m| |\033[1;33m##\033[1;37m| |\033[1;33m###\033[1;37m| |\033[1;33m##\033[1;37m|      
 \033[1;32m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      

   \033[0;41mIP GEOLOCATION BY AWOK ID\033[0m

'''
import json, os, time
try:
  import requests
except ImportError:
  os.system("pip install requests")

os.system("cls" if os.name == "nt" else "clear")
print(banner)
try:
  ip = input("\033[1;31mIP \033[1;37mADDRESS\033[1;34m: \033[1;32m")
  time.sleep(0.5)

  req = requests.get("https://ipwhois.app/json/"+ip)
  response = json.loads(req.text)

  if req.status_code == 200:
    os.system("cls" if os.name == "nt" else "clear")
    print(banner)
    time.sleep(0.2)
    print("\033[1;32m+","\033[1;37m-"*50,"\033[1;32m+\n")
    time.sleep(0.2)
    print("\033[1;32mIP        \033[1;31m: \033[1;37m",response["ip"])
    time.sleep(0.2)
    print("\033[1;32mTYPE      \033[1;31m: \033[1;37m",response["type"])
    time.sleep(0.2)
    print("\033[1;32mBENUA     \033[1;31m: \033[1;37m",response["continent"])
    time.sleep(0.2)
    print("\033[1;32mNEGARA    \033[1;31m: \033[1;37m",response["country"])
    time.sleep(0.2)
    print("\033[1;32mIBUKOTA   \033[1;31m: \033[1;37m",response["country_capital"])
    time.sleep(0.2)
    print("\033[1;32mKODE TEL  \033[1;31m: \033[1;37m",response["country_phone"])
    time.sleep(0.2)
    print("\033[1;32mWILAYAH   \033[1;31m: \033[1;37m",response["region"])
    time.sleep(0.2)
    print("\033[1;32mKOTA      \033[1;31m: \033[1;37m",response["city"])
    time.sleep(0.2)

    # Membuat url google maps dengan Garis lintang dan garis bujur
    url = "https://www.google.com/maps?q="+response['latitude']+","+response['longitude']

    print("\033[1;32mMATA UANG \033[1;31m: \033[1;37m",response["currency"])
    time.sleep(0.2)
    print("\n\033[1;32m+","\033[1;37m-"*50,"\033[1;32m+\n")
    time.sleep(0.2)
    print("\033[1;32mLOKASI    \033[1;31m: \033[1;37m",url)
    time.sleep(0.2)
  else:
    exit("\n \033[0;41mIP NOT FOUND\033[0m ")
except KeyboardInterrupt:
  exit("\n\033[0;41mExit Program\033[0m")
except requests.exceptions.ConnectionError:
  exit("\n\033[0;41mCheck Your Network\033[0m")
except KeyError:
  exit("\n\033[0;41mNOT FOUND ")
