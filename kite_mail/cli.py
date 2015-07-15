#!/usr/bin/env python
# -*- coding:utf-8 -*-

import click
from kite.takosan import Tako
from kite_mail.mail  import kiteMail
from kite_mail.utils import help_messages

@click.command(context_settings={'help_option_names' : ['-h', '--help']})
@click.argument('takosan_url', nargs=1, required=True)
@click.option('--name', nargs=1, default='Mail Notify',
        help=help_messages('name'))
@click.option('--channel', 'channels',
        nargs=1, required=True, multiple=True,
        help=help_messages('channel'))
@click.option('--icon', nargs=1, default=':mailbox_with_mail:',
        help=help_messages('icon'))
@click.option('--body/--no-body', default=False,
        help=help_messages('body'))
@click.option('--body-color', nargs=1,
        help=help_messages('color'))
@click.option('--body-prefix', nargs=1, default=':memo:',
        help=help_messages('body_prefix'))
@click.option('--subject-prefix', nargs=1, default=':round_pushpin:',
        help=help_messages('subject_prefix'))
@click.option('--from/--no-from', 'is_mail_from', default=False,
        help=help_messages('from'))
@click.option('--from-prefix', nargs=1, default=':black_nib:',
        help=help_messages('from_prefix'))
def main(takosan_url,
        channels,
        name,
        icon,
        body,
        body_color,
        body_prefix,
        subject_prefix,
        is_mail_from,
        from_prefix):

    RAW_MAIL = click.get_text_stream('stdin')
    kite_mail = kiteMail(RAW_MAIL)
    factory = kite_mail.factory

    notify_payload = {
        'name'    : name,
        'icon'    : icon,
        'color'   : body_color,
        'message' : u'{0} *{1}*'.format(subject_prefix, factory.get_subject()),
    }

    if body:
        notify_payload['text'] = u'{0} {1}'.format(body_prefix, kite_mail.get_mailpart())
    if is_mail_from:
        notify_payload['pretext'] = u'{0} From: {1[0]} {1[1]}'.format(from_prefix, factory.get_address('from'))

    kite = Tako(takosan_url, channels, notify_payload)
    kite.flying()


if __name__ == '__main__':
    main()
