from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('catagory', models.CharField(choices=[('sports', 'Sports'), ('movies', 'Movies'), ('maths', 'Maths'), ('generalknowledge', 'GeneralKnowledge')], max_length=10)),
            ],
            options={
                'ordering': ('-catagory',),
            },
        ),
    ]
