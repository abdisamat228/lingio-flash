# Generated manually to match the current Card model.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_card_image_alter_card_deck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='deck.deck'),
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cards/'),
        ),
    ]
