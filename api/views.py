from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from landbuyers.models import LandBuyer
from users.models import User
from lawyers.models import Lawyer
from landseller.models import LandSeller
from .serializers import MinimalLandBuyersSerializer, MinimalLandsellersSerializer, MinimalLawyersSerializer, MinimalUserSerializer, UserSerializer
from .serializers import LawyersSerializer, LandsellersSerializer, LandBuyersSerializer








class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        # serializer = TeacherSerializer(teachers, many=True)
        serialiizer = MinimalUserSerializer(users,many=True)
        first_name = request.query_params.get("first name")
        last_name = request.query_params.get("Last name")
        if first_name:
            users = users.filter(first_name == first_name)
        if last_name:
            teachers = teachers.filter(last_name == last_name)
        return Response(serialiizer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# class UserListView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailView(APIView):
    def get(self,request,id):
        users= User.objects.get(id=id)
        serializer = UserSerializer(users,data=request.data)
        return Response(serializer.data)
    
    def put(self,request,id):
        users = User.objects.get(id=id)
        serializer = UserSerializer(users,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        

    def delete(self,request,id):
        users=User.objects.get(id=id)
        serializer =UserSerializer(users)
        users.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  
    


class LawyerListView(APIView):
    def get(self, request):
        lawyer = Lawyer.objects.all()
        # serializer = TeacherSerializer(teachers, many=True)
        serialiizer = MinimalLawyersSerializer(lawyer,many=True)
        firm = request.query_params.get("firm")
        # last_name = request.query_params.get("Last name")
        # if first_name:
        #     users = users.filter(first_name == first_name)
        if firm:
            firm= lawyer.filter(firm == firm)
        return Response(serialiizer.data)
    
    def post(self, request):
        serializer = LawyersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# class LawyerListView(APIView):
#     def get(self, request):
#         lawyers = Lawyer.objects.all()
#         serializer = LawyersSerializer(lawyers, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = LawyersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LawyerDetailView(APIView):
    def get(self,request,id):
        lawyer= Lawyer.objects.get(id=id)
        serializer = LawyersSerializer(lawyer,data=request.data)
        return Response(serializer.data)
    
    def put(self,request,id):
        lawyer = Lawyer.objects.get(id=id)
        serializer = LawyersSerializer(lawyer,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        

    def delete(self,request,id):
        lawyer=Lawyer.objects.get(id=id)
        serializer =LawyersSerializer(lawyer)
        lawyer.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  
    
    



class LandSellerListView(APIView):
    def get(self, request):
        landseller= LandSeller.objects.all()
        # serializer = TeacherSerializer(teachers, many=True)
        serialiizer = MinimalLandsellersSerializer(landseller,many=True)
        address= request.query_params.get("address")
        # last_name = request.query_params.get("Last name")
        # if first_name:
        #     users = users.filter(first_name == first_name)
        if address:
            address= landseller.filter(address == address)
        return Response(serialiizer.data)
    
    def post(self, request):
        serializer = LandsellersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# class LandSellerListView(APIView):
#     def get(self, request):
#         landseller = LandSeller.objects.all()
#         serializer = LandsellersSerializer(landseller, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = LandsellersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LandSellerDetailView(APIView):
    def get(self,request,id):
        landseller= LandSeller.objects.get(id=id)
        serializer = LandsellersSerializer(landseller,data=request.data)
        return Response(serializer.data)
    
    def put(self,request,id):
        landseller = LandSeller.objects.get(id=id)
        serializer = LandsellersSerializer(landseller,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        
    def delete(self,request,id):
        landseller=LandSeller.objects.get(id=id)
        serializer =LandsellersSerializer(landseller)
        landseller.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  
    


class LandBuyerListView(APIView):
    def get(self, request):
        landbuyer= LandBuyer.objects.all()
        # serializer = TeacherSerializer(teachers, many=True)
        serialiizer = MinimalLandBuyersSerializer(landbuyer,many=True)
        address= request.query_params.get("address")
        # last_name = request.query_params.get("Last name")
        # if first_name:
        #     users = users.filter(first_name == first_name)
        if address:
            address= landbuyer.filter(address == address)
        return Response(serialiizer.data)
    
    def post(self, request):
        serializer = LandBuyersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


# class LandBuyerListView(APIView):
#     def get(self, request):
#         landbuyer = LandBuyer.objects.all()
#         serializer = LandBuyersSerializer(landbuyer, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = LandBuyersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LandBuyerDetailView(APIView):
    def get(self,request,id):
        landbuyer= LandBuyer.objects.get(id=id)
        serializer =LandBuyersSerializer(landbuyer,data=request.data)
        return Response(serializer.data)
    
    def put(self,request,id):
        landbuyer = LandBuyer.objects.get(id=id)
        serializer = LandBuyersSerializer(landbuyer,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        

    def delete(self,request,id):
        landbuyer=LandBuyer.objects.get(id=id)
        serializer =LandBuyersSerializer(landbuyer)
        landbuyer.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  
    
    

