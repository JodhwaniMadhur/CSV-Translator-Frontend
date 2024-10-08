from __future__ import unicode_literals

from django.db import models

languages=(('af','Afrikaans'),('sq','Albanian'),('am','Amharic'),('ar','Arabic'),('hy','Armenian')
,('az',	'Azerbaijani')
,('eu',	'Basque')
,('be',	'Belarusian')
,('bn',	'Bengali')
,('bs',	'Bosnian')
,('bg',	'Bulgarian')
,('ca',	'Catalan')
,('ceb','Cebuano')
,('ny',	'Chichewa')
,('zh',	'Chinese-Simple')
,('zh-TW','Chinese-Traditional')
,('co',	'Corsican')
,('hr',	'Croatian')
,('cs',	'Czech')
,('da',	'Danish')
,('nl',	'Dutch')
,('en',	'English')
,('eo',	'Esperanto')
,('et',	'Estonian')
,('tl',	'Filipino')
,('fi',	'Finnish')
,('fr',	'French')
,('fy',	'Frisian')
,('gl',	'Galician')
,('ka',	'Georgian')
,('de',	'German')
,('el',	'Greek')
,('gu',	'Gujarati')
,('ht',	'Haitian-Creole')
,('ha',	'Hausa')
,('haw','Hawaiian')
,('iw',	'Hebrew')
,('he',	'Hebrew')
,('hi',	'Hindi')
,('hmn','Hmong')
,('hu',	'Hungarian')
,('is',	'Icelandic')
,('ig',	'Igbo')
,('id',	'Indonesian')
,('ga',	'Irish')
,('itv','Italian')
,('ja',	'Japanese')
,('jw',	'Javanese')
,('kn',	'Kannada')
,('kk',	'Kazakh')
,('km',	'Khmer')
,('rw',	'Kinyarwanda')
,('ko',	'Korean')
,('ku',	'Kurdish-Kurmanji')
,('ckb','Kurdish-Sorani')
,('ky',	'Kyrgyz')
,('lo',	'Lao')
,('la',	'Latin')
,('lv',	'Latvian')
,('lt',	'Lithuanian')
,('lb',	'Luxembourgish')
,('mk',	'Macedonian')
,('mai','Maithili')
,('mg',	'Malagasy')
,('ms',	'Malay')
,('ml',	'Malayalam')
,('mt',	'Maltese')
,('mi',	'Maori')
,('mr',	'Marathi')
,('mn',	'Mongolian')
,('my',	'Myanmar-Burmese')
,('ne',	'Nepali')
,('no',	'Norwegian')
,('or',	'Oriya')
,('ps',	'Pashto')
,('fa',	'Persian')
,('pl',	'Polish')
,('pt',	'Portuguese')
,('pa',	'Punjabi')
,('ro',	'Romanian')
,('ru',	'Russian')
,('sm',	'Samoan')
,('gd',	'ScotsGaelic')
,('sr',	'Serbian')
,('st',	'Sesotho')
,('sn',	'Shona')
,('sd',	'Sindhi')
,('si',	'Sinhala')
,('sk',	'Slovak')
,('sl',	'Slovenian')
,('so',	'Somali')
,('es',	'Spanish')
,('su',	'Sundanese')
,('sw',	'Swahili')
,('sv',	'Swedish')
,('tg',	'Tajik')
,('ta',	'Tamil')
,('tt',	'Tatar')
,('te',	'Telugu')
,('th',	'Thai')
,('tr',	'Turkish')
,('tk',	'Turkmen')
,('uk',	'Ukrainian')
,('ur',	'Urdu')
,('ug',	'Uyghur')
,('uz',	'Uzbek')
,('vi',	'Vietnamese')
,('cy',	'Welsh')
,('xh',	'Xhosa')
,('yi',	'Yiddish')
,('yo',	'Yoruba')
,('zu',	'Zulu'))

class downloadCSV(models.Model):
    file_name = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=9,blank=True,choices=languages,default='en')

class downloadPrevCSV(models.Model):
    file_name = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=9,blank=True,choices=languages,default='en')