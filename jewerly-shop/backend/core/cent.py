from cent import Client
import os

cent_api_key = os.getenv('CENT_API_KEY')
cent_url = os.getenv('CENT_URL')

client = Client(cent_url, api_key=cent_api_key, timeout=1)