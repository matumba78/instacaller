from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from collections import OrderedDict

from instacaller.models import UserContactDB,UserDB
# Create your views here.

class RegisterUserView(View):
    def post(self,request):
        data = request.POST
        phone = data['phone_number']
        if UserDB.objects.filter(phone_number=phone,is_registered=True):
            return HttpResponse("phone must be unique")
        name = data['name']
        email = data['email']
        user_data = UserDB(name=name, phone_number=phone, email=email,is_registered=True)
        user_data.save()
        return HttpResponse('registered successfully', status=200)

class SpamUser(View):
    def post(self,request):
        data = request.POST
        phone = data['phone']
        user_data = UserDB.objects.filter(phone_number=phone)
        if user_data:
            user_data[0].is_spam = True
            user_data[0].save()
            return HttpResponse("phone already marked as spam",status=201)
        else:
            new_phone_data = UserDB(phone_number=phone,is_spam=True)
            new_phone_data.save()
            return HttpResponse("phone marked as spam")

class SearchByName(View):
    def get(self,request,search_query):
        response_data = OrderedDict()
        _list =[]
        exact_match = UserDB.objects.filter(name__iexact=search_query)
        if exact_match:
            for object in exact_match:
                response_data = {
                    "name": object.name,
                    "phone_number": object.phone_number,
                    "is_spam": object.is_spam
                }
                _list.append(response_data)
        exact_match = exact_match.values('id')
        partial_match = UserDB.objects.filter(name__icontains=search_query).exclude(id__in=exact_match)
        if partial_match:
            for object in partial_match:
                response_data = {
                    "name":object.name,
                    "phone_number":object.phone_number,
                    "is_spam":object.is_spam
                }
                _list.append(response_data)
        if _list:
             return HttpResponse(json.dumps(_list),content_type='Application/json',status=200)
        else:
            return HttpResponse('no result found for the given name', status=200)

class SearchByPhone(View):
    def get(self,request):
        import pdb;pdb.set_trace()
        search_query = request.GET.get('phone_number')
        registered_user_match = UserDB.objects.filter(phone_number=search_query,is_registered=True)
        if registered_user_match:
            response_data = {
            "name":registered_user_match[0].name,
            "phone_number":registered_user_match[0].phone_number,
            "is_spam":registered_user_match[0].is_spam
            }
            return HttpResponse(json.dumps(response_data),content_type='Application/json',status=200)
        else:
            response_data = []
            user_match = UserDB.objects.filter(phone_number=search_query)
            if user_match:
                for object in user_match:
                    response_data.append({
                        "name":object.name,
                        "phone_number":object.phone_number,
                        "is_spam":object.is_spam
                    })
                return HttpResponse(json.dumps(response_data), content_type='Application/json', status=200)
            else:
                return HttpResponse('no result found for the given phone_number', status=200)
















