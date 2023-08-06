import json
import logging
from datetime import datetime, timedelta

from dateutil.parser import parse
from django.conf import settings
from django.db.models.fields import timezone
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from music.constants import JELLYFIN_POST_KEYS as KEYS
from music.models import Track
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scrobbles.constants import (
    JELLYFIN_AUDIO_ITEM_TYPES,
    JELLYFIN_VIDEO_ITEM_TYPES,
)
from scrobbles.models import Scrobble
from scrobbles.scrobblers import (
    jellyfin_scrobble_track,
    jellyfin_scrobble_video,
    mopidy_scrobble_podcast,
    mopidy_scrobble_track,
)
from scrobbles.serializers import ScrobbleSerializer
from scrobbles.utils import convert_to_seconds
from videos.models import Video

from vrobbler.apps.music.aggregators import (
    scrobble_counts,
    top_artists,
    top_tracks,
    week_of_scrobbles,
)

logger = logging.getLogger(__name__)

TRUTHY_VALUES = [
    'true',
    '1',
    't',
    'y',
    'yes',
    'yeah',
    'yup',
    'certainly',
    'uh-huh',
]


class RecentScrobbleList(ListView):
    model = Scrobble

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        now = timezone.now()
        last_eight_minutes = timezone.now() - timedelta(minutes=8)
        # Find scrobbles from the last 10 minutes
        data['now_playing_list'] = Scrobble.objects.filter(
            in_progress=True,
            is_paused=False,
            timestamp__lte=now,
        )
        data['video_scrobble_list'] = Scrobble.objects.filter(
            video__isnull=False, in_progress=False
        ).order_by('-timestamp')[:10]
        data['top_daily_tracks'] = top_tracks()
        data['top_weekly_tracks'] = top_tracks(filter='week')
        data['top_monthly_tracks'] = top_tracks(filter='month')

        data['top_daily_artists'] = top_artists()
        data['top_weekly_artists'] = top_artists(filter='week')
        data['top_monthly_artists'] = top_artists(filter='month')

        data["weekly_data"] = week_of_scrobbles()
        data['counts'] = scrobble_counts()
        return data

    def get_queryset(self):
        return Scrobble.objects.filter(
            track__isnull=False, in_progress=False
        ).order_by('-timestamp')[:15]


@csrf_exempt
@api_view(['GET'])
def scrobble_endpoint(request):
    """List all Scrobbles, or create a new Scrobble"""
    scrobble = Scrobble.objects.all()
    serializer = ScrobbleSerializer(scrobble, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def jellyfin_websocket(request):
    data_dict = request.data

    # For making things easier to build new input processors
    if getattr(settings, "DUMP_REQUEST_DATA", False):
        json_data = json.dumps(data_dict, indent=4)
        logger.debug(f"{json_data}")

    scrobble = None
    media_type = data_dict.get("ItemType", "")

    if media_type in JELLYFIN_AUDIO_ITEM_TYPES:
        scrobble = jellyfin_scrobble_track(data_dict, request.user.id)

    if media_type in JELLYFIN_VIDEO_ITEM_TYPES:
        scrobble = jellyfin_scrobble_video(data_dict, request.user.id)

    if not scrobble:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {'scrobble_id': scrobble.id}, status=status.HTTP_201_CREATED
    )


@csrf_exempt
@api_view(['POST'])
def mopidy_websocket(request):
    data_dict = json.loads(request.data)

    # For making things easier to build new input processors
    if getattr(settings, "DUMP_REQUEST_DATA", False):
        json_data = json.dumps(data_dict, indent=4)
        logger.debug(f"{json_data}")

    if 'podcast' in data_dict.get('mopidy_uri'):
        scrobble = mopidy_scrobble_podcast(data_dict, request.user.id)
    else:
        scrobble = mopidy_scrobble_track(data_dict, request.user.id)

    if not scrobble:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {'scrobble_id': scrobble.id}, status=status.HTTP_201_CREATED
    )
