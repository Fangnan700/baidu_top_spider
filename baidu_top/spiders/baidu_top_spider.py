import time

from scrapy import Selector
import scrapy

from baidu_top.items import BaiduTopDay


class BaiduTopSpiderSpider(scrapy.Spider):
    name = 'baidu_top_spider'
    allowed_domains = ['top.baidu.com']
    start_urls = ['https://top.baidu.com/board']

    def parse(self, response):
        # 创建元素选择器
        selector = Selector(response)

        # 获取热搜列表
        top_list = selector.css('#sanRoot > main > div.hot-wrap_1nNog > div.theme-hot.category-item_1fzJW > div.list_1EDla > a.item-wrap_2oCLZ')

        # 创建当天数据对象
        date_top = BaiduTopDay()
        date_top_data_list = []

        # 遍历列表，获取单个元素
        index = 0
        for top_item in top_list:
            # 创建热搜对象
            top_obj = {
                'index': index,
                'title': top_item.css('div.c-single-text-ellipsis::text').extract_first().strip(),
                'link': top_item.attrib['href']
            }
            date_top_data_list.append(top_obj)
            index += 1

        date_top['time'] = int(round(time.time() * 1000))
        date_top['data'] = date_top_data_list
        yield date_top



