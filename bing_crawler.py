from icrawler.builtin import BingImageCrawler
import os, sys

if(len(sys.argv) != 3):
   print("{0} <folder name> <search term>".format(sys.argv[0]))
   sys.exit(1)

base_dir = os.path.abspath(str('images/' + sys.argv[1]))

print("Crawling...")
bing_crawler=BingImageCrawler(storage={'root_dir':str('images/' + sys.argv[1])})
bing_crawler.crawl(keyword=sys.argv[2], filters=None ,max_num=1000, offset=0)

a = 0

print("Renaming...")
for root, dirs, files in os.walk(base_dir):
      for file in files:
         if(file.endswith("png") or file.endswith("jpg")):
             a += 1
             path = os.path.join(root, file)
             ext = os.path.splitext(file)[1]
             newpath = os.path.dirname(path) + "/" + str(a) + ext
             os.rename(path, newpath)
