# pip install matplotlib
# 설치한 라브러리 목록 확인 / 저장 : pip freeze > requirements.txt
# 라이브러리 설치 : pip install -r requirements.txt

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 100, size = 30)
y = np.random.randint(1, 100, size = 30)

plt.scatter(x, y)
plt.show()