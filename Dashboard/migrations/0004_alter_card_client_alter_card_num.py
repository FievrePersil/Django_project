# Generated by Django 4.0.5 on 2022-07-07 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_alter_card_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.utilisateur'),
        ),
        migrations.AlterField(
            model_name='card',
            name='num',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
    ]
