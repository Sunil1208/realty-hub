from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.profiles.exceptions import ProfileNotFound, NotYourProfile
from apps.profiles.models import Profile
from apps.profiles.renderers import ProfileJSONRenderer
from apps.profiles.serializers import ProfileSerializer, UpdateProfileSerializer


class AgentListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(is_agent=True)
    serializer_class = ProfileSerializer


"""
    Implementation if it was a function based view

    from rest_framework.decorators import api_view, permission_classes
    from http import HTTPStatus

    @api_view(["GET"])
    @permission_classes([permissions.IsAuthenticated])
    def get_all_agents(request):
        agents = Profile.objects.filter(is_agent=True)
        serializer = ProfileSerializer(agents, many=True)
        name_spaced_response = {"agents": serializer.data}
        return Response(name_spaced_response, status=HTTPStatus.OK)
"""


class TopAgentListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(is_agent=True, top_agent=True)
    serializer_class = ProfileSerializer


class GetProfileApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile

        data = request.data
        serializer = UpdateProfileSerializer(
            instance=request.user.profile, data=data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
