# purpose: give program an article ID and return it's title, impact statement and DOI using the eLife API

# tell python you want to use the requests library you have installed
import requests

# tell Python what string to use for your article ID
article_id = '33065'

# normally define a variable name in upper case if you expect it not to change, standard practise. Use lowercase where variables will change.
URL = 'https://api.elifesciences.org/articles/' + article_id

# creating a tuple [collection] called FIELDS, won't change in contents so using capitalsied variable name. Note use of camelCase.
FIELDS = ('title','impactStatement','doi', 'published')

# I want requests library to get me article data from URL and convert to JSON
article = requests.get(URL).json()

# add a for loop to print the information in FIELDS for each article. Here, 'field' is a temporary variable, a name for the information behind it.
for field in FIELDS:
    print(article[field])
