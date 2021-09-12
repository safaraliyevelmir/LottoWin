from modeltranslation.translator import translator, TranslationOptions


from core.models import AboutUs, Index, JoinTitle, Service, Join, Faq
from contact.models import ContactInformation
from term_and_condination.models import PrivacyPolicy, TermAndCondition
from lottery.models import Lottery

class AboutUsTranslationOption(TranslationOptions):
    
    fields = ('text',)


class LotteryTranslationOption(TranslationOptions):
    
    fields = ('text',)


class IndexTranslationOption(TranslationOptions):

    fields = ('title','description',)


class ContactInformationTranslationOption(TranslationOptions):

    fields = ('title',)


class TermAndConditionTranslationOption(TranslationOptions):

    fields = ('text',)


class PrivacyPolicyTranslationOption(TranslationOptions):

    fields = ('text',)

class ServiceTranslationOption(TranslationOptions):

    fields = ('title','text',)


class JoinTitleTranslationOption(TranslationOptions):

    fields = ('title','description')


class JoinTranslationOption(TranslationOptions):

    fields = ('title','short_description')


class FaqTranslationOption(TranslationOptions):
    
    fields = ('question','answer',)


translator.register(AboutUs,AboutUsTranslationOption)
translator.register(Index,IndexTranslationOption)
translator.register(Lottery,LotteryTranslationOption)
translator.register(Join,JoinTranslationOption)
translator.register(JoinTitle,JoinTitleTranslationOption)
translator.register(Service,ServiceTranslationOption)
translator.register(Faq,FaqTranslationOption)
translator.register(ContactInformation,ContactInformationTranslationOption)
translator.register(TermAndCondition,TermAndConditionTranslationOption)
translator.register(PrivacyPolicy,PrivacyPolicyTranslationOption)