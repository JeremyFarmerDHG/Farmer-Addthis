from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface

class IAddThisControlPanel(Interface):
    show_addthis = schema.Bool(
        title=u'First day of the conference',
        required=False,
        default=False,
    )

    show_debug = schema.Bool(
        title=u'Show Debug',
        required=False,
        default=False,
    )

    show_on_urls = schema.Tuple(
        title = u'Show On Urls',
        default=(),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    blacklist_urls = schema.Tuple(
        title = u'Blacklist Urls',
        default=(),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    # make this a choice on a vocab
    share_options = schema.Tuple(
        title = u'Share Options',
        default=(),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

class AddThisControlPanelForm(RegistryEditForm):
    schema = IAddThisControlPanel
    schema_prefix = "addthis"
    label = u'AddThis Settings'

AddThisControlPanelView = layout.wrap_form(
    AddThisControlPanelForm, ControlPanelFormWrapper
)