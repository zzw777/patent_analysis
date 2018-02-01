from __future__ import unicode_literals

from django.db import models

import mongoengine

class reports(mongoengine.Document):
    # id = mongoengine.IntField()
    time = mongoengine.StringField()
    source_pat_sents = mongoengine.StringField()
    compare_pats = mongoengine.ListField()
    report_html = mongoengine.FileField()
    report_pdf = mongoengine.FileField()

