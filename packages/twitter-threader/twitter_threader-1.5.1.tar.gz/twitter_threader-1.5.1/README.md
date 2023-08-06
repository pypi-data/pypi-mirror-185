# twitter-threader


## Introduction

Twitter Thread is a library to manage threads on Twitter. You can GET and POST threads on Twitter.



## Installation

```bash
pip install twitter_threader
```


## Usage

### GET a thread on Twitter

```python
from twitter_threader.threader import connect_api, Thread

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token_key = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

api = connect_api(consumer_key, consumer_secret, access_token_key, access_token_secret)

thread = Thread(api)
thread.convert_to_post('1247616218153902080')
```


### POST a thread on Twitter

```python
from twitter_threader.threader import connect_api, Thread

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token_key = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

api = connect_api(consumer_key, consumer_secret, access_token_key, access_token_secret)

thread = Thread(api)
username = 'YOUR USERNAME'
thread.post_thread(
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Metus dictum at tempor commodo ullamcorper a lacus. Amet justo donec enim diam vulputate. Sit amet justo donec enim diam vulputate ut pharetra sit. Leo duis ut diam quam. At ultrices mi tempus imperdiet. Mauris augue neque gravida in fermentum. Fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Placerat vestibulum lectus mauris ultrices eros in cursus turpis massa. In aliquam sem fringilla ut morbi tincidunt augue.',
    username)

```

