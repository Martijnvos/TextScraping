# The following docs have been used with helping to create the code in this file: 
# - http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests

# Query the results of searching for 'ICT' on the official Fontys website.
# This returns the page data of the particular link.
page = requests.get('https://fontys.nl/web/show/search?id=91407&langid=43&from=&to=&webid=26098&searchid=4604001&keyword=ICT')

# Gets the contents of the page in order to create a HTML tree
tree = html.fromstring(page.content)

# Parse the data based on the location of the element in the HTML hierarcy.
# Everything is located in a section with a class search-result and employee.
# The classes 'columns' and 'small-12' show that the page is constructed with a grid system, but that's beyond the point ;)

# Titles of search results are located in a div with the classes 'columns' and 'small-12' 
# This document has an h3 tag with the title as text inside.
# The text is parsed by calling text() on the h3 tag containing the information.
titles = tree.xpath('//section[@class="row block search-result employee"]/div[@class="columns small-12"]/h3/text()')

# Mail information of search results are located in a div with the classes 'columns', 'small-12' and 'large-6' 
# This document has an p tag with a link containing the mail address as text inside.
# The text is parsed by calling text() on the a tag containing the information.
mails = tree.xpath('//section[@class="row block search-result employee"]/div[@class="columns small-12 large-6"]/p[@class="icon icon-mail"]/a/text()')

# Phone numbers of search results are located in a div with the classes 'columns', 'small-12' and 'large-6'
# This document has a p tag with the classes 'icon' and 'icon-phone' with the phone number as text inside.
# The text is parsed by calling text() on the h3 tag containing the information.
phones = tree.xpath('//section[@class="row block search-result employee"]/div[@class="columns small-12 large-6"]/p[@class="icon icon-phone"]/text()')

# Location information of search results are located in a div with the classes 'columns', 'small-12'  and 'large-6'
# This document has a p tag with the classes 'icon' and 'icon-location' with the phone number as text inside an a tag.
# The text is parsed by calling text() on the a tag containing the information.
locations = tree.xpath('//section[@class="row block search-result employee"]/div[@class="columns small-12 large-6"]/p[@class="icon icon-location"]/a/text()')

# Loops through the list of locations and strips every \n, \t, and \r in the given location
locations = [s.strip() for s in locations]

print("titles: ", titles)
print("mails: ", mails)
print("phones: ", phones)
print("locations: ", locations)