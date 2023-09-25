# Generated by Django 4.0.10 on 2023-09-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=14)),
            ],
        ),
    ]
