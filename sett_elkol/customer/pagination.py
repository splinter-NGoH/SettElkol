from rest_framework.pagination import PageNumberPagination


class CustomerPagination(PageNumberPagination):
    page_size = 5
