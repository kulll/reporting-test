from locust import HttpLocust, TaskSet, task
from random import choice


class GetUrl(TaskSet):
    def on_start(self):
        self.country = choice(self.parent.countries)
        self.headers = {'X-Real-IP': self.country}

    @task
    def get_video(self):
        self.client.get('/videos/dummy.mp4', headers=self.headers)

    @task
    def get_image(self):
        self.client.get('/images/anwar.jpg', headers=self.headers)

    @task
    def get_file(self):
        self.client.get('/main', headers=self.headers)


class User(HttpLocust):
    task_set = GetUrl
    countries = ['14.192.160.7',
                 '23.249.192.7',
                 '177.8.224.7',
                 '31.214.176.7',
                 '27.117.192.7',
                 '109.224.0.7',
                 '5.101.224.7'
                 ]
