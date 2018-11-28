# Generated by Django 2.1.2 on 2018-11-26 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('idno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('idno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.City')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
    ]
