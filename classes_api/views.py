from django.shortcuts import render
from rest_framework.generics import(ListAPIView,
                                    RetrieveAPIView,
                                    RetrieveUpdateAPIView,
                                    DestroyAPIView,
                                    CreateAPIView
                                    )
from classes.models import Classroom
from .serializers import ( RegisterSerializer ,
                           ClassSerializer,
                           ClassCreateUpdateSerializer,

                         )


class CreateUser(CreateAPIView):
    serializer_class = RegisterSerializer


class ClassroomList (ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassSerializer


class ClassroomDetail (RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassroomCreate(CreateAPIView):
    serializer_class = ClassCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ClassroomUpdate(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassroomDelete(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
