# Generated by Django 2.0.4 on 2018-04-26 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                             related_name='children', to='todo.TodoTree')),
            ],
        ),
    ]
