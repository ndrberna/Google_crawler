from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.response import get_meta_refresh
from scrapy import log

class CustomRetryMiddleware(RetryMiddleware):

    def process_response(self, request, response, spider):
        url = response.url
        if response.status in [301, 307]:
            log.msg("trying to redirect us: %s" %url, level=log.INFO)
            reason = 'redirect %d' %response.status
            return self._retry(request, reason, spider) or response
        interval, redirect_url = get_meta_refresh(response)
        # handle meta redirect
        if redirect_url:
            log.msg("trying to redirect us: %s" %url, level=log.INFO)
            reason = 'meta'
            return self._retry(request, reason, spider) or response
        