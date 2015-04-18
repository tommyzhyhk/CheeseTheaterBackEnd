from rest_framework import status
from django.shortcuts import render
from django.views.generic.base import View
from movieshow.models import Movie,CheeseUser,Theater,MovieShip,Order
from django.http import JsonResponse
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.db.models import Q
from rest_framework.serializers import ModelSerializer
from django.forms import ModelForm
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django.views.decorators.cache import cache_page
from rest_framework.parsers import JSONParser
import redis
from rest_framework import serializers
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
red=redis.Redis()
class OrderSeria(ModelSerializer):
     class Meta:
         model=Order
         fields=['id','moviename','theatername','tickets','moneys','orderedtime','user']



class TheaterSeria(ModelSerializer):
     class Meta:
        model=Theater
        fields=['id','name']
       
class MovieShipSeria(ModelSerializer):
     id=serializers.IntegerField(source='theater.id')
     name=serializers.CharField(source='theater.name')
     class Meta:
         model=MovieShip
         fields=['id','name','tickets']
class UserSeria(ModelSerializer):
     class Meta:
        model=User
        fields=['id','password','username','email']
     def create(self,validated_data):
          user=User(**validated_data)
          user.set_password(validated_data['password'])
          user.save()
          return user



class MovieSeria(ModelSerializer):
      theaters=MovieShipSeria(source='movieship_set',many=True,read_only=True)
      class Meta:
        model=Movie
        fields=('id','detail','image','money','name','year','number','theaters')
class MoviesSeria(ModelSerializer):
     class Meta:
        model=Movie
        fields=('id','detail','image','name')
class Movies(generics.ListAPIView):
      serializer_class=MoviesSeria
      queryset=Movie.objects.all()
      renderer_classes=[JSONRenderer]

class MovieDetail(generics.RetrieveAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSeria
    renderer_classes=(JSONRenderer,)    
    filter_backends=(filters.DjangoFilterBackend,)
    filter_fields=('id',)




class MovieShow(generics.ListAPIView):
     queryset=Movie.objects.all()
     serializer_class=MovieSeria
     renderer_classes=(JSONRenderer,)
     filter_backends=(filters.SearchFilter,)
     search_fields=('name','detail')
     
     
class CheeseUserForm(ModelForm):
     class Meta:
         model=CheeseUser
         fields=['name','email','password']


class UserLogup(generics.CreateAPIView):
        queryset=User.objects.all()
        serializer_class=UserSeria 
        parser_classes=[JSONParser]
        def create(self,request,*args,**kwargs):
             global red
             red.sadd('names',request.data['username'])  
             return super().create(request,*args,**kwargs) 



     
def show(request):
     item=request.GET['itemid']
      

     if request.session.get(item,False):
          
          num=request.session[item]
          request.session[item]=num+1
          print(num)
          return HttpResponse('world')
     else:
          
          request.session[item]=1
          return HttpResponse('hello')
class Check(APIView):
     parser_classes=[JSONParser]
     renderer_classes=[JSONRenderer]
     def get(self,request):
         global red
         if red.sismember('names',request.query_params['username']):
              return Response({'taken':True})
         else:
              return Response({'taken':False})

class Shop(APIView):
     
    
     def get(self,request):
          
          id=request.query_params['id']
          movie=request.query_params['movie']
          theater=request.query_params['theater']
          tickets=request.query_params['tickets']
          money=request.query_params['money']
          moneys=int(money)*int(tickets)
          sid=uuid.uuid4()
          sid=str(sid)          
          request.session[sid]={'id':id,'movie':movie,'theater':theater,'tickets':tickets,'moneys':moneys}
          

          return Response('ok')

class ShoppingCar(APIView):
     
      renderer_classes=[JSONRenderer] 
      def get(self,request):
         shoppings=[]
         for key,value in request.session.items():
                value['orderid']=key 
                shoppings.append(value)
         return Response(shoppings)
#this view is for checkout and saving user's orders          
class CheckOut(APIView):
       parser_classes=[JSONParser]
       renderer_classes=[JSONRenderer]           
       authentication_classes=[TokenAuthentication]
       permission_classes=[IsAuthenticated]

       def post(self,request):
              
              orderseria=OrderSeria(data=request.data,many=True)
               
              if orderseria.is_valid():
                     
                     orderseria.save(user=request.user)
                     print(request.data)
                     for order in request.data:
                           key=str(order['orderid'])
                           del request.session[key]
                     return Response(status=status.HTTP_201_CREATED)
           
              return Response(orderseria.errors,status=status.HTTP_400_BAD_REQUEST)
class Orders(generics.ListAPIView):
        serializer_class=OrderSeria
        renderer_classes=[JSONRenderer]
        authentication_classes=[TokenAuthentication]
        permission_classes=[IsAuthenticated]     
        def get_queryset(self):
             return Order.objects.filter(user=self.request.user)


















# Create your views here.
