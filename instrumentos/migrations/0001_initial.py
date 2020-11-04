# Generated by Django 2.0.5 on 2018-06-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200)),
                ('descricao', models.CharField(db_index=True, max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]
