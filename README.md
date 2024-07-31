# movie

## Install
```
# main
$ pip install git+https://github.com/EstherCho-7/movie.git

# branch
$ pip install git+https://github.com/EstherCho-7/movie1.git@<BRANCH NAME>
$ pip install git+https://github.com/EstherCho-7/movie1.git@0.4/api
```
## Start
```
$ git clone https://github.com/EstherCho-7/movie1.git
$ cd <DIR>
$ source .venv/bin/activate
$ pdm install
$ pytest

$ # option
$ pdm venv create
$ source .venv/bin/activate
```

### Setting enc
```
# It's my key
$ export MOVIE_API_KEY = <key>
```

### Trouble Shooting
- [ ] sign up and get key from "Korea Movie Industry"
```
{'faultInfo': {'message': 'Invalid Key', 'errorCode': '320010'}}
```


