from plone import api
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

@provider(IVocabularyFactory)
def AddThisShowUrlsVocabularyFactory(context):
    values = api.portal.get_registry_record('addthis.show_on_urls')
    return safe_simplevocabulary_from_values(values)
