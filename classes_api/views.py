from django.shortcuts import render
from rest_framework.generics import(ListAPIView,
                                    RetrieveAPIView,
                                    RetrieveUpdateAPIView,
                                    DestroyAPIView,
                                    CreateAPIView
                                    )
from classes.models import Classroom
from .serializers import ( RegisterSerializer ,
                           ClassListSerializer,
                           
                         )


class CreateUser(CreateAPIView):
    serializer_class = RegisterSerializer


class ClassroomList (ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer


class ClassroomDetail (RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
