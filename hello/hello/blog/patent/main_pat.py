#coding=utf-8
import os
import json

def get_result(paragraph1, pat_id, language='en'):
	outputfile = open(os.getcwd()+'/blog/patent/output.json', 'r', encoding="utf8")
	output = json.load(outputfile)
	outputfile.close()
	return output

	

if __name__=='__main__':
	paragraph1=''
	pat_id=[]
	language='en'
	print(get_result(paragraph1,pat_id,language))
