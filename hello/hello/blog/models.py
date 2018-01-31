from __future__ import unicode_literals

from django.db import models

import mongoengine

class reports(mongoengine.Document):
    id = mongoengine.IntField()
    time = mongoengine.StringField()
    source_pat_sents = mongoengine.DictField()
    compare_pats = mongoengine.ListField()
    innovative = mongoengine.StringField()
    novelty = mongoengine.StringField()
    creativity = mongoengine.StringField()
    report_html = mongoengine.FileField()
    report_pdf = mongoengine.FileField()

