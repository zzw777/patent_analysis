#coding:utf-8

import json
import os
import re
import sys
from django.http import HttpResponse
from django.shortcuts import render
from mongoengine import connect
from . import models
from . import xwk
from bson.objectid import ObjectId
import datetime
import __init__
from mongoengine import connect
import time


def index1(request):
    return render(request, 'blog/index1.html')

def output1(request):
    return render(request, 'blog/output1.html')


def input1(request):

    return render(request, 'blog/input1.html')

def acquire(request):
    try:
        if request.method == 'POST':
            metadata = request.POST.get('list')
            if len(metadata) == 0:
                data = list()
            else:
                metadata = xwk.parser_list(metadata.split(";"))
                print(metadata)
                data = list()
                for datum in metadata:
                    data.append([
                        datum["patent_id"] if datum["patent_id"] != "F" else "无",
                        datum["patent_no"] if datum["patent_no"] != "F" else "无",
                        datum["patent_title"] if datum["patent_title"] != "F" else "无",
                        datum["abstract"] if datum["abstract"] != "F" else "无",
                        datum["page_url"] if datum["page_url"] != "F" else "无",
                        datum["download_url"] if datum["download_url"] != "F" else "无"
                    ])

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
            pat = request.POST.get('list')
            pat_list = request.POST.get('list').split(";")

            mongodb = connect("patent")

            nowTime = datetime.datetime.now()
            monreport = models.reports()
            monreport._id = nowTime.strftime('%Y%m%d%H%M%S%f')
            monreport.status = "进行中"
            monreport.source_pat_sents = [" "]
            monreport.compare_pats = pat_list
            
            monreport.time = nowTime.strftime('%Y-%m-%d')
            with open('./templates/blog/report.htm','rb') as f:
                monreport.report_html.put(f,content_type='html')
                monreport.report_pdf.put(f,content_type='html')
            monreport.save()
            mongodb.close()

            if len(pat_list) != 0 and len(pat_list) != 0:
                data = {'msg': '任务已建立，正在分析中。。。'}
                os.system("python ./blog/arithmetic.py -w " + sorc_word + " -l " + pat + " -s " + monreport._id)

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
        data = list()
        with connect("patent") as mongodb:
            for datum in models.reports.objects():
                data.append([str(datum.id),datum.time,datum.status,datum.source_pat_sents,datum.status])
        mongodb.close()

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
