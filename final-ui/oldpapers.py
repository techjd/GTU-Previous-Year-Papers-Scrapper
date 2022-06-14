import requests
from bs4 import BeautifulSoup
import os


class OldPaper:
    idx = 0

    def __init__(self, path, subject_codes, subject_name):
        self.path = path
        self.subjectCodes = subject_codes
        self.subject_name = subject_name

    urls = [
        'http://old.gtu.ac.in/GTU_Papers/Summer_Exam_2017_BE.htm',
        'http://old.gtu.ac.in/GTU_Papers/Winter_Exam_2016_BE.htm',
        'http://old.gtu.ac.in/GTU_Papers/Summer_Exam_2016_BE.htm'
        'http://old.gtu.ac.in/GTU_Papers/Winter_Exam_2015_BE.htm',
        'http://old.gtu.ac.in/GTU_Papers/Summer_Exam_2015_BE.htm',
        'http://old.gtu.ac.in/GTU_Papers/Winter_Exam_2014_BE.htm',
        'http://old.gtu.ac.in/GTU_Papers/Summer_Exam_2014_BE.htm',
        'http://old.gtu.ac.in/GTU_Papers/Winter_Exam_2013_BE.htm'
        'http://old.gtu.ac.in/GTU_Papers/Summer_Exam_2013_BE.htm',
        'http://old.gtu.ac.in/GTU_Papers/Winter_Exam_2012_BE.htm'
        'http://old.gtu.ac.in/GTU_Papers/Summmer_Exam_2012_BE.htm'
        'http://old.gtu.ac.in/GTU_Papers/NovDec11JanFeb12_BE.htm'
    ]

    def savePaper(self, url, file_name, directory_path):
        website_response = requests.get(url, stream=True)

        if website_response.status_code != 404:
            with open(os.path.join(directory_path, file_name), 'wb') as f:
                for chunk in website_response.iter_content(chunk_size=512):
                    if chunk:
                        f.write(chunk)

    def process(self, index, website_link, name):
        final_link = "http://old.gtu.ac.in/GTU_Papers/" + website_link['href']
        middle_file_name = website_link.text.strip()
        file_name = str(index) + " " + name + " " + middle_file_name + ".zip"
        OldPaper.savePaper(self, final_link, file_name, self.path)

    def start(self):
        for code in self.subjectCodes:
            for url in OldPaper.urls:
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'lxml')
                for link in soup.find_all('a', href=True):
                    if link.text.strip() == code:
                        OldPaper.idx += 1
                        OldPaper.process(self, OldPaper.idx, link, self.subject_name)
