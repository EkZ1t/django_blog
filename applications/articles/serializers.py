from .models import Article, Tag, Comment 
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article 
        fields = '__all__'
        read_only_fields = ['user']
        
    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user 
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return representation 
        

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Article 
        fields = ['id', 'title', 'tag', 'user']
        
    def to_representation(self, instance: Article):
        representation = super().to_representation(instance)
        representation['tag'] = [tag.title for tag in instance.tag.all()] 
        return representation 

class TagSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault)
    
    class Meta:
        model = Tag 
        fields = ['id', 'title', 'user']
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text', 'created_at', 'updated_at', 'sub_comment']
        