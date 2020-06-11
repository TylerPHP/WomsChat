from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.models import Room, Chat
from chat_room.serializers import RoomSerializers, ChatSerializers


class Rooms(APIView):
    """Команата чата"""
    def get(self, request):
        roms = Room.objects.all()
        serializer = RoomSerializers(roms, many=True)
        return Response({"data": serializer.data})


class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        # room = request.data.get("room")
        dialog = ChatSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})
