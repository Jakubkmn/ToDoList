# Generated by Django 3.2.12 on 2023-06-21 14:59

from django.db import migrations, models
import django.db.models.deletion
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(default=website.models.one_week)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.todolist')),
            ],
        ),
    ]
