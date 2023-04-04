# crypto

파일을 암호화/복호화 유틸리티

## 설치

```sh
$ pip install pycryptodomex
```

## 사용법

### 비밀번호 생성

```sh
$ python3 crypto/generate_password.py
```

### 파일 암호화

```sh
$ python3 crypto/encrypt.py 파일

# 예) python3 crypto/encrypt.py 곰두리.png
```

### 파일 복호화

```sh
$ python3 crypto/decrypt.py 파일

# 예) python3 crypto/decrypt.py 곰두리.png-5841
```
