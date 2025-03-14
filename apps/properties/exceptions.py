from rest_framework import status
from rest_framework.exceptions import APIException


class PropertyNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "The requested property does not exist."


class PropertyNotYours(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You are not the owner of this property."
