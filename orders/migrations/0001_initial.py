# Generated by Django 2.1.7 on 2019-04-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketplace', models.CharField(max_length=50)),
                ('purchase_date', models.DateField(null=True)),
                ('billing_lastname', models.CharField(max_length=200, null=True)),
                ('amount', models.FloatField()),
                ('nb_items', models.IntegerField()),
            ],
        ),
    ]