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
    sentences = mongoengine.StringField(required=True)
    pat_sentences = mongoengine.StringField()
    pat_id = mongoengine.StringField()
    C_CLA = mongoengine.StringField()
    C_DIS = mongoengine.StringField()
    E_ABS = mongoengine.StringField()
    E_CLA = mongoengine.StringField()
    E_DIS = mongoengine.StringField()

