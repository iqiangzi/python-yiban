import yiban
import time
import users
from myLog import Log
from yiban import Yiban

if __name__ == '__main__':

    log = Log("log")

    print("程序运行中...")

    user_list = users.get_users("users.xlsx")
    log.info("读取用户列表成功")

    yiban = Yiban(log)
    # 用户操作
    while True:
        time.sleep(1)
        current_time = time.localtime(time.time())
        if (current_time.tm_hour == 7) and (current_time.tm_min == 0) and (current_time.tm_sec == 0):
            for user in user_list:
                ses = yiban.login(user)
                yiban.send_feed(ses)
                yiban.send_topic(ses)
                yiban.send_vote(ses)

    # for user in user_list:
    #     ses = yiban.login(user)
