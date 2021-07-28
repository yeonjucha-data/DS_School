# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] colab_type="text" id="9Hzmex9EDwku"
# ## 지그재그의 데이터분석 팀에 오신 것을 환영합니다!
#
#
#
# <img src ="https://i.imgur.com/9zb1Cdh.jpg" width=700>
#
# (이 쥬피터 노트북은 다음의 링크 http://bit.ly/dsa-0302-ipynb 데이터는 http://bit.ly/dsa-03-zigzag 에서 다운받을 수 있습니다.)
#   
# 안녕하세요! [지그재그](https://zigzag.kr/) 데이터분석팀에 오신 것을 환영합니다.
#
# 지그재그는 여성 패션 쇼핑몰들의 상품 정보를 통합적으로 제공하는 플랫폼으로 개인 취향 알고리즘을 통해 적절한 제품을 추천하여 유저 경험을 높이고 있습니다. 지그재그는 2015년 6월 ‘내 스타일의 쇼핑몰을 편하게 북마크 해보자’라는 작은 아이디어에서 시작했습니다. 서비스가 출시되고 3년이 지난 지금, 지그재그에 입점한 2,700여 개의 온라인 쇼핑몰들에서는 하루에 10,000여 개의 패션 아이템이 업데이트되며 한 달에 200만 명이 넘는 사용자들이 방문해 자신이 좋아하는 상품을 실시간으로 발견하고 있습니다. 런칭 2년 반 만에 1,000만 앱 다운로드를 돌파하며 대한민국 여성의 쇼핑 필수 앱으로 자리 잡았습니다.
#
#
# <img src = "https://i.imgur.com/chOEQhY.jpg" width=250>
#
#  오늘 이 쥬피터 노트북을 받은 수강생분들께서는 지그재그의 일일 데이터 분석가(Data Analyst)로서 일을 할 것입니다. 지그재그의 하루 동안의 로그 데이터를 바탕으로 매출 분석 등 기본적인 데이터 탐색을 할 예정입니다. 일반적으로 매출 또는 핵심 지표에 영향을 미치는 요인에 대한 가설을 세우고 이를 데이터로 검증하는 일이 일반적인 데이터 분석이지만, 때로는 가설 없이 데이터 그 자체를 이해하는 것부터 출발하여 역으로 핵심 지표 또는 매출 등을 개선하기 위한 아이디어를 얻을 수도 있습니다. 이러한 데이터 자체를 이해하는 과정을 탐색적 자료 분석이라고 합니다. 여러분들은 6월 11일에 활동한 고객 정보, 쇼핑몰 정보, 거래 정보, 상품 정보, 그리고 고객의 행동 정보를 이해하고 분석하여 다른 팀들과 정보를 공유하게 될 것입니다.
#

# + [markdown] colab_type="text" id="Zx5CQ9YmDwk2"
# ---

# + [markdown] colab_type="text" id="oUjzdq-ADwk6"
# ## *set options

# + colab={} colab_type="code" id="m5iZh_KcDwk-"
import pandas as pd

# + colab={} colab_type="code" id="SqnKfnpvDwlV"
# 화면에 출력하는 데이터 프레임의 최대 row 수를 500으로 설정합니다.
pd.set_option('display.max_rows', 500)

# 화면에 출력하는 데이터 프레임의 최대 column 수를 500으로 설정합니다.
pd.set_option('display.max_columns', 500)

# + [markdown] colab_type="text" id="lAB_mchIDwll"
#  

# + [markdown] colab_type="text" id="ew-e5ZujDwlo"
# **1. data 폴더의 zigzag_DB.db에 연결한 뒤 데이터베이스 스키마를 출력해주세요. 그 다음,  order 테이블을 불러와주세요.**

# + [markdown] colab_type="text" id="CekalP6zDwlq"
# zigzag 데이터 테이블들을 모두 zigzag_DB.db 파일에 저장해두었습니다. 저번 주 수업자료를 참고해 database를 조회하고 그 중, order 테이블을 불러와주세요.

# + [markdown] colab_type="text" id="FAU-hXIWDwls"
# 로드한 테이블이 다음과 같은 모양이어야 합니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>timestamp</th>
#       <th>user_id</th>
#       <th>goods_id</th>
#       <th>shop_id</th>
#       <th>price</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>2018-06-11 00:00:43.032</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>1414</td>
#       <td>38</td>
#       <td>45000</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>2018-06-11 00:02:33.763</td>
#       <td>smDmRnykg61KajpxXKzQ0oNkrh2nuSBj</td>
#       <td>1351</td>
#       <td>12</td>
#       <td>9500</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>2018-06-11 00:04:06.364</td>
#       <td>EyGjKYtSqZgqJ1ddKCtH5XwGirTyOH2P</td>
#       <td>646</td>
#       <td>14</td>
#       <td>22000</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>2018-06-11 00:04:17.258</td>
#       <td>KQBGi33Zxh5Dgu0WEkOkjN0YqTT_wxC3</td>
#       <td>5901</td>
#       <td>46</td>
#       <td>29800</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>2018-06-11 00:05:26.010</td>
#       <td>lq1Je3voA3a0MouSFba3629lKCvweI24</td>
#       <td>5572</td>
#       <td>89</td>
#       <td>29000</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="GXOSy3tFDwlv"
# python에서 DB를 다루는 library인 sqlite3와 데이터를 다루는 library인 padas를 import합니다.
import pandas as pd
import sqlite3

# + colab={} colab_type="code" id="XQ4bTI8LDwmE"
connect = sqlite3.connect('zigzag_DB.db')
connect
# -

query = "select * from 'order'"
order = pd.read_sql(query, connect)
order.head()

order.info()

# + [markdown] colab_type="text" id="Xsrfka8JDwmc"
# order 테이블의 각 행은 주문이 일어난 로그를 나타내며, 2018년 6월 11일 하루치 데이터가 주어졌습니다.
#
# timestamp는 주문시각, user_id는 주문을 한 유저의 고유 아이디, goods_id는 상품의 id, shop_id는 쇼핑몰의 id, price는 상품의 가격을 나타냅니다.

# + [markdown] colab_type="text" id="VlYH9oESDwmf"
# **2. order 테이블을 이용해 지그재그의 당일 매출 상위 10개 쇼핑몰을 구해주세요.**

# + [markdown] colab_type="text" id="FHlN2PQLDwmh"
# order 테이블을 이용해 지그재그를 통해 이루어진 6월 11일의 쇼핑몰별 매출 정보를 피벗 테이블을 이용하여 구해주세요. 결과는 다음과 같이 나와야 합니다.

# + [markdown] colab_type="text" id="MsdUWlVeDwmk"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>price</th>
#     </tr>
#     <tr>
#       <th>shop_id</th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>22</th>
#       <td>1365200</td>
#     </tr>
#     <tr>
#       <th>14</th>
#       <td>872000</td>
#     </tr>
#     <tr>
#       <th>63</th>
#       <td>710700</td>
#     </tr>
#     <tr>
#       <th>32</th>
#       <td>707900</td>
#     </tr>
#     <tr>
#       <th>126</th>
#       <td>669400</td>
#     </tr>
#     <tr>
#       <th>6</th>
#       <td>655900</td>
#     </tr>
#     <tr>
#       <th>11</th>
#       <td>653000</td>
#     </tr>
#     <tr>
#       <th>60</th>
#       <td>558300</td>
#     </tr>
#     <tr>
#       <th>19</th>
#       <td>518400</td>
#     </tr>
#     <tr>
#       <th>12</th>
#       <td>446900</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="J4dIY2EzDwmn"
pd.pivot_table(order, index = 'shop_id', values = 'price', aggfunc = 'sum').sort_values(by='price', ascending = False).head(10)

# + [markdown] colab_type="text" id="XDexAuYTDwm8"
# **3. 판매 건수를 포함하여 피벗테이블을 만들어주세요. 또한, 상위 10개 쇼핑몰의 매출을 막대그래프로 보여주세요.**

# + [markdown] colab_type="text" id="Yz6nCx-ADwm-"
# 같은 횟수의 거래라도 제품의 가격이 비싸면 매출이 크게 나오게 되어있습니다. 상대적으로 저렴한 물품을 파는 쇼핑몰들은 결제 건수에 비해 매출이 적을 수 있습니다.
#
# 매출과 결제 건수를 함께 볼 수 있는 피벗테이블을 작성해주세요. 그리고, 그 결과를 막대그래프로 시각화하여 보여주세요. 결과는 다음과 같이 나오게됩니다.

# + [markdown] colab_type="text" id="jtYdR2wnDwnB"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>sum</th>
#       <th>count</th>
#     </tr>
#     <tr>
#       <th>shop_id</th>
#       <th></th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>22</th>
#       <td>1365200</td>
#       <td>99</td>
#     </tr>
#     <tr>
#       <th>14</th>
#       <td>872000</td>
#       <td>30</td>
#     </tr>
#     <tr>
#       <th>63</th>
#       <td>710700</td>
#       <td>27</td>
#     </tr>
#     <tr>
#       <th>32</th>
#       <td>707900</td>
#       <td>37</td>
#     </tr>
#     <tr>
#       <th>126</th>
#       <td>669400</td>
#       <td>39</td>
#     </tr>
#     <tr>
#       <th>6</th>
#       <td>655900</td>
#       <td>24</td>
#     </tr>
#     <tr>
#       <th>11</th>
#       <td>653000</td>
#       <td>19</td>
#     </tr>
#     <tr>
#       <th>60</th>
#       <td>558300</td>
#       <td>23</td>
#     </tr>
#     <tr>
#       <th>19</th>
#       <td>518400</td>
#       <td>19</td>
#     </tr>
#     <tr>
#       <th>12</th>
#       <td>446900</td>
#       <td>42</td>
#     </tr>
#   </tbody>
# </table>

