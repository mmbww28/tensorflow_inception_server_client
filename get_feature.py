import iv3_client
from PIL import Image

img=Image.open('lenna.jpg')
while True:
  result=iv3_client.run([img])
  print(str(len(result[0]))+'  '+str(result[0][:3])+'...')
