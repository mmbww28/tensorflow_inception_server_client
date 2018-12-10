import iv3_client
from PIL import Image

img0=Image.open('lenna.jpg')
img1=Image.open('dolphin.jpg')
img2=Image.open('train.jpg')
while True:
  result=iv3_client.run([img0,img1,img2])
  print(str(len(result[0]))+'  '+str(result[0][:2])+' '+str(result[1][:2])+' '+str(result[2][:2]))

