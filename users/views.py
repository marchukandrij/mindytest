from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import users.database as database
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def extract_post_data(request):
    string = request.body.decode("utf-8")
    return json.loads(string)

def index(request):
    db_ok = database.check_connection()
    if db_ok:
        database.users_create_table()
        # because Jinja breaking Vue markup
        html = open('users/templates/index.html','r').read()
        return HttpResponse(html)
    else:
        return HttpResponse(render(request, 'nosql.html'))

def read(request):
    data = database.users_read_all()
    return JsonResponse(data, safe=False)

@csrf_exempt
def update(request):
    data = extract_post_data(request)
    date_field = datetime.datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
    database.users_update(data['id'], data['login'], data['name'], data['surname'], date_field)
    return read(request)

@csrf_exempt
def delete(request):
    data = extract_post_data(request)
    database.users_delete(data['id'])
    return read(request)

@csrf_exempt
def create(request):
    data = extract_post_data(request)
    date_field = datetime.datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
    database.users_create(data['login'], data['name'], data['surname'], date_field)
    return read(request)