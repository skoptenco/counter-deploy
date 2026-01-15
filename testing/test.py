from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.counter = 0

    @task(1)
    def get_counter(self):
        response = self.client.get("/api/counter")
        if response and response.status_code == 200:
            result = response.json()
            self.counter = result["value"]

    @task(2)
    def increment(self):
        response = self.client.post("/api/counter/increment")
        if response and response.status_code == 200:
            result = response.json()
            self.counter = result["value"]

    @task(3)
    def decrement(self):
        response = self.client.post("/api/counter/decrement")
        if response and response.status_code == 200:
            result = response.json()
            self.counter = result["value"]

    @task(4)
    def reset(self):
        response = self.client.post("/api/counter/reset")
        if response and response.status_code == 200:
            result = response.json()
            self.counter = result["value"]