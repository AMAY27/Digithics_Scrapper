from scrapping import web_scrap
from flask import Blueprint, jsonify, request, send_file
from flask_cors import cross_origin
from scrapper_services import scrap_data
import random
import string
import io


digithics_scrapper = Blueprint('digithics_scrapper', __name__, url_prefix='/digithicScrapper')

@digithics_scrapper.route('/scrapWebsite', methods=['POST'])
@cross_origin()
def scrap_website_for_dark_pattern_text():
   #return scrap_data(params=request.json)
   params=request.json
   website_url = params['websiteUrl']
   website_id = generate_random_id()
   df = web_scrap(website_url)
   buffer = io.BytesIO()
   df.to_csv(buffer, index=False, encoding='utf-8')
   buffer.seek(0)
   return send_file(buffer, mimetype='text/csv', as_attachment=True, attachment_filename='{}.csv'.format(website_id))

def generate_random_id():
    characters = string.ascii_lowercase + string.digits
    random_id = ''.join(random.choices(characters, k=24))
    return random_id