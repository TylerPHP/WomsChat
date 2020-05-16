from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.models import Room
from chat_room.serializers import RoomSerializers


class Rooms(APIView):
    """Команата чата"""
    def get(self, request):
        roms = Room.objects.all()
        serializer = RoomSerializers(roms, many=True)
        return Response({"data": serializer.data})

