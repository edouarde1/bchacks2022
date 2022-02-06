from inspect import currentframe
from signal import pthread_kill
import sys
import pyaudio

import websockets
import asyncio
import base64
import json
import time
auth_key = "44ec744d87d14fa584a38733996cc167"

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
 
# starts recording
stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)

# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
file = open("words.txt",'w') 

async def send_receive():
    # print(f'Connecting websocket to url ${URL}')
    async with websockets.connect(
       URL,
       extra_headers=(("Authorization", auth_key),),
       ping_interval=5,
       ping_timeout=20
   ) as _ws:
       await asyncio.sleep(0.1)
    #    print("Receiving SessionBegins ...")
       session_begins = await _ws.recv()
    #    print(session_begins)
    #    print("Sending messages ...")
       async def send():
           while True:
               try:
                   data = stream.read(FRAMES_PER_BUFFER)
                   data = base64.b64encode(data).decode("utf-8")
                   json_data = json.dumps({"audio_data":str(data)})
                   await _ws.send(json_data)
               except websockets.exceptions.ConnectionClosedError as e:
                #    print(e)
                   assert e.code == 4008
                   break
               except Exception as e:
                   assert False, "Not a websocket 4008 error"
               await asyncio.sleep(0.01)
           return True
      
       async def receive():
           while True:
               try:
                   result_str = await _ws.recv()
                   word = str(json.loads(result_str)['text'])
                #    print(word)
                   if len(word) > 1 and word[-1] == '.':
                        print(word.strip()+" ")
                        sys.stdout.flush()
                        file.write(word.strip()+" ")
                #    print(json.loads(result_str)['text'])
               except websockets.exceptions.ConnectionClosedError as e:
                   print(e)
                   assert e.code == 4008
                   break
               except Exception as e:
                   assert False, "Not a websocket 4008 error"
      
       send_result, receive_result = await asyncio.gather(send(), receive())

asyncio.run(send_receive())