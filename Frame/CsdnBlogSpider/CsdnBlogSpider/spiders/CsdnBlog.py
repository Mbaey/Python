import scrapy
import urllib

class CsdnBlogSpider(scrapy.Spider):
    name = 'csdn_blog'
    baseURL='https://blog.csdn.net/u011054333/article/list/'
    start_urls = ['https://blog.csdn.net/u011054333/article/list/1']
    for i in range(2, 14):
        start_urls.append(baseURL+str(i))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = 'http://blog.csdn.net'

    def parse(self, response):
        articles = response.css('div[class="article-item-box csdn-tracking-statistics"]')
        for article in articles:
            title = article.css('a[target="_blank"]::text').extract_first().strip()
            title = articles[0].css('h4 a::text').extract_first().strip()
            link = self.base_url + article.css('div.article_title a::attr(href)').extract_first()
            yield {'title': title, 'link': link}

        pages = response.css('div#papelist')
        next_page_url = pages.css('a').re_first('<a href=\"(.*)\">下一页')
        if next_page_url is not None:
            yield scrapy.Request(urllib.parse.urljoin(self.base_url, next_page_url))