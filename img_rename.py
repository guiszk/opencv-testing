import os, sys

if(len(sys.argv) != 2 or not os.path.isdir(sys.argv[1])):
    print("{0} <folder path>".format(sys.argv[0]))
    sys.exit(1)

imgdir = os.path.abspath(sys.argv[1])
print(imgdir)

a = 0

for root, dirs, files in os.walk(imgdir):
    for file in files:
        if(file.endswith("png") or file.endswith("jpg")):
            a += 1
            path = os.path.join(root, file)
            ext = os.path.splitext(file)[1]
            newpath = os.path.dirname(path) + "/" + str(a) + ext
            os.rename(path, newpath)
