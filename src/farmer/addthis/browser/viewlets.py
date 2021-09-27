from plone.app.layout.viewlets import ViewletBase
from plone import api
import re

class AddThisViewlet(ViewletBase):

    def should_show(self):
        # abs_url = self.context.absolute_url_path()
        abs_url = self.request.PATH_INFO
        whitelist_url = api.portal.get_registry_record('addthis.show_on_urls')
        blacklist_urls = api.portal.get_registry_record('addthis.blacklist_urls')
        if blacklist_urls is None:
            blacklist_urls = []
        breakpoint()
        for url in whitelist_url:
            if re.fullmatch(url, abs_url):
                if abs_url not in blacklist_urls:
                    return True
        # breakpoint()
        return False 

    def get_share_buttons(self):
        """
        Gets the share codes defined in Share options at /SiteID/@@addthis-controlpanel
        share codes should match the 'code' here - https://www.addthis.com/services
        """
        share_options = api.portal.get_registry_record('addthis.share_options')
        return share_options

    def show_debug(self):
        show_debug = api.portal.get_registry_record('addthis.show_debug')
        return show_debug
