from rest_framework.pagination import PageNumberPagination


class DelivaryPagination(PageNumberPagination):
    page_size = 5