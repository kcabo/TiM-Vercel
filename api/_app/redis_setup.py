import os
import redis

REDIS_URL = os.environ['KV_REDIS_URL']

conn = redis.from_url(REDIS_URL, decode_responses=True)
