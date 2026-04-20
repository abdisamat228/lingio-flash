class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'deck']
