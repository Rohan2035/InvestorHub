# Generated by Django 3.2 on 2022-03-13 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockpost', '0005_alter_stockposts_img1'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(default=None, max_length=50)),
                ('user_name', models.CharField(default=None, max_length=50)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockpost.stockposts')),
            ],
        ),
    ]
