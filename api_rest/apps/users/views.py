from django.utils import timezone
from django.contrib.sessions.models import Session
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .api.serializers import UserTokenSerializer

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwars):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso. '
                    }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso. '
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Este usuario no puede iniciar sesión. '}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de Usuario o contraseña incorrectos. '})
        
class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = timezone.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                return Response({'token_message': 'Token eliminado', 'message': 'Sesiones de Usuario eliminados. '}, status=status.HTTP_200_OK)
            else:    
                return Response({'message': 'No se ha encontrado un usuario con estas credenciales. '}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'message': 'No se ha encontrado token en la petición'}, status=status.HTTP_409_CONFLICT)
        
class UserToken(APIView):
    def get(self,request,*args,**kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(username = username).first()
            )
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectas.'
            },status = status.HTTP_400_BAD_REQUEST)