from django.db.models import fields
from rest_framework import serializers
from.models import Features

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        # fields = ('is_child','firstName','lastName','parentId','address','street','city','state','zip_code')  
        fields = '__all__'

# class ChildFeaturesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Features
#         is_child = True
#         fields = ('is_child','firstName','lastName','parentId')
#         fields = '__all__'


# not working

# class FeaturesCreateSerializer(serializers.Serializer):
#     firstName = serializers.CharField(required=True, max_length=200)
#     lastName = serializers.CharField(required=True, max_length=200)
#     parentId = serializers.IntegerField(required=False)
#     user = serializers.CharField(required=True, max_length=10)
#     address = serializers.CharField(required=False)
#     street = serializers.CharField(required=False)
#     city = serializers.CharField(required=False)
#     state = serializers.CharField(required=False)
#     zip_code = serializers.CharField(required=False)

#     def create(self, validated_data):
#         if validated_data.get("user") == "CHILD":
#             if validated_data.get("parentId", None) is None:
#                 return {"Error": "For child parent id is required"}
#             else:
#                 return Features.objects.create(**validated_data)
#         elif validated_data.get('user') == 'PARENT':
#             address = validated_data.get('address')
#             street = validated_data.get('street')
#             city = validated_data.get('city')
#             state = validated_data.get('state')
#             zip_code = validated_data.get('zip_code')
#             if not address or not street or not city or not state or not zip_code:
#                 return {"Error": "For parent all address field is required"}
#             else:
#                 if validated_data.get('parentID', None) is not None:
#                     return {"Error": "For parent, parent id is not needed"}
#                 else:
#                     return Features.objects.create(**validated_data)
#         return {"Error": "Server Failed!!"}

    