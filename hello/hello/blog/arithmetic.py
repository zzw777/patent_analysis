#coding:utf-8

import os
import json
import getopt
import sys
# sys.path.append(os.getcwd() + '\\blog')
# print(sys.path)
from .import models
from datetime import datetime
from bs4 import BeautifulSoup

def get_result(paragraph1, pat_id, language='en'):
	outputfile = open(os.getcwd()+'/blog/patent/output.json', 'r', encoding="utf8")
	output = json.load(outputfile)
	outputfile.close()
	return output


if __name__ == '__main__':
    paragraph1 = ''
    pat_id = []
    language = 'en'
    print(get_result(paragraph1, pat_id, language))

def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], "w:l:h", ["word=", "list=", "help"])
    except getopt.GetoptError:
        sys.exit()

    word = ''
    list = ''
    for option, value in options:
        if option in ("-w", "--word"):
            word = value
            print(word)
        if option in ("-l", "--list"):
            list = value.split(";")
            type(list)
        if option in ("-h", "--help"):
            print("help")

    output = get_result(word, list, 'en')
    # with open(os.getcwd() + '/templates/report.htm', "r") as re:
    #     soup = BeautifulSoup(re, "html")
    #     source_pat_sents = soup.find(name="source_pat_sents")
    #     source_pat_sents['value'] = output.source_pat_sents
    #     InnovationConclusion = soup.find_all(name="InnovationConclusion")
    #     InnovationConclusion['value'] = output.innovative
    #     NoveltyConclusion = soup.find_all(name="InnovationConclusion")
    #     NoveltyConclusion['value'] = output.novelty
    #     CreativityConclusion = soup.find_all(name="CreativityConclusion")
    #     CreativityConclusion['value'] = output.creativity
    report = models.reports
    report.source_pat_sents = {'sour': output.source_pat_sents, 'zh': output.source_pat_sents_zh,'en': output.source_pat_sents_en}
    report.time = datetime.now().strftime('%Y-%m-%d')
    report.novelty = output.novelty
    report.innovative = output.innovative
    report.creativity = output.novelty
    report.compare_pats = output.compare_pats
    # abc = open(os.getcwd() + '/hello/templates/report.htm', 'rb')
    # report.report_html.put(abc, content_type='html')
    report.save()
    print(report.time)
    print(report.novelty)
    print(report.innovative)


if __name__ == "__main__":main()
