#coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .import xwk
from .patent import main_pat
import json
import re
from .import models
import requests
import os

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
            output = xwk.zzw(list)
            # output1 = json.loads(xwk.zzw(list))
            # for patent in output1:
            #     num = json.loads(patent)['num']
            #     entry = models.xwkModel
                # print(num)
                # entry.title = json.loads(patent)['C_ABS']
                # entry.C_ABS = json.loads(patent)['C_ABS']
                # entry.C_CLA = json.loads(patent)['C_CLA']
                # entry.C_DIS = json.loads(patent)['C_DIS']
                # entry.E_ABS = json.loads(patent)['E_ABS']
                # entry.E_CLA = json.loads(patent)['E_CLA']
                # entry.E_DIS = json.loads(patent)['E_DIS']
                # entry.save()
                # print(entry.num)
                # print(entry.title)
            data = [
                ["1","CN103322765A","本发明公开了一种具有物品本发明公开了一种具有物品本发明公开了一种具有物品本发明公开了一种具有物品本发明公开了一种具有物品","url","url"],
                ["2","CN103322765A","本发明公开了一种具有物品","url","url"],
                ["3","CN103322765A","本发明公开了一种具有物品","url","url"],
                ["5","CN103322765A","本发明公开了一种具有物品","url","url"]
            ]

            response = HttpResponse(json.dumps(data), content_type="application/json")
            response['Access-Control-Allow-Origin'] = '*'
            # response = HttpResponse((output), content_type='application/json')
            return response
    except Exception as e:
        print(e)
        response = HttpResponse(json.dumps({"msg": e}), content_type='application/json')
        response['Access-Control-Allow-Origin'] = '*'
        return response


def work(request):
    try:
        if request.method == "POST":
            data1 = request.POST.get('word')
            data2 = request.POST.get('list')
            print(data1)
            print(data2)
            data2 = re.split(',|，|\n| ', data2)
            data2 = [l for l in data2 if len(l) != 0]
            if len(data1) != 0 and len(data2) != 0:
            # if data1[0] >= u'\u4e00' and data1[0]<=u'\u9fa5':
                output = main_pat.get_result(data1, data2, 'zh')
                data = {'output': output, 'msg': 'OK'}
            # else:
            #     output = main_pat.get_result(data1, data2, 'en')
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
        data = [
            ["2018-01-28","进行中","本发明公开了一种具有物品","url"],
            ["2018-01-28","已完成","本发明公开了一种具有物品","url"],
            ["2018-01-28","已完成","本发明公开了一种具有物品","url"],
            ["2018-01-28","已完成","本发明公开了一种具有物品","url"]
        ]

        response = HttpResponse(json.dumps(data), content_type="application/json")
        response['Access-Control-Allow-Origin'] = '*'
        return response

    except Exception as e:
        print(e)
        response = HttpResponse(json.dumps({"msg": e}), content_type='application/json')
        response['Access-Control-Allow-Origin'] = '*'
        return response

# def graph(request):
#     ctx = {}
#     form = " "
#     if request.method == "POST":
#         data = request.POST['q']
#         print(os.getcwd())
#         print ("it worked")
#
#     return render(request, 'blog/graph.html', context={'form':form})

def page1(request):
    return render(request, 'blog/page1.html')

def page2(request):
    return render(request, 'blog/page2.html')
#---------------------------------------------
