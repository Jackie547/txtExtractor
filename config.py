#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "31605369"))
    API_HASH = os.environ.get("API_HASH", "f8b54f0c81481ebf1593adebb073d844")
    AUTH_USERS = os.environ.get("AUTH_USERS", "8282839142")
