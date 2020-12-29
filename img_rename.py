import os, sys
 
if(len(sys.argv) != 2):
    print("{0} <path>".format(sys.argv[0]))
    sys.exit(1)
 
base_dir = os.path.dirname(os.path.abspath(sys.argv[1]))
 
 a = 0
 
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if(file.endswith("png") or file.endswith("jpg")):
            a += 1
            path = os.path.join(root, file)
            ext = os.path.splitext(file)[1]
            newpath = os.path.dirname(path) + "/" + str(a) + ext
            os.rename(path, newpath)
