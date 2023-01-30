from scrapy import cmdline

cmdline.execute('scrapy crawl baidu_top_spider -o ../baidu_top.json'.split())

