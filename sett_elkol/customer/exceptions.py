from rest_framework.exceptions import APIException


class NotYourCustomer(APIException):
    status_code = 403
    default_detail = "You can't edit a Customer that doesn't belong to you!"


class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "You can't follow yourself"
