from rest_framework import serializers
from .models import Student
# #Validators
# def starts_with_a(value):
#         if value[0].lower()!='a':
#             raise serializers.ValidationError("Name should start from A")

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=20)
    classname=serializers.CharField(max_length=10)


    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.name=validated_data.get('name',instance.name)
        instance.classname=validated_data.get('classname',instance.classname)
        instance.save()
        return instance
    

    # # Field Validation
    # def validate_id(self,value):
    #     if value >=100:
    #         raise serializers.ValidationError("Id cannot be greater than 100")
    #     return value
    # # Object Validation
    # def validate(self, data):
    #     nm=data.get('name')
    #     cs=data.get('classname')
    #     if nm.lower()=='ali' and cs.lower()!='sea':
    #         raise serializers.ValidationError("Class must be sea")
    #     return data
     
