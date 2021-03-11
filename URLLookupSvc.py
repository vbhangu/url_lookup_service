from urllib.parse import urlparse
import sqlite3
import json


class URLLookupSvc:

    def __init__(self, url):
        self.url = url

    def get_domain(self):
        if not self.url.startswith(('https://', 'http://')):
            self.url = "https://" + self.url

        output = urlparse(self.url)
        # print(output)
        domain = output.netloc.strip("www.")
        hostname = output.hostname
        port = output.port
        if port:
            return hostname
        else:
            return domain

    @staticmethod
    def view_db():
        conn = sqlite3.connect("malware_url.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM malware")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def if_found(domain, rows):
        for row in rows:
            if domain in row:
                return json.dumps({'Malware': True})
        return json.dumps({'Malware': False})



