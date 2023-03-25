# docker_two_services
Originally the objective was to run a couple of python services/commands from docker containers and crontab.

But crontab is tricky with docker and there was a solution that fits my needs and it's actively mantained (at least to the date of this commit).

https://deck-chores.readthedocs.io/en/stable/usage.html#on-a-single-host




## Volume to save logging data

```bash
docker volume create vol_pywebs
```

Reading data from the volume:

```
docker run --rm -i -v=vol_pywebs:/tmp/myvolume busybox find /tmp/myvolume
```

Once verified that the log file exists

```
sudo docker run --rm -i -v=vol_pywebs:/tmp/myvolume busybox cat /tmp/myvolume/app.log
```

### Note
requirements.txt is there just to have it on hand, it's not neccesary for this specific implementarion