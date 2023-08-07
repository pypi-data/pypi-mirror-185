import re
from typing import Optional
from django.http import JsonResponse


def json_response(data, status_code=200):
    resp = JsonResponse(data)
    resp.status_code = status_code
    return resp


def get_full_qualified_name(obj):
    return f"{obj.__module__}.{obj.__qualname__}"


def generate_operation_id_for_path(*, name: str, path: str, method: str) -> str:
    operation_id = name + path
    operation_id = re.sub("[^0-9a-zA-Z_]", "_", operation_id)
    operation_id = operation_id + "_" + method.lower()
    return operation_id


_UNPREFIXED_HEADERS = {"CONTENT_TYPE", "CONTENT_LENGTH"}


def get_http_header(headers: dict, key: str) -> Optional[str]:
    key = key.upper().replace("-", "_")
    key = ("HTTP_" + key) if key not in _UNPREFIXED_HEADERS else key

    return headers.get(key)
