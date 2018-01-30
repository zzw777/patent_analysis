from __future__ import unicode_literals

from django.db import models

import mongoengine

class xwkModel(mongoengine.Document):
    num = mongoengine.StringField(required=True)
    title = mongoengine.StringField()
    C_AB = mongoengine.StringField()
    C_CLA = mongoengine.StringField()
    C_DIS = mongoengine.StringField()
    E_ABS = mongoengine.StringField()
    E_CLA = mongoengine.StringField()
    E_DIS = mongoengine.StringField()


class tttModel(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    # id = mongoengine.StringField(required=True)
    # source_pat_sents = mongoengine.StringField()
    # compare_pats = mongoengine.StringField()
    # source_sim = mongoengine.StringField()
    # novelty = mongoengine.StringField()
    # creativity = mongoengine.StringField()
    # report_html = mongoengine.FileField()
    report_pdf = mongoengine.FileField()

class report(mongoengine.Document):
    id = mongoengine.StringField(required=True)
    source_pat_sents = mongoengine.StringField()
    compare_pats = mongoengine.StringField()
    source_sim = mongoengine.StringField()
    novelty = mongoengine.StringField()
    creativity = mongoengine.StringField()
    report_html = mongoengine.FileField()
    report_pdf = mongoengine.FileField()

