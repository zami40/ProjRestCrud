from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Features
from .serializers import FeaturesSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import render, get_object_or_404


@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)


@api_view(['POST'])
def add_items(request):
   
    item = FeaturesSerializer(data=request.data)    

    # validating for already existing data
    if Features.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # return response(item.data)

# not working

# @api_view(['POST'])
# def add_items(request):
#     data = request.data
#     serializer = FeaturesCreateSerializer(data=data)
#     if serializer.is_valid():
#         serializer.create(**data)
#         return Response(serializer.data, status=status.HTTP_200_OK)    

    


@api_view(['GET'])
def view_items(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        items = Features.objects.filter(**request.query_param.dict())
    else:
        items = Features.objects.all()
  
    # if there is something in items else raise error
    
    if items:
        data = FeaturesSerializer(items,  many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
 

@api_view(['POST'])
def update_items(request, pk):
        
    item = Features.objects.get(pk=pk)
    data = FeaturesSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

        


@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Features, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

