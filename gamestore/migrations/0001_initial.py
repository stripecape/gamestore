# Generated by Django 2.0 on 2018-04-23 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(blank=True, max_length=150, null=True)),
                ('game_url', models.URLField(null=True)),
                ('high_score', models.IntegerField(default=0, null=True)),
                ('gameID', models.PositiveIntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.NullBooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game', to='gamestore.StoreUser'),
        ),
    ]