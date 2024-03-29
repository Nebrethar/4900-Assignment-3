from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        user = serializer.save()
        print(user)
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

@csrf_exempt
@api_view(['GET', 'POST'])
def movie_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, context={'request': request}, many=True)
        return Response({'data': serializer.data})
 
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def getMovie(request, pk):
    """
    Retrieve, update or delete a movie instance.
    """
    try:
     movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        serializer = MovieSerializer(movie,context={'request': request})
        return Response(serializer.data)
 
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

