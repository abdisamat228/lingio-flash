class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['User', 'started_at', 'finished_at']