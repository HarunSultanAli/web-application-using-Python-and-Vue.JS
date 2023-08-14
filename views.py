from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from .models import Video, Subtitle
from .serializers import SubtitleSerializer

class VideoUpload(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request):
        file = request.FILES['video']
        video = Video.objects.create(file=file)
        return Response({'video_id': video.id}, status=status.HTTP_201_CREATED)

class SubtitleCreate(APIView):
    def post(self, request):
        video_id = request.data['video_id']
        subtitle_data = request.data['subtitle']
        video = Video.objects.get(id=video_id)
        subtitle = Subtitle.objects.create(video=video, **subtitle_data)
        return Response({'subtitle_id': subtitle.id}, status=status.HTTP_201_CREATED)

class SubtitleRetrieve(APIView):
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        subtitles = Subtitle.objects.filter(video=video)
        serializer = SubtitleSerializer(subtitles, many=True)
        return Response(serializer.data)
