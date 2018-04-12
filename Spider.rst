**************
Spider Section
**************

Here I will try to describe how I build the spider for the website :

`Irif.univ-paris-diderot.fr <https://www.irif.univ-paris-diderot.fr/seminaires/algo/index>`_

My first spider
===============

Contents

 * Import
 * Differents Parse 
 * Main Parse 

Import
------

I used three different import for this project. Each of them have been used and are necessary for the project.

Scrapy
~~~~~~
	First of all I used "import scrapy" library. You need it to create a scrapy spider.

w3lib.html
~~~~~~~~~~
	Then I called the w3lib.html library. It is a Python library and will allow us to remove all the html tag from the data we've parsed.

items
~~~~~
	Finaly I used an import item which is necessary to use the scrapy items functionnality.
	Scrapy items functionnality enable us to return an object to store the data and then export it to a CSV file.

Differents Parse
----------------

The parse was a little hard to organize. I divided it into 3 different parse for the data.
Then I call those 3 parses into a main parse that will use them and store the data into an Item to export them.

Parse the contact name :
~~~~~~~~~~~~~~~~~~~~~~~~

The first one parse the name of the Contact throught the page. When it found the good data it store it into a variable.
We will then use this variable and the w3lib.html library to remove all the tags around our data to keep only the text.
Once it's done we just return the contact variable

 .. code-block:: python 
   
   	def _parse_Contact(self, response):
		contact = response.xpath('//a[@href="https://www.irif.fr/~lboczko/"]').extract_first()
		contact = w3lib.html.remove_tags(contact)
		return contact

 

Found the next seminar :
~~~~~~~~~~~~~~~~~~~~~~~~

The second parse extract an entire bloc which contains all the information about the next seminar.
We extract all the bloc to have the name of the seminar, it date, hour and place

.. code-block:: python

    def _parse_PS(self, response):
		PS = response.xpath('//div[@id="plugin_include__seminaires__algocomp__db__futur"//div[contains(@class,"datatemplateentry")]/p[1]')
		PS = w3lib.html.remove_tags(PS)
		return PS

Security : 
~~~~~~~~~~

Finally the last one is just for security. We use a scrapy functionnality to show a message.
This message will just reassure us on the execution of our spider.

.. code-block:: python

    def _parse_logging(self, response):
		self.logger.info("Le loggeur fonctionne et le spider crawl")


Main Parse
----------

In the main parse we will call all our precedent parse one by one and storing them into a variable.
Each variable will in that case contains the data we needed.
We then store the scraped data into an item using our items library provided by scrapy.
Those new items will allow us to extract the data into a CSV file when we call our spider with the command.


**scrapy crawl spiderName -t csv -o NameOfFile.csv**

.. code-block:: python

	def parse(self, response):
		contacte = self._parse_Contact(response) #Call the parse contact 
		Prochaine_Seance = self._parse_PS(response)
		self._parse_logging(response)
		contacte = TestItem(contactName=contacte) #Put the scraped data into an item
		Prochaine_Seance = TestItem(Ps = Prochaine_Seance)
		return contacte, Prochaine_Seance
