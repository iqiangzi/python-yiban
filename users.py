import xlrd


def get_users(file_name):

    data = xlrd.open_workbook(file_name)

    table = data.sheets()[0]

    # 行数
    nrows = table.nrows
    # 列数
    ncols = table.ncols

    user_list = []

    for i in range(1, nrows):
        account = table.row_values(i)[0]
        password = table.row_values(i)[1]

        if isinstance(account, float):
            account = str(int(account))
        else:
            account = str(account)
        if isinstance(password, float):
            password = str(int(password))
        else:
            password = str(password)

        user = {
            "account": account,
            "password": password,
            "captcha": None
        }

        user_list.append(user)

    return user_list

