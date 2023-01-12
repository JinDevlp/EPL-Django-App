# Generated by Django 4.1.5 on 2023-01-12 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_alter_team_areacode_alter_team_clubcolors_and_more'),
        ('player', '0002_alter_player_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playerteam', to='teams.team'),
        ),
    ]
