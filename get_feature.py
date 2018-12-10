import iv3_client
from PIL import Image
from mem_top import mem_top

counter=0
img=Image.open('lenna.jpg')
while True:
  result=iv3_client.run([img])
  #print(str(len(result[0]))+'  '+str(result[0][:3])+'...')
  if counter%100==0:
    print('mem_top: '+str(mem_top()))
    counter=0
  counter+=1

