# Generated by Django 5.1.2 on 2024-11-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyOrderAcceptance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('venue_type', models.CharField(choices=[('restaurant', 'Restaurant'), ('cafe', 'Cafe'), ('hall', 'Hall'), ('club', 'Club'), ('other', 'Other')], max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='company/profile_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='company/videos/')),
            ],
        ),
    ]