# + [markdown] colab_type="text" id="pIliRr2oDwnE"
# ![](https://i.imgur.com/T6VRYf6.png)

# + colab={} colab_type="code" id="FXdpzFAZDwnI"
import matplotlib.pyplot as plt
import seaborn as sns

# + colab={} colab_type="code" id="nQ0uCa6BDwnd"
pt1 = pd.pivot_table(order, index = 'shop_id', values='price', aggfunc = ['sum','count']).sort_values(by=('sum', 'price'), ascending = False).head(10)
pt1.columns = ['sum','count']
pt1
# -

sns.barplot(data=pt1, x = pt1.index, y ='sum', order = pt1.index)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

# + [markdown] colab_type="text" id="JSEGTwtZDwnr"
# **4. 시간대별 지그재그 매출을 구하려고 합니다. lineplot을 이용하여 6월 11일의 시간대별 매출을 시각화 해주세요.**

# + [markdown] colab_type="text" id="H0ZPjjLMDwnv"
# 지그재그 이용자들의 구매 패턴을 알아보려고 합니다. timestamp를 to_datetime을 이용하여 datetime 자료형으로 만든 뒤, 이를 이용하여 시간대별 총 매출량을 구해주세요.
#
# x를 timestamp, y를 price로 놓는 경우 다음과 같은 그래프가 나오게 됩니다. 

# + [markdown] colab_type="text" id="jkA0FRFKDwn0"
# ![](https://i.imgur.com/5cqEAAj.png)

# + colab={} colab_type="code" id="Tn2diX0UDwn-"
import matplotlib as mpl

sns.set_style('whitegrid') #스타일은 원하는 것을 사용하세요.

mpl.rc('font', family='AppleGothic') # Mac의 경우는 AppleGothic, 윈도우의 경우는 Malgun Gothic을 사용하면 됩니다 :) 
mpl.rc('axes', unicode_minus=False)

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')
# -

order['timestamp'] = order['timestamp'].astype('datetime64')

plt.figure(figsize=(15,4))
sns.lineplot(data = order, x='timestamp',y='price')

# + [markdown] colab_type="text" id="5qwqltwtDwob"
# **5. 위의 시각화를 구간화(binning) 작업을 거쳐 보기 좋은 형태로 만들어주세요.**

# + [markdown] colab_type="text" id="jWPHBR3EDwod"
# 위의 시각화는 적절하지 못한 시각화입니다. 정확하게는 x시 00분 ~ x시 59분 까지의 매출을 시간대별로 모두 합하는 binning 과정을 거친 뒤 시각화를 진행해야 원하는 결과를 얻을 수 있습니다.
#
# order 테이블에 로그의 발생 시간을 나타내는 hour 칼럼을 추가한 뒤, pivot_table을 이용하여 시간대별 매출을 구해주세요. 그리고, 이를 이용해 아래와 같은 그래프를 만들어 주세요.

# + [markdown] colab_type="text" id="h12r819eDwof"
# *lineplot을 사용하는 경우*
# ![](https://i.imgur.com/sGVLJKi.png)
#
# *pointplot을 사용하는 경우*
# ![](https://i.imgur.com/hYuKVqE.png)

# + colab={} colab_type="code" id="bCQUTdlCDwoh"
order['hour'] = order['timestamp'].dt.hour
# -

pt2 = pd.pivot_table(data = order, index = 'hour', values = 'price', aggfunc = 'sum')

plt.figure(figsize=(14,4))
sns.lineplot(data = pt2)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

plt.figure(figsize=(14,4))
sns.pointplot(data = pt2, x = pt2.index, y ='price')
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

# + [markdown] colab_type="text" id="YNUH6KNXDwou"
# **6 . user 테이블을 불러와 order 테이블과 병합해주세요.**

# + [markdown] colab_type="text" id="1LibI5HADwov"
# user 테이블에는 고객의 고유 아이디를 나타내는 user_id, 그리고 접속 기기정보를 나타내는 os, 그리고 나이정보 age가 있습니다. 이를 이용해 top 10 쇼핑몰 매출이 어떤 연령층에서 발생했는지 분석하고자 합니다. 데이터베이스에서 user 테이블을 불러온 뒤, order 테이블과 병합해주세요.

# + [markdown] colab_type="text" id="AlMaQzVEDwox"
# 병합 결과는 다음과 같이 나오게 됩니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>timestamp</th>
#       <th>user_id</th>
#       <th>goods_id</th>
#       <th>shop_id</th>
#       <th>price</th>
#       <th>hour</th>
#       <th>os</th>
#       <th>age</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>2018-06-11 00:00:43.032</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>1414</td>
#       <td>38</td>
#       <td>45000</td>
#       <td>0</td>
#       <td>iOS</td>
#       <td>39</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>2018-06-11 00:02:33.763</td>
#       <td>smDmRnykg61KajpxXKzQ0oNkrh2nuSBj</td>
#       <td>1351</td>
#       <td>12</td>
#       <td>9500</td>
#       <td>0</td>
#       <td>And</td>
#       <td>17</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>2018-06-11 00:04:06.364</td>
#       <td>EyGjKYtSqZgqJ1ddKCtH5XwGirTyOH2P</td>
#       <td>646</td>
#       <td>14</td>
#       <td>22000</td>
#       <td>0</td>
#       <td>And</td>
#       <td>-1</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>2018-06-11 00:04:17.258</td>
#       <td>KQBGi33Zxh5Dgu0WEkOkjN0YqTT_wxC3</td>
#       <td>5901</td>
#       <td>46</td>
#       <td>29800</td>
#       <td>0</td>
#       <td>And</td>
#       <td>34</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>2018-06-11 00:05:26.010</td>
#       <td>lq1Je3voA3a0MouSFba3629lKCvweI24</td>
#       <td>5572</td>
#       <td>89</td>
#       <td>29000</td>
#       <td>0</td>
#       <td>And</td>
#       <td>17</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="Ows92XzVDwoz"
query = "select * from 'user'"
user = pd.read_sql(query, connect)
user.head()
# -

merged = pd.merge(order, user, on = 'user_id')

merged.head()

# + [markdown] colab_type="text" id="Gpb76LvTDwpA"
# **7. 매출 Top 10 쇼핑몰 구매자들의 연령대를 쇼핑몰별로 시각화하여 보여주세요.**

# + [markdown] colab_type="text" id="EXpglbBVDwpD"
# 위의 병합된 테이블을 이용하여, 당일 매출 Top 10 쇼핑몰에서 구매를 한 고객들의 연령대 분포를 시각화로 표현하고자 합니다. 이를 이용해 쇼핑몰이 설정한 타겟 연령대와 실제 구매층이 일치하는지를 비교해보고자 합니다.
#
# 나이 정보가 없는 경우는 -1이 입력되어 있기 때문에 이를 처리한 다음 시각화를 해야 합니다. 시각화 결과가 아래의 둘 중 하나가 나오게 해주세요.

# + [markdown] colab_type="text" id="HpgsISfzDwpF"
# ![](https://i.imgur.com/roHlnXi.png)
# -

idx1 = merged.groupby('shop_id')['price'].sum().sort_values(ascending = False).head(10).index

idx1 = idx1.sort_values()

# + colab={} colab_type="code" id="d4i0KtgoDwpH"
sns.boxplot(data = merged[merged['age']!=-1], x = 'shop_id', y = 'age', order = idx1);
# -

sns.violinplot(data = merged[merged['age']!=-1], x = 'shop_id', y = 'age', order = idx1);


# + [markdown] colab_type="text" id="4JE2pe5cDwpW"
# **8. user 테이블에 연령대를 나타내는 칼럼을 만들어주세요. 그리고 쇼핑몰이 설정한 타겟 연령대와 실제로 구매를 한 고객의 연령과 일치하는지를 검증해주세요.**

# + [markdown] colab_type="text" id="9dVu8SslDwpX"
# 지그재그의 쇼핑몰들은 아래의 필터에서 보여지는 것과 같이 타겟 연령대를 가지고 있습니다. 하지만, 실제 구매가 설정되어 있는 타겟 연령대에 맞게 이루어지는지 꾸준히 검증이 이루어져야 합니다. 유저에게 더 적합한 제품이나 쇼핑몰을 추천해주어 유저 경험 (UX)를 증진시키는 것은 추천 플랫폼에게 매우 중요한 요소이기 때문입니다.

# + [markdown] colab_type="text" id="Ep2dkPpCDwpa"
# <img src="https://i.imgur.com/HMd9xC2.jpg" width=300>

# + [markdown] colab_type="text" id="lGGsDpDTDwpf"
# 수행해야 할 작업은 총 3단계입니다.
#
#     1. 실제 나이를 바탕으로 user 테이블에 연령대 칼럼을 만들기
#     2. shop 테이블을 불러와 user, order 테이블과 병합하기
#     3. 쇼핑몰의 타겟 연령대와 해당 쇼핑몰에서의 결제를 한 고객의 연령대를 비교하기

# + [markdown] colab_type="text" id="-yzhZai7Dwph"
# 아래의 함수를 이용해 user 테이블에 연령대를 만들어주세요.

