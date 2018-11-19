# encoding='utf-8'

import json
import urllib.request as ur
import urllib.parse
import urllib.error as urlerror
from haf.common.log import Log

logger = Log.getLogger(__name__)

class HttpController(object):
    '''
    Http 请求 管理类
    '''

    def __init__(self):
        pass

    @staticmethod
    def getdata(data):
        '''
        将 get 的 data 格式化为 url 参数 形式

        :参数:
        * data : str/bytes/dict get 请求的参数
        :return: data
        '''
        datastr = "?"
        if isinstance(data, bytes):
            data = str(data, encoding="utf-8")
        if isinstance(data, str):
            try:
                data = json.loads(data)
                for d in data.keys():
                    datastr = datastr + str(d) + "=" + str(data[d]) + "&"
            except:
                return data
        elif isinstance(data, dict):
            for d in data.keys():
                datastr = datastr + str(d) + "=" + str(data[d]) + "&"

        return datastr[:-1]  # delete & at the last position

    @staticmethod
    def get(url, data=None, headers=None):
        '''
        http get 请求方法
        :参数:
        * url : 请求的 url
        :return: response.read() 返回的 请求内容
        '''
        try:
            url = url + HttpController.getdata(data)
            logger.debug('[url] ' + url)
            request = ur.Request(url=url, headers=headers, method="GET")
            if headers is not None:
                for key in headers.keys():
                    request.add_header(key, headers[key])
            response = ur.urlopen(request)

            if response is None:
                return {"result": "None"}
            else:
                logger.debug(str(response))

            return response
        except ur.URLError as e:
            logger.debug(str(e))
            return e
        except Exception as ee:
            logger.debug("error")
            return ee

    @staticmethod
    def post(url, data=None, headers=None, **kwargs):
        try:
            if "application/json" in headers.values():
                data = bytes(json.dumps(data), encoding='utf-8')
            else:
                data = bytes(urllib.parse.urlencode(data), encoding='utf-8')

            request = ur.Request(url=url, data=data, headers=headers, method="POST")
            response = ur.urlopen(request)

            if response is None:
                return {"result": "None"}
            else:
                logger.debug(str(response))

            return response
        except ur.URLError as e:
            logger.error(str(e), "post")
            return e
        except urlerror.HTTPError as httpe:
            logger.error(str(httpe))
            # if httpe.code == 400:
            return httpe
        except Exception as ee:
            logger.error(str(ee))
            return ee

    def put(self, url, data=None):
        try:
            data = bytes(data, encoding='utf8') if data is not None else None
            request = ur.Request(url, headers=self.headers, data=data)
            request.get_method = lambda: 'PUT'
            response = ur.urlopen(request, timeout=10)
            result = response.read()
            return result
        except ur.URLError as e:
            logger.error(str(e))
        except Exception as ee:
            logger.error(str(ee))

    def delete(self, url, data=None):
        data = bytes(data, encoding='utf8') if data is not None else None
        try:
            request = ur.Request(url, headers=self.headers, data=data)
            request.get_method = lambda: 'DELETE'
            response = ur.urlopen(request, timeout=10)
            result = response.read()
            data = data.encode() if data is not None else None
            return result
        except ur.URLError as e:
            logger.error(str(e))
        except Exception as ee:
            logger.error(str(ee))