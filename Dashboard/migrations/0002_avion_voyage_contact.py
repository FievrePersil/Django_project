# Generated by Django 4.0.5 on 2022-07-02 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('nomav', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('modelav', models.CharField(max_length=30)),
                ('capacite', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('voyid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('depart', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('datedep', models.DateTimeField()),
                ('avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.avion')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('msg', models.CharField(max_length=150)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.utilisateur')),
            ],
        ),
    ]
