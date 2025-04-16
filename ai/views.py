from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from .models import User
from . import models
from . import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from .utils import generate_video_from_file
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi




# -----------------------------register -----------------------------

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'login': openapi.Schema(type=openapi.TYPE_STRING, description='Login username'),
        'fullname': openapi.Schema(type=openapi.TYPE_STRING, description='fullname'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        'password_confirmation': openapi.Schema(type=openapi.TYPE_STRING, description='Password confirmation'),
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number')
    }
), parser_classes=[MultiPartParser, FormParser])  # swagger uchun
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    """ ro'yxatdan o'tish"""
    username = request.data.get('login')
    fullname = request.data.get('fullname')
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')
    phone_number = request.data.get('phone_number')


    if not all([username, password, password_confirmation, phone_number]):
        return Response({
            'success': False,
            'message': 'Malumotlar to‘liq emas'},
            status=status.HTTP_400_BAD_REQUEST)  # Forma to'liq to'ldirilmasa

    if password != password_confirmation:
        return Response({
            'success': False,
            'message': 'Password va confirm password bir xil emas'},
            status=status.HTTP_400_BAD_REQUEST)  # tasdiqlash paroli mos kelmasa

    if User.objects.filter(username=username).exists():
        return Response({'success': False,
                         'message': 'Bu usernamedagi foydalanuvchi bor'},
                        status=status.HTTP_400_BAD_REQUEST)  # login tanlab qilingan foydalanuvchi bor

    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=fullname,
            phone_number=phone_number
        )
        token, created = Token.objects.get_or_create(user=user)

        return Response({'success': True, 'token': token.key}, status=status.HTTP_201_CREATED)  # token yaratildi
    except Exception as e:
        return Response({'success': False, 'message': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # token yaratilmadi


# ------------------Login--------------------------------
@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'login': openapi.Schema(type=openapi.TYPE_STRING, description='Login username'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password')
    }
), responses={
    200: openapi.Response(description='Successful login', schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token')
        }
    )),
    400: 'Bad Request',
    401: 'Unauthorized'
})
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def log_in(request):
    """login qabul  qilingan foydalanuvchilar kirishi uchun """
    username = request.data.get('login')
    password = request.data.get('password')

    if not all([username, password]):
        return Response({'success': False, 'message': 'Username va parol kiritish majburiy'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'success': False, 'message': 'Login yoki parol noto‘g‘ri'},
                        status=status.HTTP_401_UNAUTHORIZED)


    token, created = Token.objects.get_or_create(user=user)
    return Response({'success': True, 'token': token.key}, status=status.HTTP_200_OK)


# -----------------------------logout------------------------
@swagger_auto_schema(method='post', responses={
    200: openapi.Response(description='Successful logout', schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Logout message')
        }
    )),
    500: 'Internal Server Error'
})
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def log_out(request):
    """LOG OUT QILISH"""
    try:
        token = request.auth
        token.delete()
        return Response({'success': True, 'message': 'Logout muvafaqiyatli'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        'username': user.username,
        'fullname': user.first_name,
        'credit': user.credit
    })


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def buy_price(request, price_id):
    try:
        price = models.Price.objects.get(id=price_id)
    except models.Price.DoesNotExist:
        return Response({'success': False, 'message': 'Bunday mahsulot mavjud emas'}, status=404)

    user = request.user

    if price.credit is None:
        return Response({'success': False, 'message': 'Ushbu mahsulot kredit bilan sotib olinmaydi'}, status=400)

    if user.credit < price.credit:
        return Response({'success': False, 'message': 'Yetarli kredit mavjud emas'}, status=400)

    # Pul yechish va sotib olish
    user.credit -= price.credit
    user.save()

    models.Purchase.objects.create(user=user, price=price)

    return Response({'success': True, 'message': 'Sotib olish muvaffaqiyatli yakunlandi'})

#---------------generated----------------------

class GenerateFromFileView(generics.CreateAPIView):
    queryset = models.Generated.objects.all()
    serializer_class = serializers.GeneratedSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        image = self.request.FILES.get("image")
        prompt = self.request.data.get("prompt")

        video_url = generate_video_from_file(image, prompt)

        if video_url:
            instance = serializer.save(video_url=video_url)
        else:
            raise ValidationError("Video URLni olishda xatolik yuz berdi.")


class PriceList(generics.ListAPIView):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSR


class MyPurchasesView(generics.ListAPIView):
    serializer_class = serializers.PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return models.Purchase.objects.filter(user=self.request.user).order_by('-date')
