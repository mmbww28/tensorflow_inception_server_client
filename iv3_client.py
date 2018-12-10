from inception_client import InceptionClient

ic=InceptionClient('192.168.1.2:4100')
def run(image_list):
  return ic.run(image_list)


