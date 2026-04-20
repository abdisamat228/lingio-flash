class SRSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRS
        fields = ['User', 'card', 'interval', 'ease_factor', 'repetitions', 'next_review', 'updated_at']
