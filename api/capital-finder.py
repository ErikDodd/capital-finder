from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)

        url = "https://restcountries.com/v3.1/capital/"
        user_input = input("> ")
        request = requests.get(url + user_input)
        data = request.json()
        countries_searched = []
        for countries in data:
            country = countries[0]["capital"]
            countries_searched.append(country)
        message = f"The capital of {countries_searched} is Y"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()


        self.wfile.write(message.encode())

        return

