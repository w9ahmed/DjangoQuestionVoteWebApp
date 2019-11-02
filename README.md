# RUN THE APP
```
docker-compose up --build
```

Might need to run this if starting from scratch
```
sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate
```


## To run unit tests
```
sudo docker-compose run web python manage.py test
```


## client testing
```
sudo docker-compose run web python manage.py shell
```

```python
from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client = Client()

response = client.get('/')
# we should expect a 404 from that address; if you instead see an
# "Invalid HTTP_HOST header" error and a 400 response, you probably
# omitted the setup_test_environment() call described earlier.
response.status_code
# 404
# on the other hand we should expect to find something at '/polls/'
# we'll use 'reverse()' rather than a hardcoded URL
from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
# 200
response.content
# b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'
response.context['latest_question_list']
# <QuerySet [<Question: What's up?>]>
```

---
# RUN A COMMAND
```
sudo docker-compose run web python manage.py COMMAND
```

https://docs.djangoproject.com/en/2.2/intro/tutorial05/#the-django-test-client
