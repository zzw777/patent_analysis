#coding:utf-8

import json
import os
import re
from django.http import HttpResponse
from django.shortcuts import render
from .import models
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
                ["1","CN103322765A","本发明公开了一种具有物品本发明公开了一种具有物品本发明公开了一种具有物品本发明公开了一种具有物品本发明公开了一种具有物品","url","url"],
                ["2","CN103322765A","本发明公开了一种具有物品","url","url"],
                ["3","CN103322765A","本发明公开了一种具有物品","url","url"],
                ["5","CN103322765A","本发明公开了一种具有物品","url","url"]
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
        report = models.reports(name='123')
        abc = open(os.getcwd() + '/blog/static/123.pdf', 'rb')
        report.report_pdf.put(abc, content_type='pdf')
        report.save()
        if request.method == "POST":
            record_id = request.POST.get('record_id')
            print(record_id)
            task = request.POST.get('task')
            print(task)
            number = models.reports.objects(name='123').first()
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
            if len(pat_list) != 0 and len(pat_list) != 0:
                data = {'msg': '任务已建立，正在分析中。。。'}
                # os.system("cd D:\Github\patent_analysis\hello\hello")
                print(os.system("cd"))
                # os.system("python arithmetic.py"+" -w" + sorc_word + " -l" + pat_list)
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
        report = models.report()
        id = report.id
        time = report.time
        abs = report.source_pat_sents
        url = report.report_html
        if report.report_pdf != "":
            statement = '已完成'
        else:
            statement = '进行中'
        data = [
            [id, time, statement, abs, url],
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
