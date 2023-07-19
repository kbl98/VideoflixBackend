Videoflixbackend

This Project is a Python-Backend for loading, saving, converting and deleting mp4-Videos.
It is based on Django-Framework, in addition working with redis-rq and caching.
Postgres-DB can be used easily by installing Posgres and decommentating at settings.py.

1. Initiate a Project at your Server and install a new environment. 
2. To start this Backend you need to clone git-repository in environment.
3. Install requirements from requirements.txt of project
4. Install nginx and supervisor and configure
5. Configure redis-server and change data for redis/redis-rq at settings.py
6. Set superuser and migrate DB
