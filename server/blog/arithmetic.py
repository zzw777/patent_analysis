#coding:utf-8

import os
import urllib
import json
import bs4
import sys
from .import models
import datetime
import urllib
import getopt

from bs4 import BeautifulSoup
from mongoengine import connect

def transition_flag(output):
	compare_pats=output['compare_pats']
	language=output['language_flag']
	flag=0
	for pat in compare_pats:
		if pat['language_flag']!=language:
			flag=1
			break
	return flag

def get_result(paragraph1, pat_id, language='en'):
	outputfile = open(os.getcwd()+'/output.json', 'r', encoding="utf8")
	output = json.load(outputfile)
	outputfile.close()
	return output

def num_change (num_all,num_front):
    if num_all == num_front:
        string_list_fornt = []
        for n in range(num_all):
            string_list_fornt.append(str(n+1))
            string_list_fornt.append('、')
        string_list_fornt.pop()
        string_fornt = ''.join(s for s in string_list_fornt)

        string_behind = '0'

    else:
        string_list_fornt = []
        for n in range(num_all - num_front -1 ):
            string_list_fornt.append(str(n+1))
            string_list_fornt.append('、')
        string_list_fornt.pop()
        string_fornt = ''.join(s for s in string_list_fornt)

        string_list_behind = []
        for n in range(num_front,num_all):
            string_list_behind.append(str(n+1))
            string_list_behind.append('、')
        string_list_behind.pop()
        string_behind = ''.join(s for s in string_list_behind)

    return string_fornt,string_behind

def dec_change(output):
    result = ""
    for pat in output:
        num = pat[0]['pat_id']
        sim_rate = pat[0]['percent']
        sim_baifen = '%.2f%%' % (sim_rate * 100)
        result += str(num) + '('+str(sim_baifen) + ')' + ' '
    return result

def font(output):
    source_pat_sents = output['source_pat_sents']
    detail = output['conclusion']['detail']
    result = []
    for d in detail:
        reveal_pats = ''.join(str(i)+' ' for i in d['reveal_pats'])
        sim_pats = ''.join(str(i) +' ' for i in d['sim_pats'])
        result.append((reveal_pats,sim_pats,source_pat_sents[d['sent_id']]))
    return result


def compare_pats_search(output,pat_id,sim_threshold):
	pat_sents=[]
	for pat in output['compare_pats']:
		if pat['pat_id']==pat_id:
			pat_sents=pat['pat_sentences']
			sent_CLA_flag=pat['sent_CLA_flag']
			sents_sim=pat['sents_sim']
			language_flag=pat['language_flag']
			break
	if pat_sents==[]:
		print('没有找到专利'+pat_id)
		return 'ERROR'
	compare_sents=[]
	if language_flag=='zh':
		source_pat_sents=output['source_pat_sents_zh']
	else:
		source_pat_sents=output['source_pat_sents_en']
	for i in range(len(pat_sents)):
		max_sim_value=0
		for sent_sim in sents_sim:
			if sent_sim['compare_sent_id']==i:
				#print(sent_sim['compare_sent_id'],sent_sim['AverageSim'],sent_sim['source_sent_id'])
				if sent_sim['AverageSim']>sim_threshold and sent_sim['AverageSim']>max_sim_value:
					max_sim_value=sent_sim['AverageSim']
					source_sent_id=sent_sim['source_sent_id']
		if max_sim_value!=0:
			max_sim_value=round(max_sim_value*100, 2)
			compare_sents.append((str(i+1),pat_sents[i],str(max_sim_value)+'%',str(source_sent_id+1),source_pat_sents[source_sent_id]))
		else:
			compare_sents.append((str(i+1),pat_sents[i],'','',''))
	abs_list=compare_sents[:sent_CLA_flag]
	cla_list=compare_sents[sent_CLA_flag:]
	return abs_list,cla_list



def pat_search(output):
    pat_id_list = []
    for compare_pats in output['compare_pats']:
        pat_id_list.append(compare_pats['pat_id'])
    return (pat_id_list)

