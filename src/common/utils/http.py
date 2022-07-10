from django.http import JsonResponse


def build_json_resp(data, code=0, err=''):
    return JsonResponse(data={
        'code': code,
        'err': err,
        'data': data
    })
