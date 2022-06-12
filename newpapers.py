import requests
from bs4 import BeautifulSoup
import os


class NewPaper:
    idx = 0

    urls = ['W2021', 'W2020', 'W2019', 'W2018', 'W2017', 'S2022', 'S2021', 'S2020', 'S2019', 'S2018']

    def __init__(self, path, subject_codes, subject_name):
        self.path = path
        self.subjectCodes = subject_codes
        self.subject_name = subject_name

    def getUrl(self, season, subject_code):
        paper_url = "https://www.gtu.ac.in/uploads/" + season + "/BE/" + subject_code + ".pdf"
        return paper_url

    def savePaper(self, url, file_name, directory_path):
        website_response = requests.get(url, stream=True)

        if website_response.status_code != 404:
            with open(os.path.join(directory_path, file_name), 'wb') as f:
                for chunk in website_response.iter_content(chunk_size=512):
                    if chunk:
                        f.write(chunk)
        else:
            NewPaper.idx -= 1

    def start(self):
        for code in self.subjectCodes:
            for url in NewPaper.urls:
                website_url = NewPaper.getUrl(self, url, code)
                NewPaper.idx += 1
                file_name = str(NewPaper.idx) + " " + url + "_" + code + ".pdf"
                NewPaper.savePaper(self, website_url, file_name, self.path)
