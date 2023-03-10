# Generated by Django 4.1.7 on 2023-03-14 09:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_customer_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='events/')),
                ('event_type', models.CharField(choices=[('MARRIAGE', 'marriage'), ('BIRTHDAY', 'birthday'), ('FUNERAL', 'funeral'), ('ENGAGEMENT', 'engagement'), ('BAPTISM', 'baptism'), ('HOUSE WARMING', 'house warming')], max_length=255)),
                ('event_date', models.DateField(max_length=64)),
                ('single_time', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
