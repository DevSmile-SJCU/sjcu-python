# 주의 : 실수할 경우 임의의 파일이 삭제될 수 있으니, 주의 부탁드립니다.
#        윈도우 기준으로 실습을 구성하였습니다.

# Ref : https://docs.python.org/ko/3/library/os.html
# Ref : https://docs.python.org/ko/3/library/zipfile.html
import os
import glob     # 검색
import shutil   # 파일 복사, 이동

import zipfile  # 압축파일 관리

# 현재 작업중인 디렉토리를 반환
curPath = os.getcwd()
print(curPath)

# 파일 목록 보기
data = os.listdir(curPath)
print(data)

# 현재 목록의 파일 중 .py만 찾기 (참고 : recursive=True 옵션으로 하위 경로까지 탐색)
data = glob.glob(curPath + '\\*.py')
print(data)

# 디렉토리 만들기 (참고 : os.mkdir() )
try:
    os.makedirs(curPath + '\\mydir\\yourdir')
except FileExistsError as e:
    print(e)
    
# 파이썬 파일 복사하기
for pyFile in data:
    shutil.copy(pyFile, curPath + '\\mydir\\')

# 복사한 파일을 다시 이동하기
data = glob.glob(curPath + '\\mydir\\*.py')
print(data)

for pyFile in data:
    try:
        shutil.move(pyFile, curPath + '\\mydir\\yourdir')
    except shutil.Error as e:
        print(e)

# 복사/이동한 파일 목록 확인하기
data = os.listdir(curPath + '\\mydir\\yourdir')
print(data)

# 디렉토리 아동 후 현재 디렉토리 확인
os.chdir(curPath + '\\mydir\\yourdir')
print(os.getcwd())

# 파일 압축하기
data = os.listdir(os.getcwd())
with zipfile.ZipFile('myzip.zip', 'w') as myzip:
    for file in data:
        myzip.write(file)
    myzip.close()
    
# 압축파일 압축 해제 하기
with zipfile.ZipFile('myzip.zip', 'r') as myzip:
    myzip.extractall('..\\')
    myzip.close()
    
# 압축 파일 삭제하기
os.remove('myzip.zip')
    
# 디렉터리를 상위 폴더로 돌아가기
os.chdir('..\\')
print(os.getcwd())

# 디렉토리 삭제하기 + 목록 확인하기
try:
    os.removedirs('yourdir')
except OSError as e:
    print(e)

# 비어있지 않은 디렉터리 삭제
shutil.rmtree('yourdir')
    
data = os.listdir(os.getcwd())
print(data)

