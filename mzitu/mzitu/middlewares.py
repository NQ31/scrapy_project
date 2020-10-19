# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random


class MzituSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MzituDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    ip_list=['180.107.182.236:57478', '110.82.167.207:40476', '117.69.147.2:45897', '222.242.184.239:24176', '115.210.158.77:42586', '27.150.86.88:58685', '61.145.8.87:46215', '182.99.186.247:32377', '111.72.148.175:26078', '183.92.197.228:24160', '61.154.88.132:54516', '115.151.179.217:47796', '113.74.55.65:44546', '60.175.9.8:54461', '36.56.150.199:41526', '36.59.104.142:44462', '223.242.8.164:23615', '115.223.146.122:51198', '36.7.249.83:29906', '183.148.2.147:22532', '180.107.182.166:31277', '112.67.57.107:26804', '120.35.176.216:31370', '115.223.149.11:56501', '114.104.131.47:43237', '106.42.192.66:62758', '114.104.130.42:39127', '117.63.18.210:31839', '59.60.132.6:60296', '183.165.180.61:21385', '119.41.144.230:34288', '122.241.204.65:45336', '218.72.139.42:30603', '119.132.109.17:39312', '101.29.117.212:64617', '222.242.162.12:36083', '61.145.5.91:56033', '122.239.164.172:36984', '36.56.145.0:53467', '114.237.203.32:50916', '183.141.61.170:30185', '175.18.195.89:32668', '182.147.6.147:29256', '115.223.179.197:29019', '121.225.139.127:47862', '119.84.213.34:42087', '183.94.90.73:58928', '140.240.232.91:28782', '119.54.4.226:46966', '222.190.222.243:45646', '221.9.130.199:37422', '125.68.120.76:54450', '117.70.47.211:29061', '218.59.223.122:51418', '114.100.174.52:22506', '117.44.43.131:23734', '115.226.243.48:59027', '60.167.5.73:24854', '180.112.50.57:35326', '180.126.71.174:31662', '122.143.86.136:48612', '115.152.233.99:25097', '58.19.248.16:44897', '112.194.251.218:34804', '36.24.2.29:51084', '119.132.32.91:47148', '114.100.169.110:24475', '49.85.42.212:22207', '116.138.241.71:46876', '115.223.161.126:63939', '117.84.68.173:52079', '58.219.60.230:50424', '1.70.65.109:25620', '218.27.35.182:59955', '125.105.177.151:63708', '218.10.162.207:60094', '14.134.109.199:39594', '60.176.235.115:32716', '175.160.171.224:60175', '218.74.74.84:26283', '183.32.225.42:42583', '27.204.52.4:63663', '122.4.29.166:49836', '202.104.185.160:36693', '106.5.122.51:57468', '121.225.139.122:35671', '113.225.86.0:50011', '113.218.235.79:20046', '221.227.163.160:21072', '223.198.224.190:45355', '113.218.236.39:56322', '117.66.81.20:45560', '117.92.214.121:36146', '115.226.243.86:23022', '111.72.119.15:62148', '58.52.116.145:57813', '115.230.58.225:61655', '220.191.12.4:27713', '113.225.88.122:44756', '125.121.174.224:41534', '']
    ex_ip_list=['182.99.185.37:20575', '117.42.243.27:63305', '59.58.63.254:63724', '113.242.171.241:63473', '59.63.119.107:22502', '36.56.147.183:55899', '114.237.75.244:45527', '183.164.226.173:48969', '120.34.196.202:40337', '182.122.245.49:65127', '115.209.80.4:41011', '117.69.147.126:32806', '60.172.212.62:32127', '183.165.192.160:25369', '220.179.102.193:21425', '182.111.152.91:53461', '171.11.206.180:43860', '122.239.187.93:52445', '218.95.123.217:52463', '110.86.183.2:47608', '114.223.176.118:49553', '115.50.111.239:36643', '114.223.179.199:23011', '117.63.18.208:59043', '182.121.209.157:45808', '114.99.18.240:46004', '121.226.188.106:62778', '183.165.180.78:46923', '111.72.99.244:30580', '180.113.48.188:23659', '1.192.155.27:20766', '180.119.95.149:55548', '117.57.62.213:30731', '60.182.72.156:34854', '140.240.232.245:31840', '115.223.147.128:53950', '114.223.188.229:39635', '120.38.64.24:61775', '223.242.97.15:34454', '42.230.81.93:59983', '223.242.22.255:25386', '60.166.163.58:57462', '180.106.121.84:63535', '183.164.227.34:26302', '27.150.127.156:38265', '183.151.253.153:27572', '1.194.190.84:22263', '42.224.99.226:63429', '140.240.232.1:24887', '117.63.18.185:38904', '122.4.52.119:42861', '27.209.214.96:52504', '182.244.168.169:40363', '117.44.30.204:25680', '114.102.2.86:63382', '1.70.64.114:51809', '221.208.39.250:28732', '171.112.93.179:33074', '218.64.199.208:63700', '60.167.7.85:35500', '175.172.91.147:26383', '183.7.73.251:44562', '114.228.254.138:48307', '115.223.183.37:29276', '180.122.115.105:62172', '183.92.216.193:47242', '125.66.15.232:24640', '119.5.217.4:51001', '182.244.164.233:52312', '115.226.235.156:23928', '125.120.206.116:62979', '117.84.70.38:65227', '219.128.34.228:41727', '139.213.170.193:32807', '220.203.50.202:54786', '218.64.196.17:52810', '117.86.155.219:39920', '124.161.128.160:41863', '112.67.59.130:36750', '114.227.5.50:25269', '125.105.175.151:37848', '122.236.183.191:33410', '115.209.102.28:39676', '182.99.152.250:49307', '114.227.107.13:60801', '180.122.144.131:24641', '123.134.237.86:30898', '124.161.128.141:33429', '119.5.217.182:51752', '113.229.61.2:40180', '117.91.250.197:42917', '180.114.188.2:59903', '117.66.88.183:44413', '175.166.35.139:28037', '39.66.15.96:29527', '60.215.36.140:21538', '119.5.248.174:63303', '221.9.144.171:24469', '58.214.151.242:21983', '113.56.70.66:44038', '']

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        request.headers['User_Agent']=random.choice(self.user_agent_list)
        request.meta['proxy']='https://'+random.choice(self.ip_list)
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.
        request.meta['proxy'] = 'http://' + random.choice(self.ex_ip_list)
        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
