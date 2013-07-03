from modeltranslation.translator import translator
from modeltranslation.models import autodiscover
from openbudget.settings import base as settings

def translated_fields(model):
    """Given a model, returns a list of translated field names for it.

    The returned list excludes the extra field created for the default language.

    """

    options = translator.get_options_for_model(model)
    fields = [f.name for l in options.fields.values() for f in l]

    for i, f in enumerate(fields):
        if f.endswith(settings.MODELTRANSLATION_DEFAULT_LANGUAGE):
            del fields[i]

    return fields
