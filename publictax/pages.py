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

class Financial1(Page):
    form_model = 'player'
    form_fields = ['FL1']
    
class Financial2(Page):
    form_model = 'player'
    form_fields = ['FL2']
    
    def is_displayed(self):
        player = self.player
        return player.FL1 == 1
    
class Financial3(Page):
    form_model = 'player'
    form_fields = ['FL3']
    
    def is_displayed(self):
        player = self.player
        return player.FL2 == 1

class Financial4(Page):
    form_model = 'player'
    form_fields = ['FL4']
    
    def is_displayed(self):
        player = self.player
        return player.FL3 == 3

class Financial5(Page):
    form_model = 'player'
    form_fields = ['FL5']
    
     def is_displayed(self):
        player = self.player
        return player.FL4 == 1
    
class Info_1(Page):
    form_model = 'player'
    form_fields = ['Instr1', 'Instr2']
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

class Info_2(Page):
    form_model = 'player'
    form_fields = ['Instr3']
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

class Info_3(Page):
    form_model = 'player'
    form_fields = ['Instr4', 'Instr5']
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

class Important(Page):
    form_model = 'player'
    form_fields = ['accept_important']
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

class E_judge(Page):
    form_model = 'player'
    form_fields = ['timer_id', 'alotax', 'check_alotax']
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

    def error_message(self, value):
        #if self.group.r == None:
            if value["check_alotax"] == None:
                return 'Please drag the slider to make a decision.'

class I_judge(Page):
    form_model = 'player'
    form_fields = ['i_judge_1', 'i_judge_2', 'i_judge_3', 'check_i_judge_1', 'check_i_judge_2', 'check_i_judge_3']
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

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
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

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
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

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
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

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
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

class Thank(Page):
    form_model = 'player'
    form_fields = ['completion_code']
    
    def is_displayed(self):
        player = self.player
        return player.FL5 == 2

page_sequence = [
    Intro,
    Financial1,
    Financial2,
    Financial3,
    Financial4,
    Financial5,
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
