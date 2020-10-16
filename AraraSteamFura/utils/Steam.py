import re

from .aiorequest import get, post
from ..config import steamAPI

async def get32(s):
    # if already 32
    if re.match('7656119\d{10}',s):
        return s
    elif re.match('.*steamcommunity.com/id/(.*)/*',s):
        s = re.match('.*steamcommunity.com/id/(.*)?/*',s).group(1)
    r = await get(url='https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={}&vanityurl={}'.format(steamAPI,s))
    t = await r.json()
    if t.get('response').get('success'):
        return t.get('response').get('steamid')
    return False