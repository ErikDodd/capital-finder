from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        if "name" in dictionary:
            url = "https://restcountries.com/v3.1/name/"
            request = requests.get(url + dictionary["name"])
            data = request.json()
            countries_searched = []
            for countries in data:
                country = countries["capital"][1]
                countries_searched.append(country)
            message = f"The capital of {dictionary['name']} is {countries_searched[0]}"
        else:
            message = "Please give us the name of a country"


        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()


        self.wfile.write(message.encode())

        return

