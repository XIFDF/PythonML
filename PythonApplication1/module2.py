
import os
import math
import pandas as pd;
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
 
## value-p计算函数
def get_p_value(arrA, arrB):
 
  a = np.array(arrA)
  b = np.array(arrB)
  t, p = stats.ttest_ind(a,b)
  return p
 
## 读取excel文件
file1 = pd.read_excel(r'C:\Users\A\Desktop\Compounds.xlsx')

inputData = pd.DataFrame(columns=('x', 'y'))
## 循环遍历整个表，每次读一行，file1.index为总行数，“for i in file1.index” 表示 i 从 0 递增到 file1.index-1， 即访问所有行
for i in file1.index:
    f3 = float(file1.loc[i, 'Area: ZDF_Fatty_1.raw (F3)'])
    f4 = float(file1.loc[i, 'Area: ZDF_Fatty_2.raw (F4)'])
    f5 = float(file1.loc[i, 'Area: ZDF_Fatty_3.raw (F5)'])
    f6 = float(file1.loc[i, 'Area: ZDF_Lean_1.raw (F6)'])
    f7 = float(file1.loc[i, 'Area: ZDF_Lean_2.raw (F7)'])
    f8 = float(file1.loc[i, 'Area: ZDF_Lean_3.raw (F8)'])
    y = get_p_value([f3, f4, f5], [f6, f7, f8])         ## 计算value-p
    y = -math.log10(y)                                  ## 得出该行数据的纵坐标
    medianNumFatty = np.median([f3, f4, f5])
    medianNumLean  = np.median([f6, f7, f8])
    x = math.log2(medianNumFatty / medianNumLean)
    ap = {"x":x, "y":y}
    inputData = inputData.append(ap, ignore_index=True)
    print(i)

print(inputData)
plt.plot( 'x', 'y', data=inputData, linestyle='none', marker='.')
plt.show()