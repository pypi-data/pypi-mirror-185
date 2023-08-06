# Insta_cs API

A Python wrapper for the Instagram API with no 3rd party dependencies. Supports both the app and web APIs.

## Overview

I wrote this to access Instagram's API when they clamped down on developer access. Because this is meant to achieve [parity](COMPAT.md) with the [official public API](https://www.instagram.com/developer/endpoints/), methods not available in the public API will generally have lower priority.

## Features

- Supports many functions that are only available through the official app, such as:
    * Multiple feeds, such as [user feed], [location feed], [tag feed], [popular feed]
    * Post a [photo]or [video] to your feed or stories
    * [Like]/[unlike] posts
    * Get [post comments]
    * [Post]/[delete] comments
    * [Like]/[unlike] comments
    * [Follow]/[unfollow] users
    * User [stories]
    * And [more]
- The web api client supports a subset of functions that do not require login, such as:
    * Get user [info] and [feed]
    * Get [post comments]
    * And [more]
- Compatible with functions available through the public API using the ClientCompatPatch ([app]/[web]) utility class
- Beta Python 3 support

An [extension module](https://github.com/Charanpreet-Singh-AI/Insta_cs) is available to help with common tasks like pagination, posting photos or videos.

## Documentation

Documentation is available at https://github.com/Charanpreet-Singh-AI/Insta_cs

## Install

Install with pip:

``pip install insta_cs``

To update:

``pip install insta_cs --upgrade``

To update with latest repo code:

``pip install insta_cs --upgrade --force-reinstall``

Tested on Python 2.7 and 3.5.

## Usage

The [app API client](insta_cs/) emulates the official app and has a larger set of functions. The [web API client](insta_web_cs/) has a smaller set but can be used without logging in.

Your choice will depend on your use case.

The [``examples/``](examples/) and [``tests/``](tests/) are a good source of detailed sample code on how to use the clients, including a simple way to save the auth cookie for reuse.

### Option 1: Use the [official app's API](insta_cs/)

```python

from insta_cs import Client, ClientCompatPatch

user_name = 'YOUR_LOGIN_USER_NAME'
password = 'YOUR_PASSWORD'

api = Client(user_name, password)
results = api.feed_timeline()
items = [item for item in results.get('feed_items', [])
         if item.get('media_or_ad')]
for item in items:
    # Manually patch the entity to match the public api as closely as possible, optional
    # To automatically patch entities, initialise the Client with auto_patch=True
    ClientCompatPatch.media(item['media_or_ad'])
    print(item['media_or_ad']['code'])
```

### Option 2: Use the [official website's API](insta_web_cs/)

```python

from insta_web_cs import Client, ClientCompatPatch, ClientError, ClientLoginError

# Without any authentication
web_api = Client(auto_patch=True, drop_incompat_keys=False)
user_feed_info = web_api.user_feed('329452045', count=10)
for post in user_feed_info:
    print('%s from %s' % (post['link'], post['user']['username']))

# Some endpoints, e.g. user_following are available only after authentication
authed_web_api = Client(
    auto_patch=True, authenticate=True,
    username='YOUR_USERNAME', password='YOUR_PASSWORD')

following = authed_web_api.user_following('123456')
for user in following:
    print(user['username'])

# Note: You can and should cache the cookie even for non-authenticated sessions.
# This saves the overhead of a single http request when the Client is initialised.
```

### Avoiding Re-login

You are advised to persist/cache the auth cookie details to avoid logging in every time you make an api call. Excessive logins is a surefire way to get your account flagged for removal. It's also advisable to cache the client details such as user agent, etc together with the auth details.

The saved auth cookie can be reused for up to **90 days**.

## Donate

Want to keep this project going? Please donate generously [https://www.buymeacoffee.com/firstmodified](https://www.buymeacoffee.com/firstmodified)

[![Build](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/firstmodified)

## Support

Make sure to review the [contributing documentation](CONTRIBUTING.md) before submitting an issue report or pull request.

## Legal

Disclaimer: This is not affliated, endorsed or certified by Instagram. This is an independent and unofficial API. Strictly **not for spam**. Use at your own risk.
