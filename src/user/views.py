from dataclasses import field
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core import serializers
from common.utils.http import build_json_resp
from user.models import User


@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create_user(
        data['username'], data['password'], data['email'])
    return build_json_resp(
        data=serializers.serialize('json', user, fields=('email', 'username'))
    )

@api_view(['POST'])
def login(request):
    data = request.data
    user = auth.authenticate(
        request, username=data['email'], password=data['password'])
    if user is not None:
        auth.login(request, user)
    return build_json_resp(
        data=serializers.serialize('json', user, fields=('email', 'username'))
    )

@api_view(['POST'])
@login_required()
def logout(request):
    auth.logout(request)
    return build_json_resp()