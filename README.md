# docker_two_services
Originally the objective was to run a couple of python services/commands from docker containers and crontab.

But crontab is tricky with docker and there was a solution that fits my needs and it's actively mantained (at least to the date of this commit).

https://deck-chores.readthedocs.io/en/stable/usage.html#on-a-single-host




## Volume to save logging data

```bash
docker volume create vol_pywebs
```