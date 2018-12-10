import sys 
sys.path.insert(0, './so')
import iv3_client
from PIL import Image
import numpy as np

img=Image.open('dolphin.jpg')
host='localhost'
port=8000
while True:
  result=iv3_client.run([img], host, port)
  a=np.array(result)
  print(str(len(result[0]))+'  '+str(result[0][:3])+'...')

