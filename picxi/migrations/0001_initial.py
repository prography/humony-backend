# Generated by Django 2.1.7 on 2019-03-30 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GUIDModel',
            fields=[
                ('guid', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='InPic',
            fields=[
                ('guidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='picxi.GUIDModel')),
                ('before', models.ImageField(upload_to='inpic/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('picxi.guidmodel',),
        ),
        migrations.CreateModel(
            name='OutPic',
            fields=[
                ('guidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='picxi.GUIDModel')),
                ('after', models.ImageField(upload_to='outpic/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('origin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picxi.InPic')),
            ],
            bases=('picxi.guidmodel',),
        ),
    ]
