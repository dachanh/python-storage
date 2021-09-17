import sys
from pyseaweed import WeedFS
w = WeedFS('localhost',9333)

file_url = w.get_file_location(sys.argv[1])

print(file_url)