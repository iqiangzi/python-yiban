import time
import requests
import json


class Yiban:
    def __init__(self, log):
        self.log = log

    # 获取当前日期和时间
    def get_time(self):
        return time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))

    # 获取当前时间
    def get_time2(self):
        return time.strftime('%H:%M', time.localtime(time.time()))

    # 获取分钟数
    def get_minute(self):
        return time.strftime('%M', time.localtime(time.time()))

    # 投票结束时间
    def vote_end_time(self):
        return time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() + 86400 * 7))

    # 登录
    def login(self, user):

        session = requests.session()

        login_url = "https://www.yiban.cn/login/doLoginAjax"

        response_login = session.post(login_url, user)

        if json.loads(response_login.text)["message"] == "操作成功":
            self.log.info("登录成功")
            # 签到
            # self.checkin(session)
        else:
            self.log.info("登录失败" + json.loads(response_login.text)["message"])

        return session

    # 用户签到
    def checkin(self, session):
        data = {
            "optionid[]": ""
        }

        get_login_url = "http://www.yiban.cn/ajax/my/getLogin"
        checkin_url = "http://www.yiban.cn/ajax/checkin/checkin"

        response_get_login = session.post(get_login_url)

        if json.loads(response_get_login.text)["data"]["checkin"] == 0:
            # 签到
            response_checkin = session.post(checkin_url)
            self.log.info("今日签到" + json.loads(response_checkin.text)["message"])
            # 回答问题
            # response_answer = session.post()

    # 发布动态
    def send_feed(self, session):
        data = {
            "content": self.get_time(),
            "privacy": "0",
            "dom": ".js-submit"
        }
        send_feed_url = "http://www.yiban.cn/feed/add"

        send_feed_response = session.post(send_feed_url, data)

        if json.loads(send_feed_response.text)["message"] == "操作成功":
            self.log.info("动态发布成功")
        else:
            self.log.info("动态发布失败" + json.loads(send_feed_response.text)["message"])

    # 发布话题
    def send_topic(self, session):

        data = {
            "title": self.get_time(),
            "puid": "7130177",
            "pubArea": "298264",
            "isNotice": "false",
            "dom": ".js-submit",
            "content": "<p>...</p>"
        }

        topic_response = session.post("http://www.yiban.cn/forum/article/addAjax", data)

        if json.loads(topic_response.text)["message"] == "操作成功":
            self.log.info("话题发布成功")
        else:
            self.log.info("话题发布失败" + json.loads(topic_response.text)["message"])

    # 发投票
    def send_vote(self, session):

        data = {
            "puid": "7130177",
            "scope_ids": "298264",
            "title": "~",
            "subjectTxt": "~",
            "subjectPic": "",
            "options_num": "3",
            "scopeMin": "1",
            "scopeMax": "1",
            "minimum": "1",
            "voteValue": self.vote_end_time(),
            "voteKey": "2",
            "public_type": "0",
            "isAnonymous": "1",
            "istop": "1",
            "sysnotice": "2",
            "isshare": "1",
            "rsa": "1",
            "dom": ".js-submit",
            "group_id": "298264",
            "subjectTxt_1": "1",
            "subjectTxt_2": "2",
            "subjectTxt_3": "3"
        }

        vote_url = "http://www.yiban.cn/vote/vote/add"

        send_vote_response = session.post(vote_url, data)

        if json.loads(send_vote_response.text)["message"] == "操作成功":
            self.log.info("投票发布成功")
        else:
            self.log.info("投票发布失败" + json.loads(send_vote_response.text)["message"])
