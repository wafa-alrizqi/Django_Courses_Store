# Generated by Django 4.0.5 on 2022-06-04 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CoursesStoreApp', '0001_initial'),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CoursesStoreApp.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Course.course'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CoursesStoreApp.customer'),
        ),
    ]