# Generated by Django 4.2.4 on 2023-09-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis_app', '0005_alter_signup_fname_alter_signup_lname_playerranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=255)),
            ],
        ),
    ]