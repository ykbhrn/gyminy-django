# pylint: disable=no-member, no-self-use
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from images.models import Image
from images.serializers import PopulatedImageSerializer

from .models import Like
from .serializers import LikeSerializer

class LikeListView(APIView):

    # permission_classes = (IsAuthenticated,)

    # def get_image(self, pk):
    #   try:
    #     return Image.objects.get(pk=pk)
    #   except Image.DoesNotExist:
    #     raise NotFound({'message': 'Not an existing image'})

    # def post(self, request):
      # # liked_image = self.get_image(pk)
      # liked_image = self.get_image(request.data['image'])
      # # populated_image = PopulatedImageSerializer(request.data['image'])
      # request.data['owner'] = request.user.id
      # created_like = LikeSerializer(data=request.data)
      # if created_like.is_valid():
      #     created_like.save()
      #     return Response(liked_image.data, status=status.HTTP_201_CREATED)
      # return Response(created_like.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    permission_classes = (IsAuthenticated, )

    def post(self, request):
      try:
        like = Like.objects.get(owner=request.user.id, image=request.data['image'])
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      except Like.DoesNotExist:
        request.data['owner'] = request.user.id
        created_like = LikeSerializer(data=request.data)
        if created_like.is_valid():
            created_like.save()
            return Response(status=status.HTTP_201_CREATED)
        raise ValidationError()
# class LikeDetailView(APIView):

#     permission_classes = (IsAuthenticated, )

#     def get_like(self, pk):
#         try:
#             return Like.objects.get(pk=pk)
#         except Like.DoesNotExist:
#             raise NotFound()

#     # def is_like_owner(self, like, user):
#     #     if like.owner.id != user.id:
#     #         raise PermissionDenied()

#     def delete(self, request, pk):
#         like_to_delete = self.get_like(pk)
#         self.is_like_owner(like_to_delete, request.user)
#         like_to_delete.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)