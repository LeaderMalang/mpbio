import scrapy
from scrapy_selenium import SeleniumRequest
import ipdb
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


            yield SeleniumRequest(url=next_url, callback=self.parse_products)



    def parse_products(self,response):
        print(response)
        driver = response.request.meta['driver']
        products_elements=response.css('.ais-InfiniteHits-item')
        for product in products_elements:
            print(product)
            product_url=product.css('.ais-InfiniteHits-item a::attr(href)').get()
            yield SeleniumRequest(url=product_url, callback=self.parse_single_product)



        # ipdb.set_trace()
        # print(driver.page_source)


    def parse_single_product(self,response):
        items=dict()
        categories=response.css('.items li a::text').getall()

        name=response.xpath('//form[@id="product_addtocart_form"]/h1/text()').get()
        sku=response.xpath('//form[@id="product_addtocart_form"]/p/span/text()').get()
        cas_number=response.xpath('//form[@id="product_addtocart_form"]/div[3]/div[2]/div[2]/text()').get()
        molecular_formula=response.xpath('//form[@id="product_addtocart_form"]/div[3]/div[3]/div[2]/text()').get()
        descript_table=response.css('div.grid__column grid__column--2-3').get()
        items.update({
            'name': name,
            'sku': sku,
            'cas_number': cas_number,
            'molecular_formula': molecular_formula,
            'descript_table': descript_table,
            'categories':categories
        })
        print(items)
        yield items


