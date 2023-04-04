import crypto
import util

if __name__ == '__main__':
    name = util.get_name()
    password = crypto.hash(bytes(name, 'utf-8'))
    with open('%s-password' % name,'wb') as f:
        f.write(password)
    print('비밀번호가 생성되었습니다.')
