# Generated by Django 3.2.7 on 2021-09-25 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagcloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='status',
            field=models.CharField(choices=[(1, '생필품'), (2, '문구류'), (3, '주방용품'), (4, '전자기기'), (5, '의류')], default=1, max_length=63),
        ),
    ]