# + colab={} colab_type="code" id="ETW7piBTDwpj" outputId="3e7bcab8-36f0-4b45-b83d-983bcebf7439"
def make_generation(age):
    if age == -1:
        return '미입력'
    elif age // 10 >= 4:
        return "30대 후반"
    elif age // 10 == 1:
        return "10대"
    elif age % 10 < 3:
        return str(age // 10 * 10) + f"대 초반"
    elif age % 10 <= 6:
        return str(age // 10 * 10) + f"대 중반"
    else:
        return str(age // 10 * 10) + f"대 후반"

    
print(make_generation(10))
print(make_generation(23))
print(make_generation(29))
print(make_generation(32))
print(make_generation(35))
print(make_generation(40))

# + colab={} colab_type="code" id="n3N4xec_Dwpz"
user['연령대'] = user['age'].apply(make_generation)
# -

user.head(1)

# + [markdown] colab_type="text" id="qWTCpq49Dwp9"
# shop 테이블을 DB에서 불러와 주세요. 그 다음, user, order 테이블과 병합해주세요.

# + [markdown] colab_type="text" id="hVlUKXV1Dwp_"
# 병합 결과는 다음과 같게 됩니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>timestamp</th>
#       <th>user_id</th>
#       <th>goods_id</th>
#       <th>shop_id</th>
#       <th>price</th>
#       <th>hour</th>
#       <th>os</th>
#       <th>age_x</th>
#       <th>연령대</th>
#       <th>name</th>
#       <th>category</th>
#       <th>age_y</th>
#       <th>style</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>2018-06-11 00:00:43.032</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>1414</td>
#       <td>38</td>
#       <td>45000</td>
#       <td>0</td>
#       <td>iOS</td>
#       <td>39</td>
#       <td>30대 후반</td>
#       <td>Mabel</td>
#       <td>의류</td>
#       <td>20대 후반/30대 초반/30대 중반</td>
#       <td>모던시크/페미닌</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>2018-06-11 07:33:39.823</td>
#       <td>ni3NQK35j-YaSxli-C_Sz7ZmQqOwMljL</td>
#       <td>2278</td>
#       <td>38</td>
#       <td>37000</td>
#       <td>7</td>
#       <td>And</td>
#       <td>32</td>
#       <td>30대 초반</td>
#       <td>Mabel</td>
#       <td>의류</td>
#       <td>20대 후반/30대 초반/30대 중반</td>
#       <td>모던시크/페미닌</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>2018-06-11 12:56:27.867</td>
#       <td>MnvhmV0tA89bN9TLXgRTbLza689bTkT9</td>
#       <td>5513</td>
#       <td>38</td>
#       <td>31000</td>
#       <td>12</td>
#       <td>And</td>
#       <td>37</td>
#       <td>30대 후반</td>
#       <td>Mabel</td>
#       <td>의류</td>
#       <td>20대 후반/30대 초반/30대 중반</td>
#       <td>모던시크/페미닌</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>2018-06-11 22:57:11.582</td>
#       <td>3Vo9NP0qU_176pgbqk6Cu-CY7kpJ2-WB</td>
#       <td>7026</td>
#       <td>38</td>
#       <td>17100</td>
#       <td>22</td>
#       <td>iOS</td>
#       <td>34</td>
#       <td>30대 중반</td>
#       <td>Mabel</td>
#       <td>의류</td>
#       <td>20대 후반/30대 초반/30대 중반</td>
#       <td>모던시크/페미닌</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>2018-06-11 00:02:33.763</td>
#       <td>smDmRnykg61KajpxXKzQ0oNkrh2nuSBj</td>
#       <td>1351</td>
#       <td>12</td>
#       <td>9500</td>
#       <td>0</td>
#       <td>And</td>
#       <td>17</td>
#       <td>10대 후반</td>
#       <td>Rachel</td>
#       <td>의류</td>
#       <td>10대/20대 초반</td>
#       <td>러블리/심플베이직</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="tdL8kajCDwqB"
query = "select * from 'shop'"
shop = pd.read_sql(query, connect)
shop.head(1)
# -

tmp = pd.merge(order, user, on = 'user_id')

tot_merged = pd.merge(tmp, shop, on = 'shop_id')
tot_merged.head()


# + [markdown] colab_type="text" id="DgSuuJeLDwqL"
# 병합한 테이블을 이용하여 '거래연령 일치여부' 칼럼을 아래의 칼럼을 이용하여 만들어 주세요. 각 열이 아닌 각 행에 함수를 적용할 때는 `apply(function, axis=1)`을 이용해야 합니다.

# + colab={} colab_type="code" id="J8SpQqOMDwqO"
def check_generation(row):
    if row['category'] == '의류' and row['연령대'] == '미입력':
        return True
    else:
        return row['연령대'] in str(row['age_y'])


# -

tot_merged['거래연령 일치여부'] = tot_merged.apply(check_generation, axis = 1)

# + [markdown] colab_type="text" id="KA1gGiSfDwqd"
# 피벗 테이블을 이용한 결과가 다음과 같이 나오게 됩니다.

# + [markdown] colab_type="text" id="qkeQQH8vDwqh"
# <table border="1" class="dataframe">
#   <thead>
#     <tr>
#       <th></th>
#       <th>mean</th>
#       <th>count</th>
#     </tr>
#     <tr>
#       <th></th>
#       <th>거래연령 일치여부</th>
#       <th>거래연령 일치여부</th>
#     </tr>
#     <tr>
#       <th>shop_id</th>
#       <th></th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>1</th>
#       <td>0.666667</td>
#       <td>3</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>0.937500</td>
#       <td>16</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>0.400000</td>
#       <td>5</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>1.000000</td>
#       <td>1</td>
#     </tr>
#     <tr>
#       <th>5</th>
#       <td>0.000000</td>
#       <td>1</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="wC-0cX03Dwqj"
pt1 = pd.pivot_table(data = tot_merged, index = 'shop_id', values = '거래연령 일치여부', aggfunc = ['mean', 'count'])
pt1.head()
# -

pt1[pt1.index.isin(idx1)]

# + [markdown] colab_type="text" id="Coz7uhRVDwqx"
# 위의 정보를 Top 10 쇼핑몰에 대해 뽑아보면 다음과 같은 결과가 나옵니다. 

# + [markdown] colab_type="text" id="zJ1f7yjqDwqz"
# `table[table.index.isin(top10_index)]`
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr>
#       <th></th>
#       <th>mean</th>
#       <th>count</th>
#     </tr>
#     <tr>
#       <th></th>
#       <th>거래연령 일치여부</th>
#       <th>거래연령 일치여부</th>
#     </tr>
#     <tr>
#       <th>shop_id</th>
#       <th></th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>6</th>
#       <td>0.750000</td>
#       <td>24</td>
#     </tr>
#     <tr>
#       <th>11</th>
#       <td>0.684211</td>
#       <td>19</td>
#     </tr>
#     <tr>
#       <th>12</th>
#       <td>0.857143</td>
#       <td>42</td>
#     </tr>
#     <tr>
#       <th>14</th>
#       <td>0.566667</td>
#       <td>30</td>
#     </tr>
#     <tr>
#       <th>19</th>
#       <td>0.789474</td>
#       <td>19</td>
#     </tr>
#     <tr>
#       <th>22</th>
#       <td>0.929293</td>
#       <td>99</td>
#     </tr>
#     <tr>
#       <th>32</th>
#       <td>0.540541</td>
#       <td>37</td>
#     </tr>
#     <tr>
#       <th>60</th>
#       <td>0.695652</td>
#       <td>23</td>
#     </tr>
#     <tr>
#       <th>63</th>
#       <td>0.000000</td>
#       <td>27</td>
#     </tr>
#     <tr>
#       <th>126</th>
#       <td>0.000000</td>
#       <td>39</td>
#     </tr>
#   </tbody>
# </table>

# + [markdown] colab_type="text" id="apTtU5RJDwq1"
# 의류이외의 제품을 파는 쇼핑몰은 타겟 연령층이 없기 떄문에 일치여부가 0이 나옵니다. 일치여부가 낮은 쇼핑몰의 경우는 더 긴 기간의 로그를 모니터링 한 다음, 태그 수정을 제안하여 타겟 적합도를 높일 수 있습니다.

# + [markdown] colab_type="text" id="KAM81IsfDwq3"
# **9. 쇼핑몰의 스타일 태그를 정리해주세요.**

# + [markdown] colab_type="text" id="MVJ4RmhjDwq5"
# 쇼핑몰별로 제품군의 스타일을 나타낼 수 있는 태그를 가지고 있습니다. 이 태그는 다음의 리스트에 정리되어 있습니다.

# + colab={} colab_type="code" id="eBcahla3Dwq6"
style_list = ['페미닌', '모던시크', '심플베이직', '러블리', '유니크', '미시스타일', '캠퍼스룩', '빈티지', '섹시글램', '스쿨룩', '로맨틱', '오피스룩',
              '럭셔리', '헐리웃스타일', '심플시크', '키치', '펑키', '큐티', '볼드&에스닉' ]

# + [markdown] colab_type="text" id="_LcmRGmXDwrF"
# 위의 스타일을 정리하여 shop 테이블을 전처리해 아래와 같은 테이블을 만들어주세요.

# + [markdown] colab_type="text" id="DLNAL9qhDwrH"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>name</th>
#       <th>category</th>
#       <th>age</th>
#       <th>style</th>
#       <th>페미닌</th>
#       <th>모던시크</th>
#       <th>심플베이직</th>
#       <th>러블리</th>
#       <th>유니크</th>
#       <th>미시스타일</th>
#       <th>캠퍼스룩</th>
#       <th>빈티지</th>
#       <th>섹시글램</th>
#       <th>스쿨룩</th>
#       <th>로맨틱</th>
#       <th>오피스룩</th>
#       <th>럭셔리</th>
#       <th>헐리웃스타일</th>
#       <th>심플시크</th>
#       <th>키치</th>
#       <th>펑키</th>
#       <th>큐티</th>
#       <th>볼드&amp;에스닉</th>
#     </tr>
#     <tr>
#       <th>shop_id</th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>1</th>
#       <td>Edna</td>
#       <td>의류</td>
#       <td>20대 중반/20대 후반/30대 초반</td>
#       <td>모던시크/러블리</td>
#       <td>False</td>
#       <td>True</td>
#       <td>False</td>
#       <td>True</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>Pam</td>
#       <td>의류</td>
#       <td>20대 중반/20대 후반/30대 초반</td>
#       <td>러블리/심플베이직</td>
#       <td>False</td>
#       <td>False</td>
#       <td>True</td>
#       <td>True</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>Carolyn</td>
#       <td>의류</td>
#       <td>20대 중반/20대 후반/30대 초반</td>
#       <td>모던시크/심플베이직</td>
#       <td>False</td>
#       <td>True</td>
#       <td>True</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#     </tr>
#   </tbody>
# </table>

# + [markdown] colab_type="text" id="xT9dQ3iRDwrK"
# 예를 들어 shop_id가 1인 쇼핑몰의 스타일이 `모던시크/러블리`인 경우 모던시크 칼럼과 러블리 칼럼은 True 값을 가지고 나머지 칼럼은 False의 값을 가집니다.
# -

for style in style_list:
        shop[style] = shop['style'].str.contains(style)

shop.head()

# + [markdown] colab_type="text" id="JHzBdmAXDwrY"
# **10. 스타일별 실제 구매 기록을 바탕으로 가장 구매가 많이 일어난 스타일 키워드를 찾아주세요. 또한, 매출이 가장 많은 3가지 스타일의 구매 연령대 분포를 그려주세요.**
#

# + [markdown] colab_type="text" id="wcO7PPe6Dwra"
# 위에서 전처리한 스타일을 이용하기 위해 order, shop, user 테이블을 다시 테이블을 병합하도록 하겠습니다.

# + colab={} colab_type="code" id="4n00o36oDwrc" outputId="3dba1afc-ed9b-46d9-b009-d3250428b8d1"
merged = (
    order.merge(shop, on='shop_id')
             .merge(user, on='user_id')
)
print(merged.shape)
merged.head(3)

# + [markdown] colab_type="text" id="2RAP8TVxDwrs"
# 위의 merged table을 이용하여 다음과 같은 그래프가 나오게 해주세요.

# + [markdown] colab_type="text" id="d-X7yQooDwrt"
#
#
# <img src="https://i.imgur.com/T4a4atS.png" width=800>

# + colab={} colab_type="code" id="OdEpEDWcDwrw"
merged[style_list].sum().sort_values(ascending =False)
# -

plt.rcParams['font.family']='NaNumGothic'
plt.figure(figsize = (10,4))
sns.distplot(merged.loc[merged['심플베이직']==True, 'age_y'], color = 'blue', label = '심플베이직', hist =False)
sns.distplot(merged.loc[merged['러블리']==True, 'age_y'], color = 'orange', label = '러블리', hist =False)
sns.distplot(merged.loc[merged['모던시크']==True, 'age_y'], color = 'green', label = '모던시크', hist =False);

# + [markdown] colab_type="text" id="croXBQ1KDwsD"
# **11. DB에서 로그 데이터를 불러온 다음 timestamp 컬럼을 datetime 형식으로 바꿔주세요. 그리고 user id를 보기 쉽게 간단한 자연수 형태로 변환해주세요.**

# + colab={} colab_type="code" id="QNoRmjIDDwsK"
query = "select * from 'log'"
log = pd.read_sql(query, connect)
log.head()
# -

log = log.sort_values(['user_id','timestamp']).reset_index(drop=True)

# + [markdown] colab_type="text" id="K9667Sp_Dwsa"
# 지그재그 로그 데이터의 명세는 다음과 같습니다.
#
#
#     - 컬럼 별 명세
#         1. timestamp : 이벤트 발생 시간 (한국 시간 기준)
#         2. user_id : 이용자 고유 식별자
#         3. event_origin : 이벤트가 발생한 앱 위치
#             - event_origin 값 별 의미
#                 a. goods_search_result : 특정 검색어의 상품 검색 결과
#                     (Ex: goods_search_result/반팔티)
#                 b. shops_ranking : '쇼핑몰 랭킹' 영역
#                 c. shops_bookmark : '즐겨찾기' 영역
#                 d. category_search_result : 카테고리 검색 결과 
#                     (Ex:category_search_result/상의)
#                 e. my_goods : '내 상품' 영역
#                 
#         4. event_name : 발생한 이벤트 명
#             - event_name 값 별 의미
#                 a. app_page_view : 앱 내 화면 이동
#                 b. enter_browser : 앱 내 클릭을 통해, 특정 웹페이지로 진입
#                 c. add_bookmark : 특정 쇼핑몰을 즐겨찾기 추가
#                 d. remove_bookmark : 특정 쇼핑몰을 즐겨찾기 제거
#                 e. add_my_goods : 특정 상품을 내 상품 추가
#                 f. remove_my_goods : 특정 상품을 내 상품 제거
#                 
#         5. event_goods_id : 이벤트가 발생한 상품 고유 식별자
#              - 상품 관련 이벤트가 아닌 경우, 공백
#              
#         6. event_shop_id : 이벤트가 발생한 쇼핑몰 고유 식별자
#              - 쇼핑몰 관련 이벤트가 아닌 경우, 공백
#
#

# + [markdown] colab_type="text" id="TUjLF7BXDwsc"
# user_id는 아래에서 확인할 수 있듯이 매우 복잡한 형태로 되어 있어 한눈에 파악하기 어렵습니다.
#
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>user_id</th>
#       <th>os</th>
#       <th>age</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>--PYPMX8QWg0ioT5zfORmU-S5Lln0lot</td>
#       <td>And</td>
#       <td>41</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>-16-xXbeDcvkZJtTpRwMi57Yo2ZQpORv</td>
#       <td>iOS</td>
#       <td>31</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>-1de9sT-MLwVVvnC0ncCLnqEqpSi3XSN</td>
#       <td>iOS</td>
#       <td>16</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>-3A3L2jnM55B_Q1bRXMjZ6sPnINIj-Y1</td>
#       <td>And</td>
#       <td>41</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>-3bhcSgPOIdQAPkPNcchxvECGqGQQ78k</td>
#       <td>And</td>
#       <td>42</td>
#     </tr>
#   </tbody>
# </table>
#
#
#

# + [markdown] colab_type="text" id="n6yGLTk3Dwse"
# 앞으로의 분석을 용이하게 하기위하여 user_id을 간단하게 0, 1, 2, 3 ...과 같이 연속된 정수 형태로 아래와 같이 변환하겠습니다.

# + [markdown] colab_type="text" id="ITC71hmFDwsg"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>user_id</th>
#       <th>n_user_id</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>K1d8_t3-QIskaSkrx32oAFu856D8JmLo</td>
#       <td>3314</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>lwFZ77v_ygk0uU40t1ud3l30EZ6sE2R3</td>
#       <td>7844</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>mR-bO6hC9g-m8ERXMRQZaRwJFvzNNdd8</td>
#       <td>7920</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>K1d8_t3-QIskaSkrx32oAFu856D8JmLo</td>
#       <td>3314</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>Yjny5AchUWLiuv4kdeq50COF-S8OFXPd</td>
#       <td>5608</td>
#     </tr>
#     <tr>
#       <th>5</th>
#       <td>LZZ0ktGq6hW685TFAQfcGNhsKVUEceHl</td>
#       <td>3548</td>
#     </tr>
#     <tr>
#       <th>6</th>
#       <td>TUoAGIbbNds5cYLZLnz-R5VlkG5L8RuZ</td>
#       <td>4790</td>
#     </tr>
#     <tr>
#       <th>7</th>
#       <td>B9F_BHH9F3b6MW329go9jDr71Uunx629</td>
#       <td>1902</td>
#     </tr>
#     <tr>
#       <th>8</th>
#       <td>e_xrTZ9fHVodxxadLx688qUKMWCdL8bW</td>
#       <td>6663</td>
#     </tr>
#     <tr>
#       <th>9</th>
#       <td>aA9S7LxnFm6ym6IUEa-4SSxJa-iL5m2J</td>
#       <td>5976</td>
#     </tr>
#   </tbody>
# </table>

# + [markdown] colab_type="text" id="Z4iiJFrTDwsi"
# 기존의 고객 아이디와 새롭게 만들 고객 아이디를 짝지어 딕셔너리로 만들고 이를 mapping하여 진행을 할 것입니다.

# + colab={} colab_type="code" id="0iQeN1YuDwsl"
# 판다스의 unique() 기능을 이용하여 유저 아이디를 user_id라는 변수에 저장합니다.

user_id = log['user_id'].unique()

# + colab={} colab_type="code" id="shqJrah2DwtD"
#새로운 user_id는 연속된 자연수들로 지정합니다. range()와 len()을 사용하여 user_id의 개수만큼의 연속된 정수를 만듭니다.

n_user_id = [i for i in range(len(user_id))]

# + colab={} colab_type="code" id="Hq3C61yYDwte" outputId="c5feec68-a210-4bd0-fc07-b4e9d91549ab"
#python 내장 함수인 zip()을 이용하여 기존의 id와 새로운 id를 묶습니다.
id_zip = zip(user_id, n_user_id)

#id_zip을 출력하면 아래 결과와 같이 zip object이 출력됩니다.
print(id_zip)

# + colab={} colab_type="code" id="GbL1zbPdDwtz" outputId="4861ee74-02e3-4eac-c19b-b47a72632be0"
#zip()의 결과를 구체적으로 보기 위하여 list로 변환하여 print하겠습니다. 상위 5개만 출력합니다.
list(zip(user_id, n_user_id))[:5]


# + colab={} colab_type="code" id="kd67iaEXDwuH" outputId="3221c967-759c-4f85-e41d-be4c39ca6279"
#새로운 id와 기존의 id가 대응된 딕셔너리 타입 변수를 생성합니다.
id_dict = dict(id_zip)

id_dict

# + [markdown] colab_type="text" id="PpEfQ7nXDwuZ"
# mapping 후 data_logs user_id, n_user_id 결과는 아래와 같습니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>user_id</th>
#       <th>n_user_id</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>K1d8_t3-QIskaSkrx32oAFu856D8JmLo</td>
#       <td>3314</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>lwFZ77v_ygk0uU40t1ud3l30EZ6sE2R3</td>
#       <td>7844</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>mR-bO6hC9g-m8ERXMRQZaRwJFvzNNdd8</td>
#       <td>7920</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>K1d8_t3-QIskaSkrx32oAFu856D8JmLo</td>
#       <td>3314</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>Yjny5AchUWLiuv4kdeq50COF-S8OFXPd</td>
#       <td>5608</td>
#     </tr>
#   </tbody>
# </table>
#
#
#
# **Hint) mapping 예시**
#
# ```
# data['column'].map(dict)
# ```

# + colab={} colab_type="code" id="NnuwEQiCDwub"
# data_logs, order, user에 id_idct를 mapping하여 각 데이터 프레임에 새로운 고객 id컬럼인 n_user_id를 만듭니다.
# Write your code here! (3 lines)
log['n_user_id'] = log['user_id'].map(id_dict)
order['n_user_id'] = order['user_id'].map(id_dict)
user['n_user_id'] = user['user_id'].map(id_dict)


# 결과를 확인합니다.
log[['user_id', 'n_user_id']].head()

# + [markdown] colab_type="text" id="HK33c7SVDwuk"
#  **12. 주문 데이터, 로그 데이터를 concat해주세요.**

# + [markdown] colab_type="text" id="YaWVuMyjDwum"
# 주문기록은 user_event_log에 기록되지 않습니다. 이는 바로 뒤에서 확인할 수 있습니다. 이를 확인하고 concat해야 되는 이유를 살펴보겠습니다.

# + colab={} colab_type="code" id="sR_b10O-Dwup" outputId="5b42d79d-4fc0-4321-81d0-4e61697c54d5"
#주문 데이터의 첫번째 row를 출력합니다.
order.iloc[0]

# + [markdown] colab_type="text" id="98eZgHbMDwu-"
# 위의 user_id에 해당하는 고객의 log기록을 가져와주세요. 결과는 아래와 같습니다. 
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>timestamp</th>
#       <th>user_id</th>
#       <th>event_origin</th>
#       <th>event_name</th>
#       <th>event_goods_id</th>
#       <th>event_shop_id</th>
#       <th>n_user_id</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>878</th>
#       <td>2018-06-11 00:06:45.357</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>901</th>
#       <td>2018-06-11 00:06:54.034</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨바지</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>1062</th>
#       <td>2018-06-11 00:08:00.579</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨바지</td>
#       <td>enter_browser</td>
#       <td>2048.0</td>
#       <td>46.0</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>1259</th>
#       <td>2018-06-11 00:09:38.881</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨바지</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>1439</th>
#       <td>2018-06-11 00:11:04.446</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨바지</td>
#       <td>enter_browser</td>
#       <td>3486.0</td>
#       <td>38.0</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>1473</th>
#       <td>2018-06-11 00:11:20.354</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨바지</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>1526</th>
#       <td>2018-06-11 00:11:48.284</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨바지</td>
#       <td>enter_browser</td>
#       <td>4006.0</td>
#       <td>24.0</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>2423</th>
#       <td>2018-06-11 00:18:21.906</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨바지</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>2529</th>
#       <td>2018-06-11 00:19:01.928</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>goods_search_result/린넨</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>2758</th>
#       <td>2018-06-11 00:20:30.432</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>shops_bookmark</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>4502</th>
#       <td>2018-06-11 00:32:29.738</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>shops_bookmark</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#     <tr>
#       <th>5156</th>
#       <td>2018-06-11 00:37:22.757</td>
#       <td>bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx</td>
#       <td>shops_bookmark</td>
#       <td>app_page_view</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>6241</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="0H_6NQJnDwvG"
log[log['user_id']=='bvu0aLTqiFDoU-963xnr5nzQWTNLUMjx']

# + [markdown] colab_type="text" id="WD5a8w8XDwvi"
# 00시 37분에 마지막 log가 기록되어 있습니다. 이 기록을 바탕으로 해당 고객은 쇼핑몰 즐겨찾기 목록에서 특정 쇼핑몰을 클릭하여 들어간다음 43분에 린넨바지를 구매한 것을 유추할 수 있습니다. 
#
# logs 테이블에 존재하는 기록들은 위와 같이 기록이 되어 있습니다. 사람들이 구매를 하도록 유도하는 것이 최종 목표이기 때문에, 로그기록과 구매기록을 연결하는 것은 매우 중요합니다. 하지만, 로그 테이블에는 이 사람이 구매를 했는지에 대한 정보가 전혀 없기 때문에 order 테이블과 log 테이블을 병합해야할 필요가 있습니다. 이를 `pd.concat()` 을 이용하여 병합하도록 하겠습니다.
#
# 기록 중에, 주문을 했지만 그 전의 로그 정보가 전혀 없는 고객들이 있습니다. 시간 대를 살펴봤을 때, 이들은 전날에 로그 기록이 존재하고 6월 11일 자정 이후 결제를 한 것으로 추론됩니다. 이들은 잔존 시간을 계산하는데 오류를 일으키므로 이들을 제외하고 concat 하도록 하겠습니다.

# + [markdown] colab_type="text" id="5RtuqzpJDwvk"
#  

# + [markdown] colab_type="text" id="a5IWFMTIDwvn"
# 로그 데이터와 주문 데이터에 동시에 기록된 고객을 구하겠습니다.
#
# 데이터를 집합(set)으로 변환하면 중복된 원소들은 1개만 남고 제거됩니다. unique() 메서드의 결과와 같다고 생각하시면 됩니다. 이를 이용하겠습니다.
#  
# 코드예시는 아래와 같습니다. 아래의 예시를 활용해 주세요.
#
# ```
# #집합 타입으로 변환하는 코드입니다.
# set(data['column'])
#
# #집합의 원소의 개수를 반환하는 코드입니다.
# len(set(data['column']))
#
# #두 집합의 공통된 원소들의 집합을 반환하는 코드입니다.
# set(data1['column']) & set(data2['column'])
# ```
#

# + [markdown] colab_type="text" id="cgIGGgwtDwvp"
# 아래 코드를 실행할 시 출력 결과는 다음과 같이 나오게 됩니다.
# ```
# 해당 날짜에 구매한 총 고객수 입니다 : 832명
# 해당 날짜 log데이터에 기록된 총 고객수입니다 : 9909명
# 중복되는 고객수입니다 : 742명
# ```

# + colab={} colab_type="code" id="6pn0fA_CDwvq"
# set()을 사용하여 user_id컬럼을 집합 타입으로 변환후 원소 개수를 반환하여 변수에 저장해주세요.

# 주문한 고객의 수를 user_number_order란 변수에 저장해주세요.

user_number_order = len(set(order['user_id']))

# log에 기록된 고객의 수를 user_number_log란 변수에 저장해주세요.

user_number_log = len(set(log['user_id']))


# 중복된 고객들을 user_duplicated란 변수에 저장해주세요.

user_duplicated = set(order['user_id']) & set(log['user_id'])


# 결과를 출력합니다.
print('해당 날짜에 구매한 총 고객수 입니다 :',user_number_order, end ='명\n')
print('해당 날짜 log데이터에 기록된 총 고객수입니다 :',user_number_log,  end ='명\n')
print('중복되는 고객수입니다 :', len(user_duplicated) , end ='명\n')

# + [markdown] colab_type="text" id="n_cDsrnIDwwA"
# 중복되는 고객의 목록을 구하였으므로 이제는 두 데이터들을 concat하기 위해 column명을 동일하게 맞추겠습니다.
#
# order, data_logs의 column을 확인합니다.

# + colab={} colab_type="code" id="sSxDo1lRDwwD" outputId="57ee3eb7-38d8-469e-b6fc-43024ba988a2"
print(order.columns)
print(log.columns)

# + [markdown] colab_type="text" id="Ov5_Zdn1DwwV"
# data_logs의 columns을 기준으로 병합할 것입니다. 따라서 order의 columns을 data_logs에 맞춰 변형합니다.

# + colab={} colab_type="code" id="PROzKk1HDwwX"
# order 원본을 변형하지 않기 위해 order을 copy하여 사용합니다. 
order_copy = order.copy()

# + colab={} colab_type="code" id="Dy9HLnwgDwww" outputId="748cd878-280b-4157-e15c-3f88254178d1"
# 겹치는 유저만으로 data를 indexing합니다. user_duplicated 이용합니다. 
# isin을 이용한 indexing은 뒤의 문제에서도 많이 나오기 때문에 유심히 봐두시면 유용합니다.
order_copy = order_copy[order_copy['user_id'].isin(user_duplicated)]

#  event_origin 컬럼에는 shop_id 컬럼을 저장합니다.
order_copy['event_origin'] = order_copy['shop_id']

#  event_name 컬럼에는 'purchase'를 저장합니다.
order_copy['event_name'] = 'purchase'

# event_goods_id 컬럼에는 good_id 컬럼를 저장합니다.
order_copy['event_goods_id'] = order_copy['goods_id']

# 사용할 columns를 설정합니다.
order_copy = order_copy[['timestamp', 'n_user_id', 'user_id','event_origin',
         'event_name', 'event_goods_id', 'price']]

order_copy.head()


# + colab={} colab_type="code" id="KLpLE1v2DwxF"
# data_logs, order_copy를 concat 해주하여 다시 log_order에 저장해주세요.

log_order = pd.concat([log, order_copy], axis = 0)
log_order.head(3)
# -

log_order['n_user_id'] = log_order['n_user_id'].astype('int64')

# + [markdown] colab_type="text" id="AxHXrIdYDwxU"
# ----

# + [markdown] colab_type="text" id="zUuPyVp5DwxW"
#  log_order에 구매기록여부 컬럼인 purchase 컬럼을 만들어주세요.
#  
#  price컬럼과 notnull()을 이용해주세요. 
#  
#  출력 결과는 아래와 같습니다.
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>event_goods_id</th>
#       <th>event_name</th>
#       <th>event_origin</th>
#       <th>event_shop_id</th>
#       <th>n_user_id</th>
#       <th>price</th>
#       <th>timestamp</th>
#       <th>user_id</th>
#       <th>purchase</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>shops_ranking</td>
#       <td>NaN</td>
#       <td>3314</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:00:00.213</td>
#       <td>K1d8_t3-QIskaSkrx32oAFu856D8JmLo</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>shops_bookmark</td>
#       <td>NaN</td>
#       <td>7844</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:00:00.810</td>
#       <td>lwFZ77v_ygk0uU40t1ud3l30EZ6sE2R3</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>goods_search_result/로브</td>
#       <td>NaN</td>
#       <td>7920</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:00:00.956</td>
#       <td>mR-bO6hC9g-m8ERXMRQZaRwJFvzNNdd8</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>shops_bookmark</td>
#       <td>NaN</td>
#       <td>3314</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:00:01.084</td>
#       <td>K1d8_t3-QIskaSkrx32oAFu856D8JmLo</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>shops_bookmark</td>
#       <td>NaN</td>
#       <td>5608</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:00:01.561</td>
#       <td>Yjny5AchUWLiuv4kdeq50COF-S8OFXPd</td>
#       <td>False</td>
#     </tr>
#   </tbody>
# </table>
#

# + colab={} colab_type="code" id="m5YCdITYDwxZ"
log_order['purchase'] = log_order['price'].notnull()
# -

log_order= log_order[['event_goods_id','event_name','event_origin','event_shop_id','n_user_id','price','timestamp','user_id','purchase']]
log_order.head()

# + [markdown] colab_type="text" id="SmzQ1uJkDwxv"
# ----

# + [markdown] colab_type="text" id="k3VhLlXUDwxz"
# 데이터를 파악하기 쉽게 하기 위해 user_id, timestamp 컬럼을 기준으로 log_order를 정렬해주세요.
#
# sort_values()를 사용해주시고 reset_index()를 통해 index를 정리해주세요.
#
# 출력 결과는 아래와 같습니다.

# + [markdown] colab_type="text" id="XwD5G3sNDwx2"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>event_goods_id</th>
#       <th>event_name</th>
#       <th>event_origin</th>
#       <th>event_shop_id</th>
#       <th>n_user_id</th>
#       <th>price</th>
#       <th>timestamp</th>
#       <th>user_id</th>
#       <th>purchase</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>shops_bookmark</td>
#       <td>NaN</td>
#       <td>0</td>
#       <td>NaN</td>
#       <td>2018-06-11 15:57:10.615</td>
#       <td>--PYPMX8QWg0ioT5zfORmU-S5Lln0lot</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>shops_bookmark</td>
#       <td>NaN</td>
#       <td>0</td>
#       <td>NaN</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>--PYPMX8QWg0ioT5zfORmU-S5Lln0lot</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>my_goods</td>
#       <td>NaN</td>
#       <td>1</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:55:37.309</td>
#       <td>-16-xXbeDcvkZJtTpRwMi57Yo2ZQpORv</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>2506.0</td>
#       <td>enter_browser</td>
#       <td>my_goods</td>
#       <td>40.0</td>
#       <td>1</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>-16-xXbeDcvkZJtTpRwMi57Yo2ZQpORv</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>my_goods</td>
#       <td>NaN</td>
#       <td>1</td>
#       <td>NaN</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>-16-xXbeDcvkZJtTpRwMi57Yo2ZQpORv</td>
#       <td>False</td>
#     </tr>
#   </tbody>
# </table>
#

# + colab={} colab_type="code" id="3qeCX_sZDwx6"
log_order = log_order.sort_values(['user_id','timestamp']).reset_index(drop=True)
log_order.head()

# + [markdown] colab_type="text" id="YTa_6A9qDwyQ"
# **13. 동일한 사용자에 대한 연속한 로그들 사이의 시간 간격을 구해주세요.**

# + [markdown] colab_type="text" id="Vpb8YNEGDwyU"
# 고객별 연속한 log사이의 시간 간격을 log duration으로 정의합니다. 이는 고객의 잔존시간을 구하는 것으로 연결됩니다.

# + [markdown] colab_type="text" id="bw8nYxB5DwyX"
# 현재 제공된 데이터에서는 고객이 앱을 종료하는 기록이 없기 때문에 마지막 log의 log_duration은 0이라고 가정을 합니다.

# + colab={} colab_type="code" id="EHdb72wlDwyk"
# 우선, timestamp 컬럼를 datetime 타입으로 변환해주세요.

log_order['timestamp']=log_order['timestamp'].astype('datetime64')

# + [markdown] colab_type="text" id="62EvoL7_Dwy1"
# ----

# + [markdown] colab_type="text" id="hU5LvcgoDwy3"
# 이번에는 timestamp_after 컬럼을 만들어줍니다. timestamp_after 컬럼은 다음 log의 timestamp값을 가집니다.
#
# 고객별로 groupby()한 뒤 shift(-1)을 적용한 결과를 timestamp_afterdp 저장합니다. 
#
# groupby를 하고 shift를 하면 고객의 당일 마지막 로그의 timestamp_after은 NaT(Not a Time)값을 갖게 됩니다.
#
# 결과는 아래와 같습니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>event_goods_id</th>
#       <th>event_name</th>
#       <th>event_origin</th>
#       <th>event_shop_id</th>
#       <th>n_user_id</th>
#       <th>price</th>
#       <th>timestamp</th>
#       <th>user_id</th>
#       <th>purchase</th>
#       <th>timestamp_after</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>shops_bookmark</td>
#       <td>NaN</td>
#       <td>0</td>
#       <td>NaN</td>
#       <td>2018-06-11 15:57:10.615</td>
#       <td>--PYPMX8QWg0ioT5zfORmU-S5Lln0lot</td>
#       <td>False</td>
#       <td>2018-06-11 15:59:05.505</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>shops_bookmark</td>
#       <td>NaN</td>
#       <td>0</td>
#       <td>NaN</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>--PYPMX8QWg0ioT5zfORmU-S5Lln0lot</td>
#       <td>False</td>
#       <td>NaT</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>my_goods</td>
#       <td>NaN</td>
#       <td>1</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:55:37.309</td>
#       <td>-16-xXbeDcvkZJtTpRwMi57Yo2ZQpORv</td>
#       <td>False</td>
#       <td>2018-06-11 00:55:44.430</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>2506.0</td>
#       <td>enter_browser</td>
#       <td>my_goods</td>
#       <td>40.0</td>
#       <td>1</td>
#       <td>NaN</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>-16-xXbeDcvkZJtTpRwMi57Yo2ZQpORv</td>
#       <td>False</td>
#       <td>2018-06-11 01:00:33.295</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>NaN</td>
#       <td>app_page_view</td>
#       <td>my_goods</td>
#       <td>NaN</td>
#       <td>1</td>
#       <td>NaN</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>-16-xXbeDcvkZJtTpRwMi57Yo2ZQpORv</td>
#       <td>False</td>
#       <td>2018-06-11 01:11:03.608</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="XqXWBIadDwy6"
# timestamp_after 컬럼을 다음과 같이 만듭니다.
log_order['timestamp_after'] = log_order.groupby(['n_user_id'])['timestamp'].shift(-1)

log_order.head()

# + [markdown] colab_type="text" id="MkgcXnunDwzC"
# timestamp_after과 timestamp의 차이를 계산하여 log_duration을 구합니다. NaT 값은 연산시 NaN값이 됩니다. 이후에 NaN값을 0으로 채워주시면 됩니다.

# + [markdown] colab_type="text" id="qO1VgIpCDwzD"
# ----
#

# + [markdown] colab_type="text" id="iUybXL_eDwzH"
# log_duration을 계산하고 nan값(마지막 로그)는 0으로 채워 log_duration 컬럼에 저장합니다.
#
# 출려 결과는 아래와 같습니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>timestamp</th>
#       <th>timestamp_after</th>
#       <th>log_duration</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>2018-06-11 15:57:10.615</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>00:01:54.890000</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>NaT</td>
#       <td>00:00:00</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>2018-06-11 00:55:37.309</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>00:00:07.121000</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>00:04:48.865000</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>2018-06-11 01:11:03.608</td>
#       <td>00:10:30.313000</td>
#     </tr>
#   </tbody>
# </table>
#
#

# + colab={} colab_type="code" id="AtCRnjihDwzM"
# log_duration을 계산하고 nan값(마지막 로그)는 0으로 채워 log_duration 컬럼에 저장합니다.

log_order['log_duration'] = log_order['timestamp_after']-log_order['timestamp']
log_order['log_duration'] = log_order['log_duration'].fillna(pd.Timedelta(0))
log_order[['timestamp','timestamp_after','log_duration']].head()

# + [markdown] colab_type="text" id="Nh8se6OpDwza"
# ----

# + [markdown] colab_type="text" id="q0sTh2RbDwzd"
# 분석의 편의를 위하여 map()과 total_seconds() 메서드를 이용하여 log_duration을 초로 환산해주세요.
#
# 마지막으로, 이 후의 계산을 위해 astype() 메서드를 이용하여 log_duration 컬럼을 float으로 변환해주세요.  

# + [markdown] colab_type="text" id="0g50CGO7Dwzf"
#
#
# 출력 결과는 아래와 같습니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>n_user_id</th>
#       <th>timestamp</th>
#       <th>timestamp_after</th>
#       <th>log_duration</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>0</td>
#       <td>2018-06-11 15:57:10.615</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>114.890</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>0</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>NaT</td>
#       <td>0.000</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>1</td>
#       <td>2018-06-11 00:55:37.309</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>7.121</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>1</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>288.865</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>1</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>2018-06-11 01:11:03.608</td>
#       <td>630.313</td>
#     </tr>
#   </tbody>
# </table>
#
#

# + colab={} colab_type="code" id="-XGEfi9IDwzj"
log_order['log_duration'] = log_order['log_duration'].dt.total_seconds()
# -

log_order['log_duration'] = log_order['log_duration'].astype('float64')

log_order[['timestamp','timestamp_after','log_duration']].head()

# + [markdown] colab_type="text" id="RtCQBzHyDw0Z"
# **14. 고객이 한 번 앱에 들어와서 활동하는 시간인 잔존시간을 구하기 위해 cycle을 정의해주세요.**

# + [markdown] colab_type="text" id="iwYXc3tFDw0d"
# 고객이 한번 app에 접속하여 나가기까지의 일련의 활동을 한 cycle이라 정의하겠습니다.
#
# cycle을 구하기 위해서 고객이 cycle을 종료하고 앱을 나갔는지 여부(boolean)인 is_out이라는 컬럼을 만듭니다. is_out의 조건은 아래와 같이 2가지가 있습니다.
#
#     조건 1) log_duration이 0이면 고객의 당일 마지막 log입니다.
#     
#     조건 2) log간 간격이 40분이상이면 고객이 한 cycle이 종료하고 다음 cycle로 돌아온 것이라고 하겠습니다.
#
#     
#    
#
# 따라서 위의 조건중 적어도 1개를 만족시키면 True되도록 is_out 컬럼을 생성해주세요. 
#
#
#
#

# + [markdown] colab_type="text" id="SHz6Ylx7Dw0j"
# 출력 결과는 아래와 같습니다.
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>n_user_id</th>
#       <th>timestamp</th>
#       <th>timestamp_after</th>
#       <th>log_duration</th>
#       <th>is_out</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>0</td>
#       <td>2018-06-11 15:57:10.615</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>114.890</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>0</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>NaT</td>
#       <td>0.000</td>
#       <td>True</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>1</td>
#       <td>2018-06-11 00:55:37.309</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>7.121</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>1</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>288.865</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>1</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>2018-06-11 01:11:03.608</td>
#       <td>630.313</td>
#       <td>False</td>
#     </tr>
#   </tbody>
# </table>
#
#
#

# + colab={} colab_type="code" id="lH6a12mmDw0n"
# 40분을 초로 환산해야 합니다.
s1 = (log_order['log_duration']==0)
s2 = (log_order['log_duration']>=2400)

log_order['is_out'] = np.where(s1|s2, True, False)
# -

log_order[['timestamp','timestamp_after','log_duration','is_out']].head()

# + [markdown] colab_type="text" id="yflr6ppSDw0x"
# log_duration이 2400이상 또는 음수인 log들은 cycle의 마지막 log입니다. 예를 들어, log_duration이 36000인 log가 있으면 이는 10시간 뒤에 다시 app에 접속한다는 것을 의미하지 실제 10시간 동안 앱을 사용했다는 의미가 아닙니다. 따라서 특정 사람에 대한 해당 logs는 해당 cycle의 마지막 log가 되고 다음 log는 10시간 뒤인 다음 cycle의 첫 log가 됩니다.
#
# 즉, 위의 조건들을 만족하는 log들의 log_duration은 0이 되도록 변환해주어야 합니다.
# is_out 컬럼이 True인 log_duration을 0으로 지정해주세요.

# + [markdown] colab_type="text" id="4KEYv1VGDw0y"
# 출력 결과는 아래와 같습니다.
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>n_user_id</th>
#       <th>timestamp</th>
#       <th>timestamp_after</th>
#       <th>log_duration</th>
#       <th>is_out</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>0</td>
#       <td>2018-06-11 15:57:10.615</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>114.890</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>0</td>
#       <td>2018-06-11 15:59:05.505</td>
#       <td>NaT</td>
#       <td>0.000</td>
#       <td>True</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>1</td>
#       <td>2018-06-11 00:55:37.309</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>7.121</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>1</td>
#       <td>2018-06-11 00:55:44.430</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>288.865</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>1</td>
#       <td>2018-06-11 01:00:33.295</td>
#       <td>2018-06-11 01:11:03.608</td>
#       <td>630.313</td>
#       <td>False</td>
#     </tr>
#   </tbody>
# </table>
#
#
#

# + colab={} colab_type="code" id="KGvN1Ht6Dw05"
# Write your code here!
log_order.loc[log_order['is_out']==True, 'log_duration']=0
log_order[['n_user_id','timestamp', 'timestamp_after', 'log_duration', 'is_out']].head()

# + [markdown] colab_type="text" id="z5Rolfx6Dw1N"
# ----

# + [markdown] colab_type="text" id="-qxhi1F8Dw1P"
# 이제 cycle을 구하여 번호를 부여할 것입니다.
#
# 번호는 cycle별 고유 번호(cycle_idx_unique)와 고객별 0부터 시작하는 daily cycle 번호(cycle_idx_daily)를 부여합니다.

# + colab={} colab_type="code" id="dEk2subcDw1V" outputId="b5d15bcc-589c-4d5b-ad1d-013756fe10e5"
log_order['cycle_idx_unique'] = (log_order['is_out']
                                 .cumsum()
                                 .shift(1)
                                 .fillna(0)
                                 .astype(int)
                                )

log_order[['n_user_id','timestamp', 'timestamp_after', 'log_duration', 'is_out', 'cycle_idx_unique']].head(5)

# + [markdown] colab_type="text" id="qRj_gUq7Dw1w"
# 이번엔 daily cycle 번호를 부여하겠습니다.

# +
log_order['cycle_idx_daily'] = (log_order.groupby('n_user_id')['is_out']
                                           .cumsum()
                                           .shift(1)
                                           .fillna(0)
                                           .astype(int)
                                            )

# user마다 첫 cycle_idx_daily가 1로 되어있기 때문에 이를 0으로 바꿔줍니다.
head_index = log_order.groupby('n_user_id')['cycle_idx_daily'].head(1).index
log_order.loc[head_index, 'cycle_idx_daily'] = 0

log_order[['n_user_id','timestamp', 'timestamp_after', 'log_duration', 'is_out','cycle_idx_daily']].head(30)

# + [markdown] colab_type="text" id="nW-bTP7PDw1_"
# 이번엔 cycle을 이용한 분석을 해보겠습니다.
#
# **cycle별 log 수(접속별 활동 개수)**, **user별 cycle당 평균 log수(고객별 접속당 평균 활동수)**을 구하겠습니다.
#
# **cycle별 log 수**는 코드는 아래와 같습니다.
#
# 이를 활용하여 `user별 cycle별 평균 log수`를 구해주세요.

# + [markdown] colab_type="text" id="9dhliWUvDw2A"
# **14.1) cycle별 log 수(접속별 활동 개수)**

# + colab={} colab_type="code" id="zk3depRlDw2C" outputId="9f7338d2-39df-4741-ec92-68e0f31156c9"
cycle_log_count = (log_order
                 .groupby(['n_user_id', 'cycle_idx_daily']) 
                 .size()  # 그룹별 속한 row 수(log 수)를 반환합니다.
                 .reset_index()  # index를 초기화합니다.
                 .rename(columns = { 0 : "log_count"} )   # 컬럼이름을 log_count로 변경합니다.
                )

cycle_log_count.head(5)

# + [markdown] colab_type="text" id="nauFhYBNDw2U"
# **14.2) user별 cycle당 평균 log수의 평균(고객별 접속당 평균 활동수)**

# + [markdown] colab_type="text" id="gc-4eE2NDw2V"
# 위에서 구한 cycle_log_count를 이용하여 user별 cycle당 평균 log수를 구해주세요.

# + [markdown] colab_type="text" id="SaTzgX9_Dw2W"
# 출력 결과는 아래와 같습니다.
# <table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>n_user_id</th>      <th>log_count_mean</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>0</td>      <td>2.00</td>    </tr>    <tr>      <th>1</th>      <td>1</td>      <td>7.00</td>    </tr>    <tr>      <th>2</th>      <td>2</td>      <td>16.00</td>    </tr>    <tr>      <th>3</th>      <td>3</td>      <td>7.75</td>    </tr>    <tr>      <th>4</th>      <td>4</td>      <td>2.00</td>    </tr>  </tbody></table>
# -

cycle_user_log_count = cycle_log_count.groupby('n_user_id')['log_count'].mean().reset_index()
cycle_user_log_count.head()

# + [markdown] colab_type="text" id="HZTHQN61Dw2j"
# **14.3) 하루동안 가장 많은 cycle을 갖는(가장 많이 활동한) 상위 5명의 user를 구해주세요.**
#
# `Hint) groupby(), nunique(), sort_values 메서드`

# + [markdown] colab_type="text" id="hmIg5-M1Dw2l"
# 결과는 아래와 같습니다. 순서는 상관 없습니다.
#
# ```
# n_user_id
# 6234     9
# 2424     9
# 2249    10
# 6010    10
# 5847    11
# ```
# -

log_order.groupby('n_user_id')['cycle_idx_daily'].nunique().sort_values(ascending = False).head()

# + [markdown] colab_type="text" id="iC-5xA0ADw2v"
# **15. 잔존시간을 구해주세요**

# + [markdown] colab_type="text" id="NXauJfUgDw2w"
# 잔존시간이란 고객이 앱에서 머문 시간을 뜻합니다.

# + [markdown] colab_type="text" id="dc-k5702Dw2x"
#
#
# 잔존 시간이 높다는 것은 사이트 운영의 청신호라고 생각할 수 있습니다. 일단 방문 목적과 랜딩페이지에서 제공되는 컨텐츠가 부합한다는 뜻이며, 웹사이트의 컨텐츠에 흥미를 느낀 방문자들이 계속 머물고 있다는 뜻이기도 합니다. 방문자들이 웹사이트에 오랜 시간 머물게 되면 웹사이트에서 제공하는 다양한 장치들을 접할 기회가 많아지고 전환에 도달할 확률이 더욱 높아지기 때문에 체류시간은 전환에 있어 매우 중요한 요소입니다.
# 광고를 고객을 통해 app으로의 유입을 성공해다면 그 다음 목표는 방문자를 계속 머물게 하여 전환으로 이어질 수 있도록 하는 것입니다.
#
# 해당 수업의 zigzag 데이터는 짧은 시간의 제한된 데이터라 잔존 시간을 이용하여 분석할 수 있는게 많지 않지만 현업에서는 잔존 시간을 이용하여 통해 어떤 채널을 이용한 고객 또는 어떤 광고를 통해 유입된 고객이 웹사이트/app에 오래 머물고 제품을 구매하는지에 대한 분석 또는 시간대/요일별 노출전략을 세우는 등 다양한 insight를 얻을 수 있습니다.
#
#

# + [markdown] colab_type="text" id="camiIN4QDw2z"
# 두가지 기준으로 잔존시간을 구할 것입니다.
#
#     1) user별
#     2) 구매 user/ 비구매 user

# + [markdown] colab_type="text" id="mlO8BpEGDw21"
# **15.1) user별 잔존시간을 구해주세요**
#
#

# + [markdown] colab_type="text" id="C8ejpQJ1Dw24"
# 먼저 cycle별 잔존시간을 다음과 같이 구합니다.

# + colab={} colab_type="code" id="CU3q4XsUDw28"
remaining_time_cycle = (log_order.groupby(['n_user_id', 'cycle_idx_daily'])['log_duration']
                         .sum()
                         .reset_index()
                         .rename(columns = {'log_duration' : 'remaining_time'})
                       )

remaining_time_cycle.head(10)

# + [markdown] colab_type="text" id="Nuox8Uv8Dw3G"
# remaining_time_cycle을 이용하여 user별 잔존시간을 구해주세요.
#
# Hint) groupby(), mean() 메서드
#
# 결과는 아래와 같습니다.
#
# <table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>duration</th>    </tr>    <tr>      <th>n_user_id</th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>114.890000</td>    </tr>    <tr>      <th>1</th>      <td>1011.541000</td>    </tr>    <tr>      <th>2</th>      <td>1346.260667</td>    </tr>    <tr>      <th>3</th>      <td>460.531250</td>    </tr>    <tr>      <th>4</th>      <td>49.130000</td>    </tr>    <tr>      <th>5</th>      <td>0.000000</td>    </tr>    <tr>      <th>6</th>      <td>1791.532000</td>    </tr>    <tr>      <th>7</th>      <td>2580.258000</td>    </tr>    <tr>      <th>8</th>      <td>984.298000</td>    </tr>    <tr>      <th>9</th>      <td>1657.393000</td>    </tr>  </tbody></table>

# + colab={} colab_type="code" id="DSrzJVLUDw3I"
remaining_time_cycle.groupby('n_user_id')['remaining_time'].mean().head(10)

# + [markdown] colab_type="text" id="jw845hnjDw3e"
# 잔존 시간이 0인 것들은 app에 들어와서 아무것도 안하고 나간 고객들입니다.
#
# 제외하고 계산할 수도 있습니다.

# + [markdown] colab_type="text" id="6pRbeg3UDw3h"
# **15.2) 구매/비구매 cycle별 평균 잔존시간 구하기**

# + [markdown] colab_type="text" id="GvnAA8D9Dw3l"
# 구매 기록이 있는 cycle은 잔존시간이 길 것이라고 예상할 수 있습니다. 이를 확인하기 위하여 구매/비구매 cycle별 평균 잔존시간을 구하겠습니다.

# + [markdown] colab_type="text" id="G4aeJs7zDw3p"
# 먼저 구매기록이 있는 cycle list를 만들어 주세요.
#
# cycle_purchase 변수에 구매기록이 있는 cycle들을 저장해주시면 됩니다.
#
# Hint) purchase 컬럼, indexing, unique() 메서드

# + colab={} colab_type="code" id="iu2yS-sSDw3r"
cycle_purchase = log_order.loc[log_order['purchase']==True, 'cycle_idx_unique']
# -

log_order[log_order['purchase']==True]

# + [markdown] colab_type="text" id="46CAJXXODw4D"
# ---

# + [markdown] colab_type="text" id="knPHhUjjDw4G"
# data_purchase 변수에는 구매 기록이 있는 cycle들의 데이터를,
#
# data_npurchase 변수에는 구매 기록이 없는 cycle들의 데이터를 저장해주세요.
#
# Hint) isin()메서드를 이용한 indexing

# + colab={} colab_type="code" id="-MOqveNADw4I"
# Write your code here!
data_purchase = log_order.loc[log_order['cycle_idx_unique'].isin(cycle_purchase)]
data_npurchase = log_order.loc[~log_order['cycle_idx_unique'].isin(cycle_purchase)]

# + [markdown] colab_type="text" id="CBAR0EUpDw4V"
# ---

# + [markdown] colab_type="text" id="CqCfDfKrDw4X"
# data_purchase를 이용하여 구매 cycle의 잔존시간을 구해주세요.
#
# Hint) User별 잔존시간을 구하는 방법과 매우 유사합니다. cycle_idx_unique를 이용해주세요.
#
# 결과는 아래와 같습니다.
#
# <table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>n_user_id</th>      <th>cycle_idx_unique</th>      <th>cycle_duration</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>2</td>      <td>4</td>      <td>3075.422</td>    </tr>    <tr>      <th>1</th>      <td>8</td>      <td>15</td>      <td>412.025</td>    </tr>    <tr>      <th>2</th>      <td>8</td>      <td>16</td>      <td>1791.231</td>    </tr>    <tr>      <th>3</th>      <td>9</td>      <td>19</td>      <td>1657.393</td>    </tr>    <tr>      <th>4</th>      <td>47</td>      <td>88</td>      <td>3116.367</td>    </tr>    <tr>      <th>5</th>      <td>49</td>      <td>92</td>      <td>2615.611</td>    </tr>    <tr>      <th>6</th>      <td>65</td>      <td>123</td>      <td>3093.858</td>    </tr>    <tr>      <th>7</th>      <td>86</td>      <td>168</td>      <td>1906.721</td>    </tr>    <tr>      <th>8</th>      <td>97</td>      <td>192</td>      <td>3031.770</td>    </tr>    <tr>      <th>9</th>      <td>117</td>      <td>232</td>      <td>1191.110</td>    </tr>  </tbody></table>

# + colab={} colab_type="code" id="D0RQpvOaDw4a"
data_purchase_duration = data_purchase.groupby(['n_user_id','cycle_idx_unique'])['log_duration'].sum().reset_index().rename(columns = {'log_duration':'cycle_duration'})
data_purchase_duration.head(10)

# + [markdown] colab_type="text" id="mW8sg41zDw40"
# 마찬가지로 비구매 cycle의 잔존시간을 구해주세요.

# + colab={} colab_type="code" id="D_W2dtyBDw43"
data_npurchase_duration = data_npurchase.groupby(['n_user_id','cycle_idx_unique'])['log_duration'].sum().reset_index().rename(columns = {'log_duration':'cycle_duration'})
data_npurchase_duration.head(10)

# + [markdown] colab_type="text" id="hqJMIVQ_Dw5K"
# 마지막으로 구매/비구매 cycle의 잔존 시간으로 boxplot을 그려주세요. 그리고 구매 cycle 잔존 시간 평균과 비구매 cycle 잔존 시간 평균을 구해주세요.
#
# 결과는 아래와 같습니다.
#
# <img src="https://drive.google.com/uc?export=view&id=1Pu4__DARP88Agt9w-f9IaequPznszMVZ" width="600" height="224"></img> 
#
#
# ```
# 구매 cycle 잔존 시간 평균: 2280.0800799999997
# 비구매 cycle 잔존 시간 평균: 611.9902027010454
# ```
#

# + colab={} colab_type="code" id="oErFl37BDw5M"
fig, ax = plt.subplots(nrows=2, ncols=1, figsize = (10,4), constrained_layout=True)
sns.boxplot(data_npurchase_duration['cycle_duration'], ax = ax[0])
ax[0].set_title('비구매 cycle 잔존시간')
sns.boxplot(data_purchase_duration['cycle_duration'], ax = ax[1])
ax[1].set_title('구매 cycle 잔존시간');
# -

print(f"구매 cycle 잔존 시간 평균: {data_purchase_duration['cycle_duration'].mean()}")
print(f"비구매 cycle 잔존 시간 평균: {data_npurchase_duration['cycle_duration'].mean()}")

# + [markdown] colab_type="text" id="4pMfn17oDw5T"
# ## 제출
#
# 과제를 다 끝내셨으면 http://bit.ly/ds-assignment 에서 안내에 따라 과제를 제출하여 주세요! 과제를 제출해주시면 솔루션과 검토 결과를 드립니다. 오프라인 수업의 경우 과제를 제출하지 않으시더라도 솔루션은 다음 수업 시간에 제공해드립니다.
#
# 수업이나 과제 관련 질문, 수료증 문의 등은 담당 튜터(조교)에게 문의 주세요. 영수증 발급 등의 문의는 support@dsschool.co.kr 로 메일 주시면 담당자분이 응대해주실 겁니다. 기타 궁금한 사항은 슬랙으로 문의 주세요!

# + colab={} colab_type="code" id="ZDbH_ylBDw5U"

