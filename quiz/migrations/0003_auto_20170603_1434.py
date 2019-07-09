from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_questions_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='catagory',
            field=models.CharField(choices=[('sports', 'Sports'), ('movies', 'Movies'), ('maths', 'Maths'), ('generalknowledge', 'GeneralKnowledge')], max_length=20),
        ),
    ]
