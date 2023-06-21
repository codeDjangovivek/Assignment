from rest_framework import serializers
from to_do_lists.models import to_do

# create serializers here
class to_do_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = to_do
        fields = "__all__"