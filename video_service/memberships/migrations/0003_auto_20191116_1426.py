# Generated by Django 2.2.7 on 2019-11-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_remove_membership_membership_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Enterprise', 'ent'), ('Professional', 'pro'), ('Free', 'free')], default='Free', max_length=30),
        ),
        migrations.AddField(
            model_name='membership',
            name='price',
            field=models.IntegerField(blank=True, default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='slug',
            field=models.SlugField(default='lates'),
            preserve_default=False,
        ),
    ]
