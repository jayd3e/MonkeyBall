def groupfinder(user_id, request):
    player = request.player
    if player is not None:
        return ['user']
    return None
