from __future__ import unicode_literals

from django.db import models

import mongoengine


class report(mongoengine.Document):
    id = mongoengine.IntField(required=True)
    name = mongoengine.StringField()
    time = mongoengine.StringField()
    source_pat_sents = mongoengine.DictField()
    compare_pats = mongoengine.ListField()
    source_sim = mongoengine.ListField()
    novelty = mongoengine.StringField()
    creativity = mongoengine.StringField()
    report_html = mongoengine.FileField()
    report_pdf = mongoengine.FileField()

