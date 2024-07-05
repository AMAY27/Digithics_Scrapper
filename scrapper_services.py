from scrapping import web_scrap
import random
import string

def generate_random_id():
    characters = string.ascii_lowercase + string.digits
    random_id = ''.join(random.choices(characters, k=24))
    return random_id

def scrap_data(params):
    print("Scrapping the data")
    website_url = params['websiteUrl']
    website_id = generate_random_id()
    web_scrap(website_url, website_id)