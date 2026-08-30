# Per-user rate limiting demo.
# Tracks each user's recent request timestamps in a sliding time window and
# throttles (with a backoff sleep) once they exceed a fixed request count
# within that window — a basic rate-limiting pattern for AI request handling.
import time
from collections import defaultdict

RATE_LIMIT = 3   # requests per window
WINDOW = 5       # seconds

user_requests = defaultdict(list)

def handle_request(user_id):

    now = time.time()
    user_requests[user_id] = [
        t for t in user_requests[user_id] if now - t < WINDOW
    ]

    if len(user_requests[user_id]) >= RATE_LIMIT:
        print(f"User {user_id} throttled → applying backoff")
        time.sleep(2)
        return "Rate limit exceeded"

    user_requests[user_id].append(now)
    return "Request processed"


# Simulate requests
for i in range(6):
    print(handle_request("user1"))