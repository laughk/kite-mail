#!/usr/bin/env python
# -*- coding:utf-8 -*-

def help_messages(command):

    msg = {
        'channel':
            'Name of notice channel, or id (e.g. #example, @id)',
        'name':
            'set botname',
        'icon':
            'set image url or emoji (e.g. :shachikun:)',
        'body':
            'the flag decide include mail body part. (Default: False) ',
        'body_prefix':
            'add prefix text message for mail body part. (Default: ":memo:" )',
        'subject_prefix':
            'add prefix text message for mail subject. (Default: ":round_pushpin:" )',
        'from':
            'the flag decide include mail from part. (Default: False) ',
        'from_prefix':
            'add prefix text message for mail from part. (Default: ":black_nib:" )',
        'color':
            'set color border along the left side of the message attachment [good|warning|danger|<hex color code>]  (e.g. #439FE0)',
    }

    if msg[command] :
        return msg[command]
    else:
        return None

def version():
    return '0.0.1.dev0'
