from rest_framework.exceptions import APIException
from http import HTTPStatus


class ProfileNotFound(APIException):
    status_code = HTTPStatus.NOT_FOUND
    default_details = "The requested profile does not exist."


class NotYourProfile(APIException):
    status_code = HTTPStatus.FORBIDDEN
    default_details = "You can't edit a profile that doesn't belong to you"
