import os
import redis

REDIS_URL = os.environ["KV_URL"].replace("redis://", "rediss://")

conn = redis.from_url(REDIS_URL, decode_responses=True)
