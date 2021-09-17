import sys
from pyseaweed import WeedFS
w = WeedFS('localhost',9333)

fid = w.upload_file(sys.argv[1])
print(fid)