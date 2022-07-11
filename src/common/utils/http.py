from rest_framework.response import Response


def build_json_resp(data, code=0, error=''):
    return Response(data={
        'code': code,
        'error': error,
        'data': data
    })
