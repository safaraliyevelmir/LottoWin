from modeltranslation import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import Blog, BlogTitle
from contact.models import ContactTitle

class BlogTranslationOption(TranslationOptions):
    
    fields = (
        'title','short_description','text'
    )

class BlogTitleTranslationOption(TranslationOptions):
    
    fields = (
        'title','desc',
    )


class ContactTitleTranslationOption(TranslationOptions):

    fields = (
       'title','desc',
    )

translator.register(Blog,BlogTranslationOption)
translator.register(BlogTitle,BlogTitleTranslationOption)
translator.register(ContactTitle,ContactTitleTranslationOption)