# Generated by Django 4.0.6 on 2022-11-04 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_organization_remove_plot_block_remove_sector_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('plan_description', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('original_price', models.PositiveIntegerField(blank=True, null=True)),
                ('seller_price', models.PositiveIntegerField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('is_available', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='projects.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
