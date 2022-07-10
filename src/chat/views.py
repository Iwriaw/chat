from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.core import serializers
from common.utils.http import build_json_resp
from chat.models import Chatroom, ChatRecord


@require_http_methods(['POST'])
@login_required()
def send_message(request, chatroom_id):
    params = request.POST
    chatroom = Chatroom.objects.get(id=chatroom_id)
    chat_record = ChatRecord.objects.create(
        chatroom=chatroom, user=request.user, content=params['content'])
    return build_json_resp(data={
        'user': {
            'username': request.user.username,
            'email': request.user.email
        },
        'chatroom': {
            'name': chatroom.name
        },
        'content': params['content']
    })


@require_http_methods(['GET'])
def get_message(request, chatroom_id):
    chat_records = ChatRecord.objects.filter(
        chatroom__id=chatroom_id).order_by('-send_time')
    return build_json_resp(data=[
        {
            'username': chat_record.user.username,
            'content': chat_record.content
        } for chat_record in chat_records
    ])


@require_http_methods(['GET'])
def get_chatroom(request):
    chatrooms = ChatRecord.objects.order_by('create_time')
    return build_json_resp(data=[
        {
            'name': chatroom.name,
            'creator': chatroom.creator.username,
            'create_time': chatroom.create_time
        } for chatroom in chatrooms]
    )


@require_http_methods(['GET'])
def get_chatroom_user(request, chatroom_id):
    pass


@require_http_methods(['POST'])
@login_required()
def create_chatroom(request):
    params = request.POST
    chatroom = Chatroom.objects.create(
        name=params['name'],
        creator=request.user
    )
    return build_json_resp(data={
        'name': chatroom.name,
        'creator': chatroom.user.username,
        'create_time': chatroom.create_time
    })


@require_http_methods(['DELETE'])
@login_required()
def delete_chatroom(request, chatroom_id):
    chatroom = Chatroom.objects.get(id=chatroom_id)
    if request.user != chatroom.user:
        return build_json_resp(code=1, str='permission denied')
    chatroom.delete()
    return build_json_resp(data={
        'name': chatroom.name,
        'creator': chatroom.user.username,
        'create_time': chatroom.create_time
    })
