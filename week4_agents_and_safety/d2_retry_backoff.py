# RETRY WITH EXPONENTIAL BACKOFF: a reliability pattern for calling flaky
# external services (APIs, tools). Instead of failing immediately or
# retrying instantly (which can hammer a struggling service), each failed
# attempt waits progressively longer (2^attempt seconds here) before
# trying again, giving the service time to recover.
import time, random

def unreliable_api():
    return random.choice([None,"OK"])

def call_with_retry(max_attempts=3):
    for attempt in 1,2,3:
        result = unreliable_api()
        if result:
            return result
        
        wait_time = 2 ** attempt
        print(f"Attempt {attempt} failed. Retrying in {wait_time} seconds...")
        time.sleep(wait_time)

    return "All attempts failed. Please try again later."

print(call_with_retry())