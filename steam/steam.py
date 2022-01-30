import scrapy
from scrapy import Request
from newscrawler.newscrawler.items import SteamItem


class SteamSpider(scrapy.Spider):
    name = 'steam'
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers']

    def parse(self, response):
        item = SteamItem()
        games = response.css("#search_resultsRows").css("a")
        i=0
        for game in games:
            item['title'] = game.css(".title").css("span::text").extract()[0]
            item['image'] = response.css("#search_resultsRows").css("a").xpath("//div[@class='col search_capsule']/img").xpath("@src").extract()[i]
            item['date'] = response.css("#search_resultsRows").css("a").xpath("//div[@class='col search_released responsive_secondrow']/text()").extract()[i]
            i=i+1
            item['price'] = game.css(".search_price::text").extract_first().strip()
            if item['price'] == "":
                item['price'] = game.css(".search_price::text").getall()[1].strip()
            yield item

    
