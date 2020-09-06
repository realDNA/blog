# Generated by Django 3.1.1 on 2020-09-06 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('contents', models.TextField()),
                ('publication_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='article_categories', to='general.category')),
            ],
        ),
    ]
