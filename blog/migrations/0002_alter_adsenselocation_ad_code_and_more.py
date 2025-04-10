# Generated by Django 5.1.6 on 2025-04-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsenselocation',
            name='ad_code',
            field=models.TextField(help_text='Codul complet <script>...</script> sau <ins>...</ins> de la AdSense.', verbose_name='Cod AdSense'),
        ),
        migrations.AlterField(
            model_name='adsenselocation',
            name='name',
            field=models.CharField(choices=[('below_header', 'Sub Antet (Liste)'), ('before_footer', 'Înainte de Footer'), ('above_content', 'Deasupra Conținut Articol'), ('below_content', 'Sub Conținut Articol'), ('below_hero', 'Sub Secțiunea Hero (Homepage)'), ('middle_page', 'Mijloc Pagină (Homepage)')], max_length=100, unique=True, verbose_name='Nume locație'),
        ),
    ]
