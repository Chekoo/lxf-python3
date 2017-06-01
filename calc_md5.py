# coding=utf-8


import hashlib


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def calc_md5(password):
    return get_md5(password + user + 'the-Salt')


def login(user, password):
    check = db[user]
    if check == calc_md5(password):
        return True
    else:
        return False


if __name__ == "__main__":
    print('1.register\n2.login\n3.exit')
    while 1:
        se = input('Select function:')
        if se.isdigit():
            se = int(se)
        if se == 2:
            user = input('Enter your user:')
            password = input('Enter your password:')

            if login(user, password):
                print('Pass')
            else:
                print('Failed!')
        elif se == 1:
            user = input('Enter new user: ')
            password = input('Enter your password: ')
            register(user, password)
        elif se == 3:
            print('End!')
            break
        else:
            print('Invalid Opreation!')
