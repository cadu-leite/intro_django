# Generated by Django 2.2.3 on 2019-07-31 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appinterna', '0003_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matriculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinterna.Participante')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinterna.Curso')),
            ],
        ),
    ]