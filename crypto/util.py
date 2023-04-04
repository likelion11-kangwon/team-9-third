def get_name():
    return input('이름을 입력하세요: ').strip()

def get_password():
    name = get_name()
    try:
        with open('%s-password' % name, 'rb') as f:
            return f.read()
    except:
        return None