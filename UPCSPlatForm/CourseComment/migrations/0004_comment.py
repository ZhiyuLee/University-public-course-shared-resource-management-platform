# Generated by Django 2.1.2 on 2020-07-25 00:47

from django.db import migrations, models
import django.db.models.deletion
import win32timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MySite', '0001_initial'),
        ('CoursePart', '0001_initial'),
        ('CourseComment', '0003_auto_20200725_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('Comment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Comment_text', models.CharField(max_length=1024)),
                ('Time', models.DateTimeField(default=win32timezone.now)),
                ('Comment_User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='MySite.User')),
                ('Course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='CoursePart.Course')),
                ('To_Comment_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_comment', to='CourseComment.Comment')),
            ],
            options={
                'verbose_name': '用户评价',
                'verbose_name_plural': '用户评价',
                'ordering': ['Comment_User_ID', 'Time'],
            },
        ),
    ]