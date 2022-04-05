import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use(['seaborn-notebook'])

### Line Plot
'''
 plot은 그림 figure와 축 axes로 구성
 plt.figure : 축과 그래픽, 텍스트, 레이블을 표시하는 모든 객체를 포함하는 컨테이너
 plt.axes : 눈금과 레이블이 있는 테두리 박스로 시각화를 형성하는 플롯 요소를 포함
'''

# fig = plt.figure()
# plt.plot([0.1, 0.3, 0.4, 0.9])
# ax = plt.axes()

# fig = plt.figure()
# x = np.arange(0, 10, 0.2)
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
# plt.plot(np.random.randn(50).cumsum())
# plt.show()

## 라인스타일과 컬러 지정 (일반 방식)
# plt.plot(np.random.randn(50).cumsum(), linestyle="solid", color='skyblue')
# plt.plot(np.random.randn(50).cumsum(), linestyle="dashed", color='dodgerblue')
# plt.plot(np.random.randn(50).cumsum(), linestyle="dashdot", color='royalblue')
# plt.plot(np.random.randn(50).cumsum(), linestyle="dotted", color='navy')
# plt.show()

## 라인스타일과 컬러 한번에 지정
# plt.plot(np.random.randn(50).cumsum(), 'b-')
# plt.plot(np.random.randn(50).cumsum(), 'g--')
# plt.plot(np.random.randn(50).cumsum(), 'k-.')
# plt.plot(np.random.randn(50).cumsum(), 'y:')
# plt.show()

## 플롯 축 (plot axis)  - 가로, 세로 각각 설정
# plt.plot(np.random.randn(50), 'y:')
# plt.xlim(-10, 30)
# plt.ylim(-5, 5)
# plt.show()

## 플롯 축 (plot axis)  - 가로, 세로 한번에 설정
# plt.plot(np.random.randn(50), 'y:')
# plt.axis([-10, 30, -5, 5])   #[x의 시작, x의 끝, y의 시작, y의 끝]
# plt.show()

## 플롯 축 (plot axis)  - tight 설정
# plt.plot(np.random.randn(50), 'y:')
# plt.axis('tight')   #[x의 시작, x의 끝, y의 시작, y의 끝]
# plt.show()

## 플롯 축 (plot axis)  - equal 설정
# plt.plot(np.random.randn(50), 'y:')
# plt.axis('equal')   #[x의 시작, x의 끝, y의 시작, y의 끝]
# plt.show()


## 플롯 레이블 (plot label)
# plt.plot(np.random.randn(50).cumsum(), 'y-', label='A')
# plt.plot(np.random.randn(50).cumsum(), 'b-.', label='B')
# plt.plot(np.random.randn(50).cumsum(), 'r:', label='C')
# plt.legend()   # 복수의 표가 들어가고 각각 레이블 구분시 legend행 삽입
# plt.title("title")
# plt.xlabel("x")
# plt.ylabel("random.randn")
# plt.show()

## 폰트 관리자 (Font Manager)
# 기본 폰트 조회
# print(set([f.name for f in mpl.font_manager.fontManager.ttflist]))

# font1 = {'family' : 'Palace Script MT', 'size' : 24, 'color' : 'black'}
# font2 = {'family' : 'Microsoft JhengHei', 'size' : 10, 'weight' : 'bold', 'color' : 'blue'}
# font3 = {'family' : 'Times New Roman', 'size' : 30, 'weight' : 'light', 'color' : 'navy'}
#
# plt.plot(np.random.randn(50).cumsum(), 'y-', label='A')
# plt.plot(np.random.randn(50).cumsum(), 'b-.', label='B')
# plt.plot(np.random.randn(50).cumsum(), 'r:', label='C')
# plt.legend()   # 복수의 표가 들어가고 각각 레이블 구분시 legend행 삽입
# plt.title("title", fontdict=font3)
# plt.xlabel("x", fontdict=font2)
# plt.ylabel("random.randn", fontdict=font1)
# plt.show()

## 플롯 범례 (plot legend)

# fig, ax = plt.subplots()
# ax.plot(np.random.randn(10), '-r', label="AAA")
# ax.plot(np.random.randn(10), ':g', label="BBB")
# ax.plot(np.random.randn(10), ':y', label="CCC")
# ax.axis('equal')
# # ax.legend(loc='lower right')
# ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
# plt.show()


## 다중 플롯 (Multiple Subplots)
# ax1 = plt.axes()
# ax2 = plt.axes([0.6, 0.2, 0.2, 0.4])
# plt.show()

# for i in range(1, 10):
#     plt.subplot(3, 3, i)
#     plt.text(0.5, 0.5, str((3, 3, i)), ha='center')
# plt.show()

## 차트간 간격 조정
# fig = plt.figure()
# fig.subplots_adjust(hspace=0.4, wspace=0.4)
# for i in range(1, 10):
#     plt.subplot(3, 3, i)
#     plt.text(0.5, 0.5, str((3, 3, i)), ha='center')
# plt.show()

## 한번에 다중 차트 만들기
# fig, ax = plt.subplots(3, 3, sharex='col', sharey='row')
# # plt.show()
#
# for i in range(3):
#     for j in range(3):
#         ax[i, j].text(0.5, 0.5, str((i, j)), ha='center')
# plt.show()

## grid 조정하기
# grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.4)
# plt.subplot(grid[0,0])
# plt.subplot(grid[0,1:])
# plt.subplot(grid[1,:2])
# plt.subplot(grid[1,2])
# plt.show()

## 순차적으로 그래프 표현하기
plt.figure(figsize=(5, 6))
x = range(1, 21)
columns = [np.random.randn(20) * i for i in range(1, 7)]

i = 0
for c in columns:
    i += 1
    plt.subplot(3, 2, i)
    plt.plot(x, c, marker='o', linewidth=1, label=c)
    plt.xlim(-1, 21)
    plt.ylim(c.min()-1, c.max()+1)

plt.show()

## 50분 38초



