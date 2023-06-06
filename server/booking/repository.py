from django.core import serializers

import json

from django.http import response
import booking.repository_helper as helper

def get_all(Target_class):
    return serializers.serialize("json", Target_class.objects.all())

def get(Target_class, id):
    result = serializers.serialize("json", [Target_class.objects.get(id=id)])
    return json.dumps(json.loads(result)[0])

def add(Target_class, request ):
    payload = json.loads(request.body)
    print(payload)
    helper.add_dates(payload)
    new_object = Target_class()
    new_object.add_fields(payload)
    return helper.try_save(new_object)

def edit(Target_class, id, request):
    print(id, request)
    object_to_edit = Target_class.objects.get(id=id)
    request_dict = json.loads(request.body)
    helper.add_dates(request_dict)
    object_to_edit.add_fields(request_dict)
    return helper.try_save(object_to_edit)

def delete(Target_class, id):
    try:
        Target_class.objects.get(id=id).delete()
        result = "okay"
    except:
        result = "error"
    return result
