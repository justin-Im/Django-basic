# Generated by Django 3.2.3 on 2021-05-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_alter_fcuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='test@gmail.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
