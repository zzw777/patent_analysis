#coding:utf-8

import os
import json
import getopt
import sys
from datetime import datetime
from.blog import models
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
    report = models.report
    report.time = datetime.now().strftime('%Y-%m-%d')
    report.source_pat_sents = output.source_pat_sents
    report.novelty = output.novelty
    report.creativity = output.novelty
    report.compare_pats = output.compare_pats
    report.novelty = output.novelty


if __name__ == "__main__": main()