def main():
    try:
        options, args,sec_id = getopt.getopt(sys.argv[1:], "w:l:i", ["word=", "list=", "id="])
    except getopt.GetoptError:
        sys.exit()

    word = ''
    list = ''
    sec_id = ''
    for option, value in options:
        if option in ("-w", "--word"):
            word = value
            print(word)
        if option in ("-l", "--list"):
            list = value.split(";")
            print(list)
        if option in ("-i", "--id"):
            sec_id = value
            print(sec_id)

    output = get_result(word, list, 'en')

    mongodb = connect("patent")


    monreport = models.reports(id = sec_id)
    monreport.source_pat_sents = {output['source_pat_sents']}
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
    monreport.time = nowTime
    patent_list = pat_search(output)
    monreport.compare_pats = patent_list

    File = open('./templates/blog/report.htm', encoding='UTF-8')
    soup = bs4.BeautifulSoup(File.read(), 'html.parser')

    flag = transition_flag(output)
    if flag == '1':
        source_pat_sents_zh = soup.find('p',{'name':"source_pat_sents_zh"})
        source_pat_sents_en = soup.find('p', {'name': "source_pat_sents_en"})
        source_pat_sent_en = ''.join(s for s in output['source_pat_sents_en'])
        source_pat_sent_zh = ''.join(s for s in output['source_pat_sents_zh'])
        source_pat_sents_zh.string = str(source_pat_sent_zh)
        source_pat_sents_en.string = str(source_pat_sent_en)
    else:
        source_pat_sents_zh = soup.find('p', {'name': "source_pat_sents_zh"})
        source_pat_sent_zh = ''.join(s for s in output['source_pat_sents'])
        source_pat_sents_zh.string = str(source_pat_sent_zh)

    inno = output['conclusion']['innovative']
    if inno == '无':
        innovative = soup.find('button',{'name':"InnovationConclusion"})
        innovative.string = str(inno)
        innovative['class']='btn btn-outline-danger'

    elif inno == '有':
        innovative = soup.find('button', {'name': "InnovationConclusion"})
        innovative.string = str(inno)
        innovative['class'] = 'btn btn-danger'

    nov = output['conclusion']['novelty']
    novelty = soup.find('button', {'name': "NoveltyConclusion"})
    novelty.string = str(nov)
    if nov == '无':
        novelty['class'] = 'btn btn-outline-danger'

    elif nov == '有':
        novelty['class'] = 'btn btn-danger'

    cre = output['conclusion']['creativity']

    button1 = soup.find('button', {'name': "button1"})
    button2 = soup.find('button', {'name': "button2"})
    button3 = soup.find('button', {'name': "button3"})
    button2.string = str(cre)
    if cre == '无（弱）':
        button1['class'] = 'btn btn-danger'
        button2['class'] = 'btn btn-outline-danger'
        button3['class'] = 'btn btn-outline-danger'
    elif cre == '有（中）':
        button1['class'] = 'btn btn-danger'
        button2['class'] = 'btn btn-danger'
        button3['class'] = 'btn btn-outline-danger'
    elif cre == '有（强）':
        button1['class'] = 'btn btn-danger'
        button2['class'] = 'btn btn-danger'
        button3['class'] = 'btn btn-danger'

    TotalTechnicalFeatureNum = soup.find('font', {'name': "TotalTechnicalFeatureNum"})
    TotalTechnicalFeatureNum.string = str(len(output['source_pat_sents']))

    for patent in output['conclusion']['detail']:
        front = patent['sent_id']
    (qian,hou) = num_change(len(output['source_pat_sents']),front+1)
    RevealedTechnicalFeature = soup.find('font', {'name': "RevealedTechnicalFeature"})
    RevealedTechnicalFeature.string = str(qian)

    RevealedTechnicalFeatureNum = soup.find('font', {'name': "RevealedTechnicalFeatureNum"})
    RevealedTechnicalFeatureNum.string = str(len(qian.split('、')))

    UnrevealedTechnicalFeature = soup.find('font', {'name': "UnrevealedTechnicalFeature"})
    UnrevealedTechnicalFeature.string = str(hou)

    UnrevealedTechnicalFeatureNum = soup.find('font', {'name': "UnrevealedTechnicalFeatureNum"})
    if hou == '0':
        UnrevealedTechnicalFeatureNum.string = str('0')
    if hou != '0':
        UnrevealedTechnicalFeatureNum.string = str(hou)

    RevealedRatio = soup.find('font', {'name': "RevealedRatio"})
    reveal_rate = output['conclusion']['reveal_rate']
    rev_baifen = '%.2f%%' % (reveal_rate * 100)
    RevealedRatio.string = str(rev_baifen)

    MinimumRevealedPatNum = soup.find('font', {'name': "MinimumRevealedPatNum"})
    MinimumRevealedPatNum.string = str(output['conclusion']['min_reveal_pat_num'])

    rev_details = dec_change(output['conclusion']['pat_groups_novelty'])
    RevealedDetails = soup.find('font', {'name': "RevealedDetails"})
    RevealedDetails.string = str(rev_details)

    HighSimTechnicalFeatureRatio = soup.find('font', {'name': "HighSimTechnicalFeatureRatio"})
    sim_rate = output['conclusion']['sim_rate']
    sim_baifen = '%.2f%%' % (sim_rate * 100)
    HighSimTechnicalFeatureRatio.string = str(sim_baifen)

    MinimumHighSimPatNum = soup.find('font', {'name': "MinimumHighSimPatNum"})
    MinimumHighSimPatNum.string = str(output['conclusion']['min_sim_pats_num'])

    HighSimDetails = soup.find('font', {'name': "HighSimDetails"})
    high_details = dec_change(output['conclusion']['pat_groups_creativity'])
    HighSimDetails.string = str(high_details)

    InnovationConclusion = soup.find('font', {'name': "InnovationConclusion"})
    InnovationConclusion.string = str(inno)

    CreativityConclusion = soup.find('font', {'name': "CreativityConclusion"})
    CreativityConclusion.string = str(cre)

    font_result = font(output)
    ComparisonDetails = soup.find('ul', {'name': "ComparisonDetails"})
    for sen in font_result:
        (front, middle, after) = sen
        if front == "" and  middle == "":
            new_li_tag = soup.new_tag("li")
            new_li_tag.append(str('技术特征“'+after+'”未被对比专利揭示'))
            ComparisonDetails.append(new_li_tag)
        else:
            new_li_tag = soup.new_tag("li")
            new_li_tag.append(str('技术特征“' + after + '”被对比专利中公开号为'+front+'的专利揭示，且与'+middle+'的技术特征相似度较高；'))
            ComparisonDetails.append(new_li_tag)

    pat_list = pat_search(output)
    for index in pat_list:
        PatComparison = soup.find('div', {'name': "PatComparison"})
        new_div_tag = soup.new_tag("div")
        new_font_tag=soup.new_tag("font")
        new_div_tag.attrs = {'class':"container",'style':"text-align: center"}
        new_font_tag.append('专利'+index+'与该创新性描述的比对报告')
        new_font_tag.attrs = {'size': '6'}
        new_div_tag.append(new_font_tag)

        new_table_tag = soup.new_tag("table")
        new_table_tag.attrs = {'class':"bordered"}
        new_tbody_tag = soup.new_tag("tbody")

        new_tr_tag1 = soup.new_tag("tr")

        new_th_tag = soup.new_tag("th")
        new_th_tag.attrs = {'style': 'vertical-align: middle;width:4%'}
        new_th_tag.append('序号')
        new_tr_tag1.append(new_th_tag)

        new_th_tag = soup.new_tag("th")
        new_th_tag.attrs = {'style': 'vertical-align: middle;width:40%'}
        new_th_tag.append('专利'+index)
        new_tr_tag1.append(new_th_tag)

        new_th_tag = soup.new_tag("th")
        new_th_tag.attrs = {'style': 'vertical-align: middle;width:12%'}
        new_th_tag.append('技术特征相似度')
        new_tr_tag1.append(new_th_tag)

        new_th_tag = soup.new_tag("th")
        new_th_tag.attrs = {'style': 'vertical-align: middle;width:4%'}
        new_th_tag.append('序号')
        new_tr_tag1.append(new_th_tag)

        new_th_tag = soup.new_tag("th")
        new_th_tag.attrs = {'style': 'vertical-align: middle;width:40%'}
        new_th_tag.append('该创新性描述')
        new_tr_tag1.append(new_th_tag)
        new_tbody_tag.append(new_tr_tag1)

        new_tr_tag2 = soup.new_tag("tr")

        new_td_tag = soup.new_tag("td")
        new_tr_tag2.append(new_td_tag)

        new_td_tag = soup.new_tag("td")
        new_td_tag.attrs = {'style': "text-align:center"}
        new_td_tag.append('摘要')
        new_tr_tag2.append(new_td_tag)

        new_td_tag = soup.new_tag("td")
        new_tr_tag2.append(new_td_tag)
        new_tr_tag2.append(new_td_tag)
        new_tr_tag2.append(new_td_tag)

        new_td_tag = soup.new_tag("td")
        new_tr_tag2.append(new_td_tag)
        new_tr_tag2.append(new_td_tag)
        new_tr_tag2.append(new_td_tag)

        new_td_tag = soup.new_tag("td")
        new_tr_tag2.append(new_td_tag)
        new_tr_tag2.append(new_td_tag)
        new_tr_tag2.append(new_td_tag)

        new_tbody_tag.append(new_tr_tag2)

        (abs_list,cla_list) =  compare_pats_search(output,index,0.5)

        for a in abs_list:
            if a[2] != '':
                new_tr_tag3 = soup.new_tag("tr")

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(a[0])
                new_tr_tag3.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class': 'highlight'}
                new_td_tag.append(a[1])
                new_tr_tag3.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(a[2])
                new_tr_tag3.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(a[3])
                new_tr_tag3.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class': 'highlight'}
                new_td_tag.append(a[4])
                new_tr_tag3.append(new_td_tag)

                new_tbody_tag.append(new_tr_tag3)

            else:
                new_tr_tag4 = soup.new_tag("tr")

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(a[0])
                new_tr_tag4.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.append(a[1])
                new_tr_tag4.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_tr_tag4.append(a[2])
                new_tr_tag4.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(a[3])
                new_tr_tag4.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.append(a[4])
                new_tr_tag4.append(new_td_tag)

                new_tbody_tag.append(new_tr_tag4)
        new_tr_tag5 = soup.new_tag("tr")

        new_td_tag = soup.new_tag("td")
        new_tr_tag5.append(new_td_tag)

        new_td_tag = soup.new_tag("td")
        new_td_tag.attrs = {'style': 'text-align:center'}
        new_td_tag.append('权利要求')
        new_tr_tag5.append(new_td_tag)

        new_td_tag = soup.new_tag("td")
        new_tr_tag5.append(new_td_tag)
        new_tr_tag5.append(new_td_tag)
        new_tr_tag5.append(new_td_tag)

        new_td_tag = soup.new_tag("td")
        new_tr_tag5.append(new_td_tag)
        new_tr_tag5.append(new_td_tag)
        new_tr_tag5.append(new_td_tag)

        new_td_tag = soup.new_tag("td")
        new_tr_tag5.append(new_td_tag)
        new_tr_tag5.append(new_td_tag)
        new_tr_tag5.append(new_td_tag)

        new_tbody_tag.append(new_tr_tag5)
        for b in cla_list:
            if b[2] != '':
                new_tr_tag6 = soup.new_tag("tr")
                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(b[0])
                new_tr_tag6.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class': 'highlight'}
                new_td_tag.append(b[1])
                new_tr_tag6.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(b[2])
                new_tr_tag6.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(b[3])
                new_tr_tag6.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class': 'highlight'}
                new_td_tag.append(b[4])
                new_tr_tag6.append(new_td_tag)

                new_tbody_tag.append(new_tr_tag6)
            else:
                new_tr_tag7 = soup.new_tag("tr")

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(b[0])
                new_tr_tag7.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.append(b[1])
                new_tr_tag7.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(b[2])
                new_tr_tag7.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.attrs = {'class':'vt'}
                new_td_tag.append(b[3])
                new_tr_tag7.append(new_td_tag)

                new_td_tag = soup.new_tag("td")
                new_td_tag.append(b[4])
                new_tr_tag7.append(new_td_tag)

                new_tbody_tag.append(new_tr_tag7)
        new_table_tag.append(new_div_tag)
        new_table_tag.append(new_tbody_tag)
        PatComparison.append(new_table_tag)
    fin_html = soup.prettify()
    with open('report_html.html','wb') as f:
        f.write(fin_html.encode('utf-8'))
        re_html = open('report_html.html','rb')
        monreport.report_html.put(re_html,content_type='html')
    monreport.save()
    mongodb.close()




if __name__ == "__main__": main()



