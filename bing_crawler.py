from icrawler.builtin import BingImageCrawler

print("Crawling...")
bing_crawler=BingImageCrawler(storage={'root_dir':'images/jacob'})
bing_crawler.crawl(keyword='jacob collier',filters=None,max_num=100,offset=0)
