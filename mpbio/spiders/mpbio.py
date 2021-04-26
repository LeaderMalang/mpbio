import scrapy


class MpbioSpider(scrapy.Spider):
    name = "mpbio"
    allowed_domains=['mpbio.com']
    start_urls = ['https://www.mpbio.com/us/life-sciences/']
    # def start_requests(self):
    #     urls = ['https://www.mpbio.com/us/life-sciences'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        print(response)
        li_div_elements=response.css('.main_ul')
        for li_div in li_div_elements:
            print(li_div)
            lis_element=li_div.css('ul li')
            for li in lis_element:
                req_url=li.css('a::attr(href)').get()
                yield scrapy.Request(url='https://www.mpbio.com//'+req_url, callback=self.parse_next)


    def parse_next(self,response):
        print(response)
        sub_categories_elements=response.css('.blue_bg')
        for sub_category in sub_categories_elements:
            next_url=sub_category.css('a::attr(href)').get()
            yield scrapy.Request(url=next_url, callback=self.parse_products)



    def parse_products(self,response):
        print(response)
        products_elements=response.css('.ais-InfiniteHits-item')
        for product in products_elements:
            print(product)