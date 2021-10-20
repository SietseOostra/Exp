from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from captcha.fields import ReCaptchaField

class Intro(Page):
    form_model = 'player'
    form_fields = ['captcha']

    def get_form(self, data=None, files=None, **kwargs):
        frm = super().get_form(data, files, **kwargs)
        frm.fields['captcha'] = ReCaptchaField(label='')
        return frm

class Info_1(Page):
    form_model = 'player'
    form_fields = ['Instr1', 'Instr2']

class Info_2(Page):
    form_model = 'player'
    form_fields = ['Instr3']

class Info_3(Page):
    form_model = 'player'
    form_fields = ['Instr4', 'Instr5']

class Important(Page):
    form_model = 'player'
    form_fields = ['accept_important']

class E_judge(Page):
    form_model = 'player'
    form_fields = ['timer_id', 'alotax', 'check_alotax']

    def error_message(self, value):
        #if self.group.r == None:
            if value["check_alotax"] == None:
                return 'Please drag the slider to make a decision.'

class I_judge(Page):
    form_model = 'player'
    form_fields = ['i_judge_1', 'i_judge_2', 'i_judge_3', 'check_i_judge_1', 'check_i_judge_2', 'check_i_judge_3']

    def error_message(self, value):
        #if self.group.r == None:
            if value["check_i_judge_1"] == None:
                return 'Please drag all sliders to make your decisions.'
            if value["check_i_judge_2"] == None:
                return 'Please drag all sliders to make your decisions.'
            if value["check_i_judge_3"] == None:
                return 'Please drag all sliders to make your decisions.'

class Peq1(Page):
    form_model = 'player'
    form_fields = [
        'taxmanagement_check',
        'australia_check'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Peq2(Page):
    form_model = 'player'
    form_fields = [
        'fin_exp',
        'fin_own',
        'tax_exp'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Peq3(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'age',
        'education',
        'english',
        'attention_1'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class M(Page):
    form_model = 'player'
    form_fields = [
        'mturk',
        'mturk_feedback',
        'mturk_motivation'
    ]

class Thank(Page):
    form_model = 'player'
    form_fields = ['completion_code']

page_sequence = [
    Intro,
    Info_1,
    Info_2,
    Info_3,
    Important,
    E_judge,
    I_judge,
    Peq1,
    Peq2,
    Peq3,
    M,
    Thank
]
