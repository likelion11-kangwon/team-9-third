import crypto
import sys
import util

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python3 decrypt.py (file)')
        exit(1)

    password = util.get_password()
    if password == None:
        print('비밀번호가 없습니다.')
        exit(1)

    input_file = None
    try:
        with open(sys.argv[1], 'rb') as f:
            input_file = f.read()
    except:
        print('지정된 파일(%s)이 없습니다.' % sys.argv[1])
        exit(1)
    
    decrypted = crypto.decrypt(input_file, password)

    with open(sys.argv[1] + '-decrypted', 'wb') as f:
        f.write(decrypted)
    
    print('지정된 파일이 복호화 되었습니다.')
