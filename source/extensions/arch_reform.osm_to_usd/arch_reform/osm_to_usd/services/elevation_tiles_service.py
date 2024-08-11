import requests
import gzip

class ElevationTilesService():
    @classmethod
    def request_hgt_data(cls, file):
        url = "https://s3.amazonaws.com/elevation-tiles-prod/skadi/%s/%s" % (file[:3], file)
        response = requests.get(url)
        if response.headers.get('Content-Encoding') == 'gzip':
            data = gzip.decompress(response.content)
        else:
            data = response.content

        return data