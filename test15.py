# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/13 3:35 下午
# file: test15.py
# IDE: PyCharm


class EmailFormatException(Exception):
    print("incorrect email format")


class Email(object):
    def __init__(self, email):
        if Email.check_email(email):
            self.email = email
        else:
            raise EmailFormatException

    @staticmethod
    def check_email(email=""):
        flag = True
        if "@" and ".com" in email:
            if email.endswith(".com"):
                return flag
            else:
                flag = False
        else:
            flag = False
        return flag

    def get_user_name(self):
        return "@".join(self.email.split("@")[:-1])

    def get_company_name(self):
        return self.email.split("@")[-1]




if __name__ == '__main__':
    a = input("输入邮箱: ")
    while True:
        if a == 'q' or a == 'Q':
            exit(0)
        else:
            try:
                email = Email(a)
            except EmailFormatException as e:
                print("incorrect email format")
            else:
                print(f"用户名: {email.get_user_name()}")
                print(f"公司名: {email.get_company_name()}")
        a = input("输入邮箱:")
