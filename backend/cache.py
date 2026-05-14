import redis
import json

# connect to local redis server
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# cache helper functions
def get_cache(key):
    value = r.get(key)
    if value:
        return json.loads(value)
    return None


def set_cache(key, value, expire=300):
    r.setex(key, expire, json.dumps(value))