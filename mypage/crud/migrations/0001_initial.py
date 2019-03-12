# Generated by Django 2.1.7 on 2019-03-12 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('major_id', models.IntegerField(primary_key=True, serialize=False)),
                ('major_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('hobby', models.CharField(max_length=50, null=True)),
                ('skill', models.CharField(max_length=50, null=True)),
                ('major_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Major')),
            ],
        ),
    ]
