from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis 설정
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_client = redis.StrictRedis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    hostname = os.uname()[1]
    visits = redis_client.incr('counter')
    return f"Hostname: {hostname}, Visits: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
