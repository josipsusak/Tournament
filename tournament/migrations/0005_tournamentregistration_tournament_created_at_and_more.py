# Generated by Django 4.1.7 on 2025-02-22 09:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0002_remove_player_firstname_remove_player_lastname_and_more'),
        ('tournament', '0004_alter_signup_player_delete_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='Player.player')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tournaments', to='Player.player'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('ongoing', 'Ongoing'), ('finished', 'Finished')], default='open', max_length=20),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default=None, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.AddField(
            model_name='tournamentregistration',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='tournament.tournament'),
        ),
        migrations.AlterUniqueTogether(
            name='tournamentregistration',
            unique_together={('player', 'tournament')},
        ),
    ]
