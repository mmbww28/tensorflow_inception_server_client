from inception_client import InceptionClient

ic=InceptionClient('http://127.0.0.1:2222')
def run(image_list):
  return ic.run(image_list)


