from rest_framework.pagination import PageNumberPagination


class ChefPagination(PageNumberPagination):
    page_size = 5
