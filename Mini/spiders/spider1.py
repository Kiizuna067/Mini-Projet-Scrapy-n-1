import scrapy 
import w3lib.html
#from .item import TestItem

"""The w3lib librarie will be use to take out all html tags.
"""

class TestSpider(scrapy.Spider):
	name = "Test1"

	start_urls = [
		'https://www.irif.univ-paris-diderot.fr/seminaires/algo/index'
	]

	def parse_contact(self, response):
		contact = response.xpath('//a[@href="https://www.irif.fr/~lboczko/"]').extract_first()
		contact = w3lib.html.remove_tags(contact)

	def parse_logging(self, response):
		self.logger.info("Tout à l'air de marcher")

	"""def parse_PS(self, response):
		PS = response.xpath('//div[@id="plugin_include__seminaires__algocomp__db__futur"//div[contains(@class,"datatemplateentry")]/p[1]')
		PS = w3lib.html.remove_tags(PS)"""




""""	def parse_item(self, response):
		self.logger.info("Let's call an item page!", response.url)
		item = TestItem
		item['Test'] = parse_contact()
		return item
"""

