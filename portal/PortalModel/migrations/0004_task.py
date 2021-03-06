# Generated by Django 2.2.3 on 2020-02-20 22:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PortalModel', '0003_auto_20200218_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('taskname', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=200)),
                ('state', models.IntegerField(default=0)),
                ('result', models.CharField(max_length=700)),
            ],
        ),
    ]
