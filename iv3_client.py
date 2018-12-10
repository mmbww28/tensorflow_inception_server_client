import sys
sys.path.insert(0, './so')
from zc import Zc

c=Zc('127.0.0.1:2223')
def run(image_list):
  return c.run(image_list)


