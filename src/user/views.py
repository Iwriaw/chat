from dataclasses import field
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core import serializers
from common.utils.http import build_json_resp
from user.models import User


@require_http_methods(['POST'])
def register(request):
    params = request.POST
    user = User.objects.create_user(
        params['username'], params['password'], params['email'])
    return build_json_resp(
        data=serializers.serialize('json', user, fields=('email', 'username'))
    )

@require_http_methods(['POST'])
def login(request):
    params = request.POST
    user = auth.authenticate(
        request, username=params['email'], password=params['password'])
    if user is not None:
        auth.login(request, user)
    return build_json_resp(
        data=serializers.serialize('json', user, fields=('email', 'username'))
    )

@require_http_methods(['POST'])
@login_required()
def logout(request):
    auth.logout(request)
    return build_json_resp()