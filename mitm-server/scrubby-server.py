#!/usr/bin/env python3

from mitmproxy import flowfilter
import os, sys, re, datetime, json

class RequestHacks:
    @staticmethod
    def all(msg):
        if ('all' in msg.host) and ('action=login' in msg.content):
            fake_lat, fake_lng = 25.0333, 121.5333
            tampered = re.sub('lat=([\d.]+)&lng=([\d.]+)', 'lat=%s&lng=%s' % (fake_lat, fake_lng), msg.content)
            msg.content = tampered
            print('[RequestHacks][Example.com] Fake location (%s, %s) sent when logging in' % (fake_lat, fake_lng))


class ResponseHacks:
    @staticmethod
    def all(msg):
        if ('all' in msg.request.host:
