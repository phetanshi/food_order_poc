from cachetools import TTLCache

menu_cache = TTLCache(maxsize=1, ttl=300)  # Cache for 5 minutes