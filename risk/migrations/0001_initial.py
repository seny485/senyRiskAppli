# Generated by Django 2.1.15 on 2020-07-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regime', models.CharField(max_length=4)),
                ('produit', models.CharField(max_length=10)),
                ('mode_cond', models.CharField(max_length=4)),
                ('origine', models.CharField(max_length=3)),
                ('provenance', models.CharField(max_length=4)),
                ('valeur_caf', models.IntegerField()),
                ('poids_net', models.IntegerField()),
                ('destinataire', models.CharField(max_length=7)),
                ('declarant', models.CharField(max_length=7)),
                ('mode_paiement', models.IntegerField()),
                ('circuit', models.CharField(max_length=1)),
            ],
        ),
    ]