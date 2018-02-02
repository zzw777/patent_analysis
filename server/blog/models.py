from __future__ import unicode_literals

from django.db import models

import mongoengine

class reports(mongoengine.Document):
    _id = mongoengine.StringField(primary_key=True)
    time = mongoengine.StringField()
    status = mongoengine.StringField()
    source_pat_sents = mongoengine.ListField()
    compare_pats = mongoengine.ListField()
    report_html = mongoengine.FileField()
    report_pdf = mongoengine.FileField()

