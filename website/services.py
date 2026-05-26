from .models import Character


def get_player_characters(user_id):
    return Character.objects.filter(owner_id=user_id)
