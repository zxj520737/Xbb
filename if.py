username = "zhangsan"
userpasswd = 123456
while True:
    name = input("请输入你的用户名:")
    if name == username:
        passwd = int(input("请输入密码:"))
        if passwd == userpasswd:
            print("恭喜{}用户成功登录".format(username))
        else:
            print("密码错误,请重新输入")
    else:
        print("请输入正确的用户名")