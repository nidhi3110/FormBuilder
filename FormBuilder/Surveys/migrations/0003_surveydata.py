# Generated by Django 3.2.6 on 2021-08-10 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Surveys', '0002_survey_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=10)),
                ('field1', models.TextField()),
                ('field2', models.TextField()),
                ('field3', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Surveys.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
