class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['User', 'Title', 'description', 'is_public', 'created_at']