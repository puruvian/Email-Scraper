# UC Email Web Scraper

This program scrapes a particular UC faculty website to obtain the emails of professors and reserachers. A list of names is also collected. These emails and names are only collected from current, reseraching professors. In other words, teaching professors and emeritus faculty are not included. 


The program uses the BeautifulSoup4 library to conduct web scraping and the Selenium web driver to access sites which require the loading of JavaScript before emails can be collected. A version of the Selenium driver is included here for convenience, but running the program may require you to download an updated version of the driver, which can be found [here](https://selenium-python.readthedocs.io/installation.html).


I created this program to help me find professors to conduct reserach with, and other versions of this project use the ChatGPT API to write personalized emails to faculty. If you're interested, that can be found [here](https://github.com/puruvian/hackathon).


### Usage ###

To execute the program, simply run any of the Python files. Two .txt files are created in the local directory, one of which contains the emails and one of which contains the names.  
