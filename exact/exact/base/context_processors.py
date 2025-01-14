from django.conf import settings
from exact.users.models import Team
from exact.tagger_messages.models import TeamMessage
from django.db.models import Q


def base_data(request):
    show_datasets = settings.SHOW_DEMO_DATASETS

    if request.user.is_authenticated:
        my_teams = Team.objects.filter(members=request.user)
        unread_message_count = 0
        #unread_message_count = TeamMessage.in_range(TeamMessage.get_messages_for_user(request.user).filter(~Q(read_by=request.user))).count()
    else:
        my_teams = None
        unread_message_count = 0

    return {
        'IMPRINT_URL': settings.IMPRINT_URL,
        'USE_IMPRINT': settings.USE_IMPRINT,
        'IMPRINT_NAME': settings.IMPRINT_NAME,
        'TOOLS_ENABLED': settings.TOOLS_ENABLED,
        'my_teams': my_teams,
        'unread_message_count': unread_message_count,
        'show_datasets':show_datasets
    }
