from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from common.utils.http import build_json_resp
from chat.models import Chatroom, ChatRecord


@api_view(['POST'])
@login_required()
def send_message(request, chatroom_id):
    data = request.data
    chatroom = Chatroom.objects.get(id=chatroom_id)
    ChatRecord.objects.create(
        chatroom=chatroom, user=request.user, content=data['content'])
    return build_json_resp(data={
        'user': {
            'username': request.user.username,
            'email': request.user.email
        },
        'chatroom': {
            'name': chatroom.name
        },
        'content': data['content']
    })


@api_view(['GET'])
def get_message(request, chatroom_id):
    chat_records = ChatRecord.objects.filter(
        chatroom__id=chatroom_id).order_by('-send_time')
    return build_json_resp(data=[
        {
            'username': chat_record.user.username,
            'content': chat_record.content
        } for chat_record in chat_records
    ])


@api_view(['GET'])
def get_chatroom(request):
    chatrooms = ChatRecord.objects.order_by('create_time')
    return build_json_resp(data=[
        {
            'name': chatroom.name,
            'creator': chatroom.creator.username,
            'create_time': chatroom.create_time
        } for chatroom in chatrooms]
    )


@api_view(['GET'])
def get_chatroom_user(request, chatroom_id):
    pass


@api_view(['POST'])
@login_required()
def create_chatroom(request):
    data = request.data
    chatroom = Chatroom.objects.create(
        name=data['name'],
        creator=request.user
    )
    return build_json_resp(data={
        'name': chatroom.name,
        'creator': chatroom.user.username,
        'create_time': chatroom.create_time
    })


@api_view(['DELETE'])
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
