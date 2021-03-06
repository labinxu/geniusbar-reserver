# -*- coding: utf-8 -*-
from utils import debug
from utils.webpage import WebPage
import time
import urllib
import urllib2


class StorePage(WebPage):
    storeNumber = None
    headers = {}
    postData = {}

    def __init__(self, url, data=None,
                 headers={},
                 charset='utf-8',
                 timeout=20):
        super(StorePage, self).__init__(url, data, headers, charset, timeout)

    @classmethod
    def _init_headers(self):
        StorePage.headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,\
en;q=0.3'

        StorePage.headers['User-Agent'] = "Mozilla/5.0 (Windows \
NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"

        StorePage.headers['Accept'] = 'text/html,application/xhtml+xml,\
application/xml;q=0.9,*/*;q=0.8'
        StorePage.headers["Connection"] = 'keep-alive'
        StorePage.headers["Host"] = 'concierge.apple.com'


class GeniusbarPage(StorePage):
    geniusbarBaseUril = "http://concierge.apple.com/geniusbar/"


    def __init__(self, url, data=None,
                 headers={},
                 charset='utf-8',
                 timeout=100):
        super(GeniusbarPage, self).__init__(url, data, headers,
                                            charset,
                                            timeout)
        self.geniusbarUrl = None
        self.pageHeader = None

    def get_formtoken_value(self):
        attrs = {'name': '_formToken'}
        return self.get_tag_value('input', attrs=attrs)

    def get_store_list(self):
            attrs = {"id": "cnstores", "class": "listing"}
            soup = self.get_soup()
            tag = soup.find('div', attrs=attrs)
            hrefs = tag.findAll('a')
            suburl = None
            storeName = None
            data = {}
            index = 0
            for href in hrefs:
                suburl = href.get('href').encode('utf-8')
                storeName = href.text
                data[index] = (storeName, suburl)
                index += 1
            return data

    @classmethod
    def get_geniusbar_url(self):
        return GeniusbarPage.geniusbarBaseUril + GeniusbarPage.storeNumber

    def build_auth_post_data(self):
        tag_names = ['Env', 'appIdKey', 'captchaType', 'captchaToken',
                     'grpCode', 'language', 'iForgotNewWindowVar',
                     'paramcode', 'path', 'path2', 'segment']
        postData = {}
        for tag in tag_names:
            postData[tag] = self.get_tag_value("input", {'id': tag})
        return postData

    def build_governmentid_post_data(self):
        postData = {}
        postItems = ['clientTimezone', 'FirstName', 'LastName']
        for item in postItems:
            postData[item] = self.get_tag_value('input', {'id': item})
        return postData

    def build_smschallenge_post_data(self, serviceType):
        postData = {}
        postItems=['clientTimezone']
        for item in postItems:
            postData['clientTimezone'] = self.get_tag_value('input', {'id': item})

        # find service spantag
        spantag = self.get_soup().find('a', attrs={'id': serviceType})
        attrs = {'class': 'NSCSSStateHidden value', "name": "id"}
        idtag = spantag.find('span', attrs=attrs)
        postData['id'] = idtag.text
        postData['_formToken'] = self.get_formtoken_value()
        return postData

    def get_verification_code_pic(self):
        try:
            getData = {}
            getData['key'] = self.get_tag_value("input", {'id': 'captchaKey'})
            getData['format'] = self.get_tag_value("input",
                                                   {'id': "captchaFormat"})
            timeStamp = str(time.time()).replace('.', '')
            getData['t'] = timeStamp
            if not self.geniusbarUrl:
                self.geniusbarUrl = self.get_geniusbar_url()

            url = "%s/captcha?&%s" % (self.geniusbarUrl,
                                      urllib.urlencode(getData))

            if not self.pageHeader:
                self.pageHeader = GeniusbarPage.headers
            headers = self.pageHeader
            headers['Accept'] = 'image/png,image/*;q=0.8,*/*;q=0.5'
            headers['Accept-Encoding'] = 'gzip, deflate'
            request = urllib2.Request(url, headers=headers)
            try:
                data = urllib2.urlopen(request).read()
            except:
                debug.debug('read pic err')
            return (data, timeStamp)
        except Exception as e:
            debug.error(str(e))
            return (None, None)

    def build_submit_post_data(self):
        # soup = self.get_soup()
        postData = {}
        postData['_formToken'] = self.get_formtoken_value()
        attrs = {'id': 'captchaBackToText'}
        postData['captchaBackToText'] = self.get_tag_value('input', attrs)
        attrs = {'id': 'captchaTryNewAudio'}
        postData['captchaTryNewAudio'] = self.get_tag_value('input', attrs)
        attrs = {'id': 'captchaFormat'}
        postData['captchaFormat'] = self.get_tag_value('input', attrs)

        # captcha dir
        attrs = {'id': 'captchaKey'}
        postData['captchaKey'] = self.get_tag_value('input', attrs)

        attrs = {'id': 'captchaTryNewImg'}
        postData['captchaTryNewImg'] = self.get_tag_value('input', attrs)

        attrs = {'id': 'captchaVisionImpaired'}
        postData['captchaVisionImpaired'] = self.get_tag_value('input', attrs)
        #'<input name="countryISDCode" value="86" type="hidden">'
        postData['countryISDCode'] = self.get_tag_value('input', attrs={'name': 'countryISDCode'})
        return postData

    def get_smschalleng_steps(self, data=None):
        soup = self.get_soup(data)
        tag = soup.find('div', {'class': "info"})
        if not tag:
            return None
        try:
            text = tag.getText().replace(' ', '')
            pos = text.find(u'第1步')
            pose = text.find(u'第2步')
            text = text[pos: pose]
            text = text[text.find(':'):]
            text = text.replace(':', '\n').replace('：', '\n')
            return text
        except Exception as e:
            debug.error('get_challeng_steps function: %s' % str(e))
            return None

    def check(self, tagname, attrs):
        tag = self.get_soup().findAll(tagname, atts=attrs)

        if tag:
            return True
        return False
