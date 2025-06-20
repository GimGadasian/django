# Generated by Django 5.2.1 on 2025-06-10 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0002_remove_board_id'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('cpuw', models.CharField(blank=True, max_length=20, null=True)),
                ('ccontent', models.TextField(blank=True)),
                ('cdate', models.DateField(auto_now=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]
