#coding:utf-8

import json
import os
import re
import time

from django.http import HttpResponse
from django.shortcuts import render

from . import models
from . import xwk


def index1(request):
    return render(request, 'blog/index1.html')

def output1(request):
    return render(request, 'blog/output1.html')


def input1(request):

    return render(request, 'blog/input1.html')

def acquire(request):
    try:
        if request.method == 'POST':
            data1 = request.POST.get('list')
            print(data1)
            list = re.split(',|，|\n| ', data1)
            list = [l for l in list if len(l) != 0]
            data = [
                ["1","CN103322765A","一种发送物品信息的方法，其特征在于，所述方法包括：获取储物箱的储物箱信息；根据所述储物箱信息，获取所述储物箱储藏的物品的物品信息，所述物品的物品信息至少包括所述物品的物品描述信息；发送所述物品的物品信息给用户对应的移动终端。","url","url"],
                ["2","CN103322765A","一种发送物品信息的方法，其特征在于，所述方法包括：获取储物箱的储物箱信息；根据所述储物箱信息，获取所述储物箱储藏的物品的物品信息，所述物品的物品信息至少包括所述物品的物品描述信息；发送所述物品的物品信息给用户对应的移动终端。","url","url"],
                ["3","CN103322765A","一种发送物品信息的方法，其特征在于，所述方法包括：获取储物箱的储物箱信息；根据所述储物箱信息，获取所述储物箱储藏的物品的物品信息，所述物品的物品信息至少包括所述物品的物品描述信息；发送所述物品的物品信息给用户对应的移动终端。","url","url"],
                ["5","CN103322765A","一种发送物品信息的方法，其特征在于，所述方法包括：获取储物箱的储物箱信息；根据所述储物箱信息，获取所述储物箱储藏的物品的物品信息，所述物品的物品信息至少包括所述物品的物品描述信息；发送所述物品的物品信息给用户对应的移动终端。","url","url"]
            ]

            response = HttpResponse(json.dumps(data), content_type="application/json")
            response['Access-Control-Allow-Origin'] = '*'
            return response
    except Exception as e:
        print(e)
        response = HttpResponse(json.dumps({"msg": e}), content_type='application/json')
        response['Access-Control-Allow-Origin'] = '*'
        return response


def dl_report(request):
    try:
        report = models.report(name='123')
        abc = open(os.getcwd() + '/blog/static/123.pdf', 'rb')
        report.report_pdf.put(abc, content_type='pdf')
        report.save()
        if request.method == "POST":
            record_id = request.POST.get('record_id')
            print(record_id)
            task = request.POST.get('task')
            print(task)
            number = models.report.objects(name='123').first()
            if (task == 'download'):
                output = number.report_pdf.read()
                content_type = number.report_pdf.content_type
                response = HttpResponse(output, content_type)
                return response
            elif(task == 'view'):
                output = number.report_html.read()
                content_type = number.report_html.content_type
                response = HttpResponse(output, content_type)
                return response
    except Exception as e:
        print(e)
        response = HttpResponse(json.dumps({"msg": e}), content_type='application/json')
        response['Access-Control-Allow-Origin'] = '*'
        return response

def work(request):
    try:
        if request.method == "POST":
            sorc_word = request.POST.get('word')
            pat_list = request.POST.get('list')
            print(sorc_word )
            print(pat_list)
            # pat_list = re.split(',|，|\n| ', pat_list)
            # pat_list = [l for l in pat_list if len(l) != 0]
            # list = ',|，|\n| '.join(pat_list)
            print(list)
            if len(pat_list) != 0 and len(pat_list) != 0:
                data = {'msg': '任务已建立，正在分析中。。。'}
                os.system("python arithmetic.py"+" -w" + sorc_word + " -l" + pat_list)
                response = HttpResponse(json.dumps(data), content_type="application/json")
                response['Access-Control-Allow-Origin'] = '*'
                return response
            else:
                data = {'msg': '您输入的数据有误'}
                response = HttpResponse(json.dumps(data), content_type="application/json")
                response['Access-Control-Allow-Origin'] = '*'
                return response
    except Exception as e:
        print(e)
        response = HttpResponse(json.dumps({"msg": e}), content_type='application/json')
        response['Access-Control-Allow-Origin'] = '*'
        return response

def acquire1(request):
    return render(request, 'blog/acquire1.html')


def download1(request):
    return render(request, 'blog/download1.html')

def tasks(request):
    try:
        report = models.report(id='')
        time = report.time
        abs = report.source_pat_sents
        data = [
            ["1","2018-01-28","进行中","一种发送物品信息的方法，其特征在于，所述方法包括：获取储物箱的储物箱信息；根据所述储物箱信息，获取所述储物箱储藏的物品的物品信息，所述物品的物品信息至少包括所述物品的物品描述信息；发送所述物品的物品信息给用户对应的移动终端。","url"],
            ["2","2018-01-28","已完成","一种发送物品信息的方法，其特征在于，所述方法包括：获取储物箱的储物箱信息；根据所述储物箱信息，获取所述储物箱储藏的物品的物品信息，所述物品的物品信息至少包括所述物品的物品描述信息；发送所述物品的物品信息给用户对应的移动终端。","url"],
            ["3","2018-01-28","已完成","一种发送物品信息的方法，其特征在于，所述方法包括：获取储物箱的储物箱信息；根据所述储物箱信息，获取所述储物箱储藏的物品的物品信息，所述物品的物品信息至少包括所述物品的物品描述信息；发送所述物品的物品信息给用户对应的移动终端。","url"],
            ["4","2018-01-28","已完成","一种发送物品信息的方法，其特征在于，所述方法包括：获取储物箱的储物箱信息；根据所述储物箱信息，获取所述储物箱储藏的物品的物品信息，所述物品的物品信息至少包括所述物品的物品描述信息；发送所述物品的物品信息给用户对应的移动终端。","url"]
        ]

        response = HttpResponse(json.dumps(data), content_type="application/json")
        response['Access-Control-Allow-Origin'] = '*'
        return response

    except Exception as e:
        print(e)
        response = HttpResponse(json.dumps({"msg": e}), content_type='application/json')
        response['Access-Control-Allow-Origin'] = '*'
        return response

def page1(request):
    return render(request, 'blog/page1.html')

def page2(request):
    return render(request, 'blog/page2.html')
#---------------------------------------------
