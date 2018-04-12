import scrapy
import w3lib.html
from ..items import TestItem

class TestSpider(scrapy.Spider):
	name = "Test"
	
	start_urls = [
		'https://www.irif.univ-paris-diderot.fr/seminaires/algo/index'
	]
#----------------------------------------------------------------------------------------
"""Parse the contact on the website and the next seminar
"""
	def _parse_Contact(self, response):
		self.logger.info("Je suis ici")
		contact = response.xpath('//a[@href="https://www.irif.fr/~lboczko/"]').extract_first()
		contact = w3lib.html.remove_tags(contact)
		return contact

	def _parse_logging(self, response):
		self.logger.info("Le loggeur fonctionne et le spider crawl")
		

	def _parse_PS(self, response):
		self.logger.info("Esque cela fonctionne")
		PS = response.xpath('//div[@id="plugin_include__seminaires__algocomp__db__futur"//div[contains(@class,"datatemplateentry")]/p[1]')
		PS = w3lib.html.remove_tags(PS)
		return PS

#----------------------------------------------------------------------------------------

"""Main Parse
"""
	def parse(self, response):
		contacte = self._parse_Contact(response) #Call the parse contact 
		Prochaine_Seance = self._parse_PS(response)
		self._parse_logging(response)
		contacte = TestItem(contactName=contacte) #Put the scraped data into an item
		Prochaine_Seance = TestItem(Ps = Prochaine_Seance)
		return contacte, Prochaine_Seance
