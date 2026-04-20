class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['User', 'card', 'quality', 'reviewed_at']