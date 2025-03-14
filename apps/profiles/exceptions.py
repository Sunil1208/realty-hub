from rest_framework import status
from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_details = "The requested profile does not exist."


class NotYourProfile(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_details = "You can't edit a profile that doesn't belong to you"
