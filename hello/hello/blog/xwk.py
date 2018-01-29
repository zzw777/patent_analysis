#coding=UTF-8
import json
import requests
import bs4
import threading
import time
import queue
result_list = []

def get_abs(soup):
    c_abs = ''
    t = soup.find('div', class_='abstract')
    try:
        c_abs = t.get_text()
        if len(c_abs) == 0:
            c_abs = 'F'
    except:
        c_abs = "F"
    return c_abs

def get_cla(soup):
    text = soup.find_all('div', class_='patent-text')
    c_cla = ""
    if len(text) == 3:
        cla = text[1]
        c_cla = cla.get_text()
    if len(c_cla) == 0:
        c_cla = "F"
    return c_cla

def get_des(soup):
    ret = ''
    text = soup.find_all('div', class_='patent-text')
    if len(text) == 3:
        des = text[2].descendants
        temp = ''
        for d in des:
            try:
                s = d.string
                if s != temp and s != None and s != '\n':
                    ret += s
                    #print(s.strip('\n'))
                    temp = s
            except:
                pass
    if len(ret) != 0:
        return ret
    else:
        return "F"

def parser_cn(url):
    abs, cla, dis, raw = 'F', 'F', 'F', 'F'
    try:
        re = requests.get(url, verify=False)
        if re.status_code == 200:
            soup = bs4.BeautifulSoup(re.content.decode('gb2312', 'ignore'), 'html.parser')
            abs = get_abs(soup)
            cla = get_cla(soup)
            dis = get_des(soup)
            if abs == 'F' and cla == 'F' and dis == 'F':
                raw = 'F'
            else:
                raw = soup
        elif re.status_code == 404:
            print('该专利不存在')
    except Exception as e:
        print(e)
    return abs, cla, dis, raw

def get_abs_e(soup):
    try:
        abs = ''
        t = soup.find('div', class_='abstract')
        spanss = t.find_all('span')
        if len(spanss) != 0 and len(spanss)%2 == 0:
            spans = t.find_all('span',recursive=False)
            for k in spans:
                a,b = k.stripped_strings
                abs += b
        else:
            abs = t.get_text()
    except:
        abs = "F"
    if len(abs) == 0:
        abs = 'F'
    return abs

def sum_ord(str_unknom):
    """求出均值，判断是否为英文"""
    str_ord = [ord(i) for i in str_unknom]
    str_ordSum = sum(str_ord)
    str_ord_mean = str_ordSum/len(str_unknom)
    if str_ord_mean <=700:
        flag = 1
    else:
        flag = 0
    return flag

def get_cla_e(soup):
    text = soup.find_all('div', class_='patent-text')
    e_cla = ''
    str_unknow = []
    if len(text) == 3:
        cla = text[1]
        divs = cla.find_all('div',class_='claim-text')
        for div in divs:
            spans = div.find_all('span',recursive=False)
            for span in spans:
                str_temp = [s for s in span.stripped_strings if sum_ord(s)]
                str_unknow.extend(str_temp)
    for s in str_unknow:
        e_cla += s
    if len(e_cla) == 0 :
            e_cla = "F"
    return e_cla

def get_des_e(soup):
    div = soup.find('div',class_='patent-section patent-description-section')
    if div is None:
        des = 'F'
    else:
        spans = div.find_all('span',class_='notranslate')
        des_list = []
        for span in spans:
            des_temp = [s for s in span.stripped_strings if sum_ord(s)]
            des_list.extend(des_temp)
        des = ''.join(s for s in des_list)

    if len(des) != 0:
        return des
    else:
        return 'F'

def parser_eng(url):
    """有时候会抛出 requests.exceptions.ChunkedEncodingError 这个错误 暂时不知道为什么 但是等一下再连接似乎就解决了 权宜之策"""
    abs,cla,des,raw = 'F','F','F','F'
    try:
        re = requests.get(url, verify=False)
        if re.status_code == 200:
            soup = bs4.BeautifulSoup(re.content,'html.parser')
            abs = get_abs_e(soup)
            cla = get_cla_e(soup)
            des = get_des_e(soup)
            raw = soup
        elif re.status_code == 404:
            print('该专利不存在')
    except Exception as e:
        print(e)

    return abs, cla, des,raw

def parser(i,num):
    if num[0:2] == 'US' or num[0:2] == 'DE':  # 美国 德国 的专利 没有中文
        u_en = 'https://www.google.com/patents/{}?cl=en&hl=zh-CN'.format(num)#根据专利号构造地址
        C_RAW = 'F'
        C_ABS = 'F'
        C_DIS = "F"
        C_CLA = 'F'
        E_ABS, E_CLA, E_DIS, E_RAW = parser_eng(u_en)
    else:
        u_en = 'https://www.google.com/patents/{}?cl=en&hl=zh-CN'.format(num)
        u_cn = 'https://www.google.com/patents/{}?cl=zh&hl=zh-CN'.format(num)
        C_ABS, C_CLA, C_DIS, C_RAW = parser_cn(u_cn)
        E_ABS, E_CLA, E_DIS, E_RAW = parser_eng(u_en)

    if E_RAW != 'F':
        title = E_RAW.find('span', class_='patent-title').get_text()
        chin_index = []
        for (index, s) in enumerate(title):
            if ord(s) > 122:
                chin_index.append(index)
        if len(chin_index) != 0:
            s = chin_index[0]
            e = chin_index[-1]
            title = title.replace(title[s:e + 1], '')
    else:
        title = 'F'
    di = {'num':num,'C_ABS': C_ABS, 'C_CLA': C_CLA,'C_DIS':C_DIS,'E_ABS':E_ABS,'E_CLA':E_CLA,'E_DIS':E_DIS,'title':title}
    zzw =json.dumps(di,ensure_ascii=False)
    result_list.append((i,zzw))

def zzw(num_list):
    # num_list = ['CN104501944A', 'CN204330128U', 'US20130100097A1', 'CN103200286A', 'CN103890645A', 'US20120019152A1', 'US20140104436A1', 'US9332616B1', 'US8686981B2', 'US9495915B1']
    num_list_index  =[(i,num) for (i,num) in enumerate(num_list)]

    threads = []

    for tup in num_list_index:
        thread = threading.Thread(target=parser,args=(tup[0],tup[1]))
        threads.append(thread)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()

    result_list.sort()
    result = [t[1] for t in result_list]
    result = json.dumps(result,ensure_ascii=False)
    return result


