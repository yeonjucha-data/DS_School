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

# + [markdown] colab_type="text" id="nn9OrDw4FxRQ"
# ## DS School의 데이터분석 팀에 오신 것을 환영합니다!
#
#
# (이 쥬피터 노트북은 다음의 링크 https://bit.ly/dsa-0302 데이터는 https://bit.ly/dsa-dsschool 에서 다운받을 수 있습니다.)
#
# 안녕하세요! [DS School](https://dsschool.co.kr) 데이터분석팀에 오신 것을 환영합니다.
#
# [DS School](https://dsschool.co.kr)은 직무교육 스타트업으로 데이터 사이언스와 데이터 마케팅 수업을 진행하고 있습니다.
#
# 오늘 이 쥬피터 노트북을 받은 수강생분들께서는 하루동안 DS School의 일일 데이터 분석가(Data Analyst)로서 일을 할 것입니다. DS School의 데이터베이스에서 파일을 읽어와 운영, 기획, 마케팅, 재무팀의 요청사항을 분석한 뒤, 그 결과를 전달하는 것이 오늘의 목표입니다.
#
# DS School의 마케팅팀은 분석 결과를 바탕으로 사용 플랫폼별 예산을 재조정할 수도 있고, 캠페인별 성과를 비교분석하여 사용자의 니즈를 파악함과 동시에 캠페인별 예산 비중을 조절할 수 있습니다. 또한, 재무팀은 분석 결과를 바탕으로 매출을 예측할 수 있고 이를 바탕으로 예산안을 작성할 수도 있습니다.
#
# 반면 데이터 분석가(Data Analyst)가 정확한 분석 결과를 전달해주지 못한다면, 마케팅팀은 마케팅 예산을 재조정하는데 실패함으로써 회사의 매출을 감소시킬 수 있습니다. 운영팀과 기획팀은 매출이 잘 나오지 않는 컨텐츠에 많은 시간과 비용을 투입함으로써 회사에 손해를 안길 것입니다. 재무팀은 회사의 앞으로의 재무상황을 잘못 예측함으로써 큰 위기에 빠질 수 있습니다.
#
# 그러므로 데이터를 정확하게 분석하는 것은 무엇보다도 중요합니다. 하기에 제시한 15개의 데이터 분석 요청을 프로그래밍 언어 파이썬(Python)과 파이썬의 데이터 분석 패키지 판다스(Pandas), 그리고 데이터베이스 관리 패키지인 SQLite를 활용해 풀어주세요.
#
# 숙련된 데이터분석가의 경우 하기의 요청을 늦어도 3시간 내에는 해결할 수 있습니다. 즉, **3시간 안에 모든 문제를 풀 수 있다면 합격입니다.**
#
# 문제를 풀 때 다른 자료를 참고하거나, 구글에 검색하는 것 모두 허용합니다. (문제 중에는 구글에 검색하지 않으면 풀 수 없는 문제도 준비해놓았습니다) 관련 자료는 [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)를 강력 추천합니다. 또한, SQL에 대해 궁금하신 내용은 [SQL Tutorial](https://www.w3schools.com/sql/)을 참고할 것을 추천드립니다. 이전 수업에서 학습한 내용을 참고하는 것도 적극 추천합니다.

# + [markdown] colab_type="text" id="YOf68omFFxRT"
# ## 데이터 로딩하기
#
# 먼저 데이터를 로딩하도록 하겠습니다. 저번 주 수업과는 달리 여러분들은 엔지니어가 추출해준 csv 파일을 받은 것이 아닌 데이터베이스에 대한 접근 권한을 받았습니다. 따라서, 여러분들은 DB에서 필요한 데이터를 추출하는데 필요한 쿼리문을 이용하여 데이터를 불러와야 합니다.
#
#
#
# --- 
# ### 데이터셋 설명
#
# 여러분들이 사용할 수 있는 테이블의 리스트는 다음과 같습니다.
#  
# * surveys
#
#     DS School 홈페이지에 접속하게 되면 설문조사를 수행하게 되고, 이 결과를 바탕으로 적절한 강의를 선정해 과목 추천을 해드리고 있습니다. 이 때, 수집한 설문조사 내용은 고객의 수요를 조사하는데 아주 소중한 자산이 되고, 강의 내용에 대한 피드백이나 향후 오픈할 강의의 우선순위를 정하는데 쓰일 수 있습니다.
#     
#     
#  * users
#  
#     여러가지 마케팅 채널들을 통해서 유입된 고객들에게는 별도의 id가 부여가 됩니다. 이를 통해 고객의 결제 유무 등을 파악할 수 있고, 이는 마케팅 채널별 효율 분석에 소중한 자산이 됩니다. mixpanel에서 사용하는 id와 DS School에서 자체적으로 사용하는 데이터베이스의 user id를 연결시켜주는 역할을 하고, 고객에 개인정보를 가지고 있습니다. 이는 비식별화 과정을 거쳐 제공됩니다.
#     
#     
# * payments
#
#     유저들의 결제 정보입니다. 연락처와 수강신청한 기수, 결제일, 결제 상태 등이 제공되는데 마찬가지로 개인정보는 비식별화되어있는 상태로 제공됩니다. 2018년 이전의 결제 정보가 포함되어 있습니다.
#     
#
# * 믹스패널 데이터
#
#     DS School은 웹로그 데이터 분석을 위해 믹스패널을 사용합니다. 2009년 설립된 믹스패널은 사용자 추적을 기본으로 하는 분석 툴로, 원하는 서비스 사용자를 지정하면 해당 유저의 활동을 모두 조회할 수 있는 기능을 제공해줍니다. 이를 통해 해당 사용자 그룹의 특성과 사용 패턴을 알 수 있습니다. 유명 액셀러레이터 ‘Y Combinator’의 멤버로 트위치, 우버, 핏빗, 스포티파이, 세일즈포스 등의 고객사를 보유하고 있으며 2016년 1월 기준 누적 투자액 800억원을 기록함과 동시에 기업 가치 9,000억원대로 평가 받는 분석툴이기도 합니다. 실시간분석이 가능하며 코호트 분석과 잔존율, 퍼널 분석이 가능합니다. 믹스패널 데이터 또한 고객의 유입경로 등의 정보를 가지고 있습니다. 제공되는 데이터는 믹스패널 데이터베이스에서 추출한 자료이기 때문에 csv파일로 제공됩니다.

# + [markdown] colab_type="text" id="QNYJv1k4FxRV"
# ---

# + [markdown] colab_type="text" id="JWzKlk1CFxRW"
# **1. 데이터베이스에서 설문조사 결과를 읽어와주세요. 그 다음 사용자와 질문을 기준으로 정렬해주세요.**

# + [markdown] colab_type="text" id="zxx3lwLrFxRa"
# 설문조사 결과를 분석하여, DS School 홈페이지에 접속하는 사람들이 왜 데이터 사이언스에 관심이 있는지 파악하려고 합니다. 고객들의 니즈를 파악하여 향후 어떤 강의를 우선적으로 오픈할지 결정할 수도 있고, 수강생들에게 어떤 내용의 자료를 보여드려야할지 결정할 수도 있습니다.

# + [markdown] colab_type="text" id="a77mw7ibFxRc"
# 하지만, 중복응답이 가능한 설문조사이다 보니, 데이터베이스에 정보가 보기좋게 정리되어 있지는 않습니다. 이를 응답한 사람과 질문 번호 순으로 정렬해주세요.
#
# 데이터베이스에 설문 데이터가 정리 후에 정답은 다음과 같이 나오게 됩니다.

# + [markdown] colab_type="text" id="UTRNkgEOFxRd"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>survey_id</th>
#       <th>user_id</th>
#       <th>question_id</th>
#       <th>answer1_selected</th>
#       <th>answer2_selected</th>
#       <th>answer3_selected</th>
#       <th>answer4_selected</th>
#       <th>answer5_selected</th>
#       <th>answer6_selected</th>
#       <th>answer7_selected</th>
#       <th>answer8_selected</th>
#       <th>answer9_selected</th>
#       <th>answer10_selected</th>
#       <th>answer11_selected</th>
#       <th>answer12_selected</th>
#       <th>created_at</th>
#       <th>updated_at</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>73176</th>
#       <td>os5048odsazv</td>
#       <td>006tq68icz4g</td>
#       <td>1</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-03-17 16:15:50.334428</td>
#       <td>2018-03-17 16:15:50.334428</td>
#     </tr>
#     <tr>
#       <th>73168</th>
#       <td>t5qwx5xdjcwy</td>
#       <td>006tq68icz4g</td>
#       <td>2</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-03-17 16:16:03.192710</td>
#       <td>2018-03-17 16:16:03.19271</td>
#     </tr>
#     <tr>
#       <th>73177</th>
#       <td>rok2mzb73rf6</td>
#       <td>006tq68icz4g</td>
#       <td>3</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>2018-03-17 16:16:37.648422</td>
#       <td>2018-03-17 16:16:37.648422</td>
#     </tr>
#     <tr>
#       <th>73184</th>
#       <td>oilk23xum4ur</td>
#       <td>006tq68icz4g</td>
#       <td>4</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-03-17 16:16:51.857495</td>
#       <td>2018-03-17 16:16:51.857495</td>
#     </tr>
#     <tr>
#       <th>73185</th>
#       <td>utjiy4kgyvre</td>
#       <td>006tq68icz4g</td>
#       <td>5</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-03-17 16:17:09.312639</td>
#       <td>2018-03-17 16:17:09.312639</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="f5L6DWfZFxRf"
#데이터를 불러오는데 필요한 판다스와 sqlite3를 import 해주세요.
import pandas as pd
import sqlite3

# + colab={} colab_type="code" id="JOdOvTWEFxRp"
# 판다스는 테이블을 출력할 때, row나 column이 일정 개수 이상 넘으면 생략해서 보여줍니다.
# column을 생략하길 원하지 않는 경우 아래와 같이 옵션을 주어 생략되지 않도록 할 수 있습니다.
pd.options.display.max_columns = 50

# + colab={} colab_type="code" id="DHtNSJaWFxRy" outputId="bef040a4-de8c-410b-e7f8-c3261c5e56ad"
# data폴더의 dsschool.db에 접속을 해주세요.
connect = sqlite3.connect('dsschool.db')
connect

# + colab={} colab_type="code" id="6rEX61GjFxR9" outputId="e5b89c67-502d-4350-83a9-595f8ab778a4"
# 'surveys' 테이블의 모든 컬럼을 가져오는 쿼리를 작성 후 read_sql로 불러와주세요.
query = "SELECT * FROM 'surveys'"

surveys = pd.read_sql(query, connect)

print(surveys.shape)
surveys.head(5)

# + [markdown] colab_type="text" id="7Zkq7XeAFxSG"
# surveys를 user_id와 question_id, 그리고 created_at를 기준으로 정렬해주세요. user_id를 우선으로 정렬해야 합니다.

# + colab={} colab_type="code" id="EPxEG21iFxSI"
surveys = surveys.sort_values(['user_id','question_id','created_at'])
surveys.head()

# + [markdown] colab_type="text" id="_YxDlfZXFxSP"
# ---

# + [markdown] colab_type="text" id="ox759XaPFxSS"
# **2. Survey 정보를 cleaning해주세요.**
#
# Surveys 테이블은 원본 데이터이기 때문에 분석을 위해서는 cleaning 작업이 필요합니다. 여러분이 해주셔야 할 처리는 다음과 같습니다.
#   
#      * answer 값이 't', 'f'로 입력되어 있는데 이를 True, False로 변환해주세요.
#      * created_at과 updated_at을 datetime 형식으로 변환해주세요.
#      * 같은 user_id가 여러번의 설문조사를 응답한 경우도 제거해주세요.

# + [markdown] colab_type="text" id="zmHPuJngFxSU"
# 정리 후의 테이블은 다음과 같이 나오게됩니다.
#
# <div>
# <style scoped>
#     .dataframe tbody tr th:only-of-type {
#         vertical-align: middle;
#     }
#
#     .dataframe tbody tr th {
#         vertical-align: top;
#     }
#
#     .dataframe thead th {
#         text-align: right;
#     }
# </style>
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>survey_id</th>
#       <th>user_id</th>
#       <th>question_id</th>
#       <th>answer1_selected</th>
#       <th>answer2_selected</th>
#       <th>answer3_selected</th>
#       <th>answer4_selected</th>
#       <th>answer5_selected</th>
#       <th>answer6_selected</th>
#       <th>answer7_selected</th>
#       <th>answer8_selected</th>
#       <th>answer9_selected</th>
#       <th>answer10_selected</th>
#       <th>answer11_selected</th>
#       <th>answer12_selected</th>
#       <th>created_at</th>
#       <th>updated_at</th>
#       <th>answer1_selected(bool)</th>
#       <th>answer2_selected(bool)</th>
#       <th>answer3_selected(bool)</th>
#       <th>answer4_selected(bool)</th>
#       <th>answer5_selected(bool)</th>
#       <th>answer6_selected(bool)</th>
#       <th>answer7_selected(bool)</th>
#       <th>answer8_selected(bool)</th>
#       <th>answer9_selected(bool)</th>
#       <th>answer10_selected(bool)</th>
#       <th>answer11_selected(bool)</th>
#       <th>answer12_selected(bool)</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>73176</th>
#       <td>os5048odsazv</td>
#       <td>006tq68icz4g</td>
#       <td>1</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-03-17 16:15:50.334428</td>
#       <td>2018-03-17 16:15:50.334428</td>
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
#     </tr>
#     <tr>
#       <th>73168</th>
#       <td>t5qwx5xdjcwy</td>
#       <td>006tq68icz4g</td>
#       <td>2</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-03-17 16:16:03.192710</td>
#       <td>2018-03-17 16:16:03.19271</td>
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
#     </tr>
#     <tr>
#       <th>73177</th>
#       <td>rok2mzb73rf6</td>
#       <td>006tq68icz4g</td>
#       <td>3</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>2018-03-17 16:16:37.648422</td>
#       <td>2018-03-17 16:16:37.648422</td>
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
#       <td>True</td>
#       <td>False</td>
#     </tr>
#     <tr>
#       <th>73184</th>
#       <td>oilk23xum4ur</td>
#       <td>006tq68icz4g</td>
#       <td>4</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-03-17 16:16:51.857495</td>
#       <td>2018-03-17 16:16:51.857495</td>
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
#     </tr>
#     <tr>
#       <th>73185</th>
#       <td>utjiy4kgyvre</td>
#       <td>006tq68icz4g</td>
#       <td>5</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-03-17 16:17:09.312639</td>
#       <td>2018-03-17 16:17:09.312639</td>
#       <td>False</td>
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
#     </tr>
#   </tbody>
# </table>
# </div>
#
#

# + [markdown] colab_type="text" id="DV5Rekf_FxSW"
# answer의 t 값과 f값을 True, False로 변환하는 코드를 작성해주세요. 원본 데이터를 수정하지 말고 새로운 컬럼을 만들어주세요. (ex. answer1_selected(bool))
# -

for i in range(1,13):
    old = f'answer{i}_selected'
    new = f'answer{i}_selected(bool)'
    
    surveys[new] = surveys[old] == 't'

# + colab={} colab_type="code" id="L_gH_u_lFxSX"
# apply를 이용한 풀이

# def TF_update(x):
#     if x == 't':
#         return 'True'
#     elif x == 'f':
#         return 'False'

# for i in range(1,13):
#     surveys[f'answer{i}_selected(bool)'] = surveys[f'answer{i}_selected'].apply(lambda x: TF_update(x))

# + [markdown] colab_type="text" id="jZJOqNtiFxSd"
# 그리고, created_at과 updated_at을 datetime 자료형으로 변환해주세요. pd.to_datetime() 함수를 활용하는 것이 편합니다.

# + colab={} colab_type="code" id="LOzJxs8pFxSf"
surveys['created_at'] = pd.to_datetime(surveys['created_at'])
surveys['updated_at'] = pd.to_datetime(surveys['updated_at'])

# + [markdown] colab_type="text" id="aJUXi08WFxSp"
# 같은 유저가 여러번 설문조사를 응답한 경우를 제거해주세요, drop_duplicates() 메소드를 사용하는데, keep 옵션을 통해 어떤 정보를 남길지 정할 수 있습니다.
#
# **주의** : 1번 문제에서 created_at으로 sorting이 되어 있는 상태에서 drop_duplicates()를 사용하셔야 합니다.
#

# + colab={} colab_type="code" id="ySy5gzJHFxSs"
surveys = surveys.drop_duplicates(['user_id','question_id'], keep = 'last')

surveys.head()

# + [markdown] colab_type="text" id="QE2FHEtqFxTA"
# ---

# + [markdown] colab_type="text" id="vusReY5EFxTE"
# **3. 데이터베이스에서 결제정보를 불러와주세요. 그리고 연락처와 수업정보를 정리해주세요.**

# + [markdown] colab_type="text" id="lkBbLMjFFxTF"
# 데이터베이스의 payments 테이블에서 데이터를 읽어오겠습니다. 마찬가지로 쿼리문과 데이터베이스에 접속하기 위한 커넥터를 이용하여 payments 테이블을 가져옵니다.

# + colab={} colab_type="code" id="mMIq5p58FxTG"
query = "SELECT * FROM 'payments'"

payments = pd.read_sql(query, connect)

print(payments.shape)
payments.head(5)

# + [markdown] colab_type="text" id="kSCTc40uFxTR"
# 개인정보 보호를 위해 연락처 정보는 비식별화 처리된 상태입니다.

# + [markdown] colab_type="text" id="xqYl3n9JFxTS"
# 이번에는 연락처 정보를 정리하도록 하겠습니다. 결제창에서 수기로 연락처를 입력받아 수강생별로 연락처의 양식이 들쑥날쑥합니다. 이번에는 모든 연락처의 양식을 010-xxxx-xxxx으로 통일해주세요. 단, 010으로 시작하지 않는 전화번호는 잘못 기입된 전화번호라고 가정하고 NaN값 처리해주세요.

# + [markdown] colab_type="text" id="RFLt9rhXFxTU"
# *참고*
# 이 문제를 풀기 위해서는 string (문자열)에 관련된 메소드를 알고 있어야 합니다. 문자열에 관련된 함수와 정규 표현식의 상세한 내용은 수업의 범위를 벗어나므로 링크로 대체합니다. pandas.Series.str에 대한 정보는 [다음 링크](https://pandas.pydata.org/pandas-docs/stable/api.html#string-handling)에 잘 정리되어 있습니다. 또한, 문자 내에서 특정 역할을 하는 **정규 표현식**은 [다음 링크](https://wikidocs.net/4308)에 잘 설명되어 있습니다.

# + [markdown] colab_type="text" id="3IbiTzh8FxTV"
# 010이나 +82로 시작하는 번호를 골라주세요. +의 경우 문자 내에서 특정한 역할을 수행하기 때문에 이를 무력화 시켜주는 역슬래시(\)를 사용하여야 합니다. 

# + colab={} colab_type="code" id="9leB7CUoFxTY"
payments[~payments['연락처'].str.contains(r'^010')]
# -

import numpy as np
payments.loc[~payments['연락처'].str.contains(r'^010'), '연락처'] = np.nan

payments[payments['연락처'].isnull()]


# + [markdown] colab_type="text" id="qHTtudpTFxTe"
# 각 행, 또는 각 열에 스스로 만든 함수를 사용하고 싶은 경우에는 apply, map, applymap을 사용합니다. 이 경우에는 연락처의 각 데이터에 대쉬 (-)를 사이사이에 넣는 작업을 할 수 있는 함수를 만들어 apply, map, applymap 등을 사용해야 합니다.

# + colab={} colab_type="code" id="2lStb2ugFxTf"
# 대시(-)가 있으면 그대로 반환, 없으면 대시를 넣어주는 함수를 만들어 주세요. 그리고 apply를 이용해 이를 적용해주세요.
def clean_phone_number(phone_number):
    if pd.isnull(phone_number):
        return np.nan

#대시가 문자열에 이미 있다면 번호를 그대로 반환합니다.
    if "-" in phone_number:
        return phone_number
    
#대시가 문자열에 없다면 자릿수에 맞추어 대시를 넣어줍니다.
    else:
        phone_number = phone_number[0:3] + "-" + phone_number[3:7] + '-' + phone_number[7:]
        
        return phone_number

#연락처 데이터에 clean_phone_number 함수를 각각 apply를 이용해 적용시킵니다.
#그리고 이 데이터들로 연락처(clean) 칼럼을 대체합니다.

#Write your code here!

payments['연락처'] = payments['연락처'].apply(clean_phone_number)
# -

payments['연락처']

# + [markdown] colab_type="text" id="FVAe9jp-FxTk"
# 신청 수업을 쪼개어 수업타입과 기수를 만들어내는 작업 또한 string 메소드를 사용해야 합니다. split을 이용하여 띄어쓰기 별로 데이터를 분리한 뒤, 마지막 단어는 기수, 그 앞의 모든 단어들은 수업타입으로 만들어줄 수 있습니다.

# + colab={} colab_type="code" id="6f3LvsGWFxTl" outputId="4ba5e1a3-7436-4bb3-86fe-95ccb68f44ce"
# string.split() 사용 예시입니다. 구분 기준마다 문자를 나누어 리스트로 만들어줍니다.
print('010-1234-5678'.split('-'))

#별도로 구분 기준을 정해주지 않는 경우 자동으로 공백을 기준으로 분리합니다.
print('입문 속성반 5기'.split())

# + colab={} colab_type="code" id="X6ZMBoG9FxTs" outputId="70b86628-a838-4acf-f5cf-776827141385"
#뒤의 2개를 붙이고 싶은 경우 붙이는 ''.join()을 이용합니다.
example_list = ['입문', '속성반', '5기']

print(''.join(example_list[1:]))

print('--'.join(example_list[1:]))

# + [markdown] colab_type="text" id="A1Ise4kEFxT0"
# 신청수업을 띄어쓰기를 기준으로 split 해주세요. 그리고 이를 이용하여 수업타입과 기수를 분리해주세요. 성공적으로 수행할 시 결과는 다음과 같게 나옵니다.

# + [markdown] colab_type="text" id="R2oSvSr-FxT1"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>신청수업</th>
#       <th>수업타입</th>
#       <th>기수</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>입문반 22기</td>
#       <td>입문반</td>
#       <td>22기</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>중급반 5기</td>
#       <td>중급반</td>
#       <td>5기</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>입문반 22기</td>
#       <td>입문반</td>
#       <td>22기</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>입문반 22기</td>
#       <td>입문반</td>
#       <td>22기</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>중급반 5기</td>
#       <td>중급반</td>
#       <td>5기</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="F20weSgNFxT2"
class_split = payments['신청수업'].str.split()
payments['수업타입'] = class_split.str.get(0)
payments['기수'] = class_split.str.get(1)
payments[['신청수업','수업타입','기수']].head()

# + [markdown] colab_type="text" id="NMlrgn2YFxT9"
# ---

# + [markdown] colab_type="text" id="rd-R_VWHFxT_"
# **4. 2018년 이후 결제 정보를 정리해주세요.**
#
# 결제정보가 잘 정리되어 있지만, 분석을 진행하기 위해 처리해야할 사항이 남아있습니다. 
#     
#     1) 신청날짜 컬럼을 datetime 자료형으로 만들어주세요.
#     2) 결제가 완료된 경우 True, 아닌 경우 False인 컬럼을 만들어주세요.
#

# + [markdown] colab_type="text" id="kUyWSOxYFxUB"
# 결과는 다음과 같이 나오게 됩니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>상태</th>
#       <th>상태(bool)</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>결제 완료</td>
#       <td>True</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>결제 완료</td>
#       <td>True</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>결제 완료</td>
#       <td>True</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>결제 완료</td>
#       <td>True</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>결제 완료</td>
#       <td>True</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="wpMm-eTEFxUE"
payments['신청날짜'] = pd.to_datetime(payments['신청날짜'])
# -

payments['상태(bool)'] = payments['상태'] == '결제 완료'

payments[['상태','상태(bool)']].head()

# + [markdown] colab_type="text" id="_IBSjJmqFxUL"
# ---

# + [markdown] colab_type="text" id="PJ39Vv40FxUM"
# **5. 결제 데이터에서 신청날짜 칼럼을 이용하여 월, 일, 요일, 시간 칼럼을 추가해주세요. 그리고, 금액 정보를 정수형 (int)로 바꿔주세요.**

# + [markdown] colab_type="text" id="lZ3xtI2VFxUN"
# 월, 일, 시간, 요일 등을 기준으로 피벗테이블을 만들거나 그래프를 그리려면 그에 해당하는 칼럼을 만들어주어야 합니다. 입문반에서 배웠던 슬라이싱(Slicing)을 이용해 문자를 쪼개는 방식으로 할 수도 있지만, 자료형을 datetime으로 만들어버리면 더욱 쉽게 월, 일, 시간, 요일 등의 정보를 만들어낼 수 있습니다.

# + [markdown] colab_type="text" id="W5NjY9PuFxUP"
# 정답은 다음과 같이 나오게 됩니다. 
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>신청날짜</th>
#       <th>신청날짜(연)</th>
#       <th>신청날짜(월)</th>
#       <th>신청날짜(일)</th>
#       <th>신청날짜(시)</th>
#       <th>신청날짜(분)</th>
#       <th>신청날짜(초)</th>
#       <th>신청날짜(요일)</th>
#       <th>금액</th>
#       <th>금액(int)</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>2018-01-31 15:42:20</td>
#       <td>2018</td>
#       <td>1</td>
#       <td>31</td>
#       <td>15</td>
#       <td>42</td>
#       <td>20</td>
#       <td>Wednesday</td>
#       <td>495,000</td>
#       <td>495000</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>2018-01-31 15:29:24</td>
#       <td>2018</td>
#       <td>1</td>
#       <td>31</td>
#       <td>15</td>
#       <td>29</td>
#       <td>24</td>
#       <td>Wednesday</td>
#       <td>594,000</td>
#       <td>594000</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>2018-01-31 14:04:14</td>
#       <td>2018</td>
#       <td>1</td>
#       <td>31</td>
#       <td>14</td>
#       <td>4</td>
#       <td>14</td>
#       <td>Wednesday</td>
#       <td>495,000</td>
#       <td>495000</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>2018-01-31 10:18:19</td>
#       <td>2018</td>
#       <td>1</td>
#       <td>31</td>
#       <td>10</td>
#       <td>18</td>
#       <td>19</td>
#       <td>Wednesday</td>
#       <td>495,000</td>
#       <td>495000</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>2018-01-30 19:12:54</td>
#       <td>2018</td>
#       <td>1</td>
#       <td>30</td>
#       <td>19</td>
#       <td>12</td>
#       <td>54</td>
#       <td>Tuesday</td>
#       <td>594,000</td>
#       <td>594000</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="37tyvSgwFxUQ"
payments['신청날짜(연)'] = payments['신청날짜'].dt.year
payments['신청날짜(월)'] = payments['신청날짜'].dt.month
payments['신청날짜(일)'] = payments['신청날짜'].dt.day
payments['신청날짜(시)'] = payments['신청날짜'].dt.hour
payments['신청날짜(분)'] = payments['신청날짜'].dt.minute
payments['신청날짜(초)'] = payments['신청날짜'].dt.second
payments['신청날짜(요일)'] = payments['신청날짜'].dt.day_name()

# + colab_type="text" id="Yddu3hkqFxUY"
payments['금액(int)'] = payments['금액'].str.replace(',','').astype(int)
# -

payments[['신청날짜','신청날짜(연)','신청날짜(월)','신청날짜(일)','신청날짜(시)','신청날짜(분)','신청날짜(초)','신청날짜(요일)','금액','금액(int)']].head()

# + [markdown] colab_type="text" id="p4xhvGGMFxUZ"
# **6. 결제 데이터를 바탕으로 요일별, 시간별 결제량의 차이를 구해주세요.**

# + [markdown] colab_type="text" id="3M1C34zLFxUa"
# DS School에서 주로 사용하고 있는 마케팅 채널인 페이스북은 시간, 요일대별 광고 노출빈도를 조절할 수 있는 기능이 있습니다. 기존의 결제 패턴을 분석해 결제가 특정 시간대에서 높게 일어난다면 해당 시간대에 더 많은 예산을 사용하는 것이 효율적일 것입니다.

# + [markdown] colab_type="text" id="LrR3bbZcFxUb"
# 피벗테이블을 만들었을 때 결과가 다음과 같이 나와야 합니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr>
#       <th></th>
#       <th>sum</th>
#       <th>count</th>
#     </tr>
#     <tr>
#       <th></th>
#       <th>금액(int)</th>
#       <th>금액(int)</th>
#     </tr>
#     <tr>
#       <th>신청날짜(요일)</th>
#       <th></th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>Monday</th>
#       <td>91184000</td>
#       <td>145</td>
#     </tr>
#     <tr>
#       <th>Tuesday</th>
#       <td>78183000</td>
#       <td>128</td>
#     </tr>
#     <tr>
#       <th>Wednesday</th>
#       <td>100303000</td>
#       <td>170</td>
#     </tr>
#     <tr>
#       <th>Thursday</th>
#       <td>102165000</td>
#       <td>175</td>
#     </tr>
#     <tr>
#       <th>Friday</th>
#       <td>86818000</td>
#       <td>155</td>
#     </tr>
#     <tr>
#       <th>Saturday</th>
#       <td>44337000</td>
#       <td>76</td>
#     </tr>
#     <tr>
#       <th>Sunday</th>
#       <td>54212000</td>
#       <td>88</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="yWkidbY3FxUc"
pivot_1 = pd.pivot_table(payments, index = '신청날짜(요일)', values = '금액(int)', aggfunc = ['sum','count'])

days = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_1 = pivot_1.reindex(days)
pivot_1

# + [markdown] colab_type="text" id="pNrffBnEFxUi"
# 평일의 결제량이 주말에 비해 매우 높은 것을 알 수 있습니다. 이를 시간별 결제량과 연결지어보도록 하겠습니다. 마찬가지로 시각에 따른 피벗테이블도 만들어 주세요.

# + [markdown] colab_type="text" id="mPxXWylyFxUj"
# 결과는 다음과 같게 나오게 됩니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr>
#       <th></th>
#       <th>sum</th>
#       <th>count</th>
#     </tr>
#     <tr>
#       <th></th>
#       <th>금액(int)</th>
#       <th>금액(int)</th>
#     </tr>
#     <tr>
#       <th>신청날짜(시)</th>
#       <th></th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>19962000</td>
#       <td>35</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>9663000</td>
#       <td>16</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>5699000</td>
#       <td>9</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>3122000</td>
#       <td>5</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>4066000</td>
#       <td>6</td>
#     </tr>
#     <tr>
#       <th>5</th>
#       <td>2033000</td>
#       <td>3</td>
#     </tr>
#     <tr>
#       <th>6</th>
#       <td>6251000</td>
#       <td>8</td>
#     </tr>
#     <tr>
#       <th>7</th>
#       <td>5643000</td>
#       <td>11</td>
#     </tr>
#     <tr>
#       <th>8</th>
#       <td>19188000</td>
#       <td>28</td>
#     </tr>
#     <tr>
#       <th>9</th>
#       <td>27836000</td>
#       <td>49</td>
#     </tr>
#     <tr>
#       <th>10</th>
#       <td>42721000</td>
#       <td>80</td>
#     </tr>
#     <tr>
#       <th>11</th>
#       <td>39475000</td>
#       <td>65</td>
#     </tr>
#     <tr>
#       <th>12</th>
#       <td>23515000</td>
#       <td>43</td>
#     </tr>
#     <tr>
#       <th>13</th>
#       <td>42586000</td>
#       <td>73</td>
#     </tr>
#     <tr>
#       <th>14</th>
#       <td>33935000</td>
#       <td>58</td>
#     </tr>
#     <tr>
#       <th>15</th>
#       <td>37487000</td>
#       <td>61</td>
#     </tr>
#     <tr>
#       <th>16</th>
#       <td>41328000</td>
#       <td>64</td>
#     </tr>
#     <tr>
#       <th>17</th>
#       <td>33924000</td>
#       <td>57</td>
#     </tr>
#     <tr>
#       <th>18</th>
#       <td>25952000</td>
#       <td>47</td>
#     </tr>
#     <tr>
#       <th>19</th>
#       <td>23328000</td>
#       <td>39</td>
#     </tr>
#     <tr>
#       <th>20</th>
#       <td>27267000</td>
#       <td>41</td>
#     </tr>
#     <tr>
#       <th>21</th>
#       <td>30219000</td>
#       <td>49</td>
#     </tr>
#     <tr>
#       <th>22</th>
#       <td>27143000</td>
#       <td>48</td>
#     </tr>
#     <tr>
#       <th>23</th>
#       <td>24859000</td>
#       <td>42</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="pHYi3jvZFxUk"
pivot_2 = pd.pivot_table(payments, index = '신청날짜(시)', values = '금액(int)', aggfunc = ['sum','count'])
pivot_2

# + [markdown] colab_type="text" id="h8glthrTFxUp"
# DS School 수강생들의 대부분이 직장인임을 감안할 때, 일별, 시간별 결제금액을 보고 '직장인들이 주로 근무시간에 결제를 결심한다.' 라는 합리적인 가설을 세울 수 있습니다. 이 가설은 점심시간대인 12시부터 1시 사이에 급격하게 감소하는 것을 통해 더 지지받을 수 있습니다.
#
# 이를 바탕으로 콘텐츠 제작자에게 근무시간에 딴 짓을 하는 직장인들을 타겟팅하는 콘텐츠를 제작해달라고 요청할 수 있습니다. 또한, 페이스북이 제공하는 광고 시간 타겟팅 기능을 이용하여 근무시간대에 들어가는 광고예산의 비중을 늘릴 수도 있습니다.
#

# + [markdown] colab_type="text" id="ntl9EcFXFxUq"
# ---

# + [markdown] colab_type="text" id="whxCzzUCFxUq"
# **7. 사용자의 니즈를 바탕으로 향후 오픈할 강의의 우선순위를 정하려고 합니다. 설문조사 데이터에서 답변을 정리해서 보여주세요.**
#
# 우선, 각 질문과 답변의 내용은 다음과 같습니다.

# + [markdown] colab_type="text" id="VRGQ3ovrFxUs"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>question_text</th>
#       <th>answer1_text</th>
#       <th>answer2_text</th>
#       <th>answer3_text</th>
#       <th>answer4_text</th>
#       <th>answer5_text</th>
#       <th>answer6_text</th>
#       <th>answer7_text</th>
#       <th>answer8_text</th>
#       <th>answer9_text</th>
#       <th>answer10_text</th>
#       <th>answer11_text</th>
#       <th>answer12_text</th>
#     </tr>
#     <tr>
#       <th>question_id</th>
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
#       <td>데이터 사이언스를 배우고 싶은 이유는 무엇인가요?</td>
#       <td>현재 다니는 직장에서 즉시 활용할만한 데이터 관련 지식을 습득하기 위해</td>
#       <td>데이터와 인공지능 관련 석사/박사로 진학하기 위해</td>
#       <td>풀타임 데이터 사이언티스트로 취업/이직을 하기 위해</td>
#       <td>기술 창업을 위한 원천기술을 습득하기 위해</td>
#       <td>최신 데이터사이언스 트렌드에 관심이 있어서</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>이전까지 수학, 통계학, 프로그래밍에 관한 공부를 얼만큼 하셨나요?</td>
#       <td>최근 2~3년간 수학, 통계학 공부를 해 본 적이 없으며, 프로그래밍 역시 해 본 ...</td>
#       <td>수학과 통계학은 자신 없지만, 프로그래밍은 조금 해 보았다.</td>
#       <td>최근까지 수학과 통계학을 공부해왔지만, 프로그래밍은 해 본 적 없다.</td>
#       <td>수학과 통계학을 공부하였으며, 프로그래밍도 할 줄 안다.</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>데이터 사이언스를 어디에 활용하고 싶으신가요? (복수 선택 가능)</td>
#       <td>상품, 컨텐츠 추천 엔진을 구현하고 싶다. (ex: 의류, 영화, 음악 추천 등)</td>
#       <td>주가를 분석하고 예측할 수 있는 방법을 알고 싶다. (ex: 주가 등락, 비트코인 ...</td>
#       <td>부동산 시세와 그 등락을 예측하고 싶다. (ex: 아파트, 점포, 오피스텔 등)</td>
#       <td>텍스트 데이터를 적극 활용해보고 싶다. (ex: 스팸 필터링, 검색 엔진, 법률/판...</td>
#       <td>이미지 데이터를 다뤄보고 싶다. (ex: 얼굴 인식, 자동차 표시판 분석 등)</td>
#       <td>온라인 커머스에서 판매하는 상품의 재구매율을 늘리고 싶다.</td>
#       <td>정기 구독 상품의 구독 이탈률(Churn Rate)을 낮출 수 있는 방법을 알고 싶다.</td>
#       <td>마케팅 데이터를 분석하여, 온라인 마케팅의 효율을 높이고 싶다.</td>
#       <td>해상사고나 범죄를 분석/예측하여 그 비율을 낮추고 싶다.</td>
#       <td>의료 데이터나 신약 분석 등에 활용하고 싶다.</td>
#       <td>공공데이터를 활용하는데 도움이 되고 싶다.</td>
#       <td>기타</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>수강을 하면서 과제를 어느정도까지 완수하실 수 있으신가요?</td>
#       <td>현재 하는 일이 바빠서, 과제가 주어지면 전혀 할 수가 없다.</td>
#       <td>여가시간을 활용하여 무리하지 않는 선에서 어느정도의 과제는 해결할 수 있다.</td>
#       <td>다소 시간이 넉넉하기 때문에 많은 과제가 주어진다고 해도 충분히 완수할 수 있다.</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>5</th>
#       <td>DS School의 과정을 마친 후 데이터를 얼만큼 잘 다루고 싶은가요?</td>
#       <td>취미로 데이터를 다뤄볼 수 있을 정도면 충분하다.</td>
#       <td>대학원 연구실에 가도 뒤쳐지지 않을 만큼 이론과 실전 경험을 쌓고 싶다.</td>
#       <td>현재 다니는 회사에서 데이터 관련 업무를 병행할 수 있을 만큼 실력을 쌓고 싶다.</td>
#       <td>풀타임 데이터 사이언티스트로 취업/이직할 수 있을 만큼 실력을 쌓고 싶다.</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>6</th>
#       <td>수업은 어느 시간을 선호하시나요? (중복 선택 가능)</td>
#       <td>주중 아침</td>
#       <td>주중 낮</td>
#       <td>주중 저녁</td>
#       <td>주말 아침</td>
#       <td>주말 낮</td>
#       <td>주말 저녁</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>7</th>
#       <td>수업을 듣는 기간동안 얼만큼 시간을 할애할 수 있나요?</td>
#       <td>현재 하는 일에 지장이 없는 선에서, 파트타임으로 수업을 들을 수 있다.</td>
#       <td>현재 하는 일은 쉬는 한이 있더라도, 풀타임으로 수업을 듣고 싶다.</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#   </tbody>
# </table>

# + [markdown] colab_type="text" id="kHWAX9l2FxUt"
# 고객들이 데이터 사이언스를 어디에 활용하고 싶은지에 대한 이유를 정리하기 위해서는 1번 3번 질문에 대한 정답을 정리해서 보여주어야 합니다. 판다스의 피벗 테이블을 이용하여 1번, 3번 질문에 대한 응답을 정리해서 보여주세요. 

# + [markdown] colab_type="text" id="hJ-yGksUFxUu"
# 완성된 피벗 테이블은 다음과 같은 모양이 나와야 합니다.
#
# **주의** : 혹시 결과가 아래와 다르다면 1번, 2번 문제에서 sorting이나 `drop_duplicate()`가 잘 되어있지 않을 가능성이 큽니다.

# + [markdown] colab_type="text" id="r6uN910hFxUv"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>answer1_selected(bool)</th>
#       <th>answer2_selected(bool)</th>
#       <th>answer3_selected(bool)</th>
#       <th>answer4_selected(bool)</th>
#       <th>answer5_selected(bool)</th>
#       <th>answer6_selected(bool)</th>
#       <th>answer7_selected(bool)</th>
#       <th>answer8_selected(bool)</th>
#       <th>answer9_selected(bool)</th>
#       <th>answer10_selected(bool)</th>
#       <th>answer11_selected(bool)</th>
#       <th>answer12_selected(bool)</th>
#     </tr>
#     <tr>
#       <th>question_id</th>
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
#       <td>0.321978</td>
#       <td>0.093082</td>
#       <td>0.238010</td>
#       <td>0.074705</td>
#       <td>0.272225</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.00000</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>0.372238</td>
#       <td>0.313507</td>
#       <td>0.211327</td>
#       <td>0.371489</td>
#       <td>0.244438</td>
#       <td>0.215821</td>
#       <td>0.141958</td>
#       <td>0.437186</td>
#       <td>0.103079</td>
#       <td>0.173421</td>
#       <td>0.356281</td>
#       <td>0.12368</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="Hk989fBXFxUv"
#리스트 안에 for 문을 넣을 수 있습니다.
answer_list = [f"answer{i}_selected(bool)" for i in range(1, 13)]

# + colab={} colab_type="code" id="Yk9TedbYFxUz"
func = lambda x : x.sum()/x.count()
pivot_3 = pd.pivot_table(surveys, index = 'question_id', values = answer_list, aggfunc = func)
pivot_3 = pivot_3[answer_list].loc[[1,3]]
pivot_3

# + [markdown] colab_type="text" id="5FlkkCIdFxU6"
# 1번 질문에는 1번 응답 (현재 다니는 직장에서 데이터 사이언스를 활용하기 위해) 가 가장 높은 답변을 받았고, 3번 질문에서는 8번 응답 (마케팅 데이터를 분석하여 마케팅의 효율을 높이고 싶다.)가 가장 높은 응답을 받았습니다.
#
# 하지만, 최종 목표는 결제 유도이기 때문에, 모든 설문조사를 완료한 사람이 아닌 결제를 완료한 사람들의 결과만을 가지고 분석해야 합니다. 이를 위해 surveys 테이블과 payments 테이블을 병합할 필요가 있습니다.

# + [markdown] colab_type="text" id="VwgG2HkoFxU8"
# ---

# + [markdown] colab_type="text" id="7zQpuqZ2FxU9"
# **8. 결제 데이터와 유저 데이터에는 동일한 id (payment_id), 유저 데이터와 설문조사 데이터에는 동일한 id (user_id)가 존재합니다. 각자 가져와서 pandas merge로 해주세요.**

# + [markdown] colab_type="text" id="wcVBslzwFxU-"
# 필요한 것은 결제 데이터와 설문조사 데이터를 조인하는 것이지만, 각각에게 필요한 id가 유저 테이블에 존재하는 상황입니다. 따라서 merge를 2번 해야 결제 데이터와 설문조사 데이터를 합칠 수 있는 상황입니다.
#
# 우선 결제 데이터와 유저 데이터를 이메일을 기준으로 조인해주세요. 그 후에 설문조사 데이터를 조인해주시면 필요로 하는 데이터프레임이 완성이 됩니다.

# + [markdown] colab_type="text" id="phiTTZLIFxU_"
# 병합 2번이 완료된 경우 다음과 같은 테이블이 나오게 됩니다.

# + [markdown] colab_type="text" id="U9SKjbUGFxVA"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>payment_id_x</th>
#       <th>이름</th>
#       <th>이메일</th>
#       <th>연락처</th>
#       <th>신청날짜</th>
#       <th>신청수업</th>
#       <th>금액</th>
#       <th>결제방법</th>
#       <th>상태</th>
#       <th>연락처(clean)</th>
#       <th>기수</th>
#       <th>수업타입</th>
#       <th>상태(bool)</th>
#       <th>신청날짜(연)</th>
#       <th>신청날짜(월)</th>
#       <th>신청날짜(일)</th>
#       <th>신청날짜(시)</th>
#       <th>신청날짜(분)</th>
#       <th>신청날짜(초)</th>
#       <th>신청날짜(요일)</th>
#       <th>금액(int)</th>
#       <th>user_id</th>
#       <th>mixpanel_id</th>
#       <th>payment_id_y</th>
#       <th>email</th>
#       <th>survey_id</th>
#       <th>question_id</th>
#       <th>answer1_selected</th>
#       <th>answer2_selected</th>
#       <th>answer3_selected</th>
#       <th>answer4_selected</th>
#       <th>answer5_selected</th>
#       <th>answer6_selected</th>
#       <th>answer7_selected</th>
#       <th>answer8_selected</th>
#       <th>answer9_selected</th>
#       <th>answer10_selected</th>
#       <th>answer11_selected</th>
#       <th>answer12_selected</th>
#       <th>created_at</th>
#       <th>updated_at</th>
#       <th>answer1_selected(bool)</th>
#       <th>answer2_selected(bool)</th>
#       <th>answer3_selected(bool)</th>
#       <th>answer4_selected(bool)</th>
#       <th>answer5_selected(bool)</th>
#       <th>answer6_selected(bool)</th>
#       <th>answer7_selected(bool)</th>
#       <th>answer8_selected(bool)</th>
#       <th>answer9_selected(bool)</th>
#       <th>answer10_selected(bool)</th>
#       <th>answer11_selected(bool)</th>
#       <th>answer12_selected(bool)</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>aiym79ous7l8</td>
#       <td>고세준</td>
#       <td>0usbs4knns0s@dsschool.co.kr</td>
#       <td>01056007186</td>
#       <td>2018-01-31 15:42:20</td>
#       <td>입문반 22기</td>
#       <td>495,000</td>
#       <td>카드결제</td>
#       <td>결제 완료</td>
#       <td>NaN</td>
#       <td>22기</td>
#       <td>입문반</td>
#       <td>True</td>
#       <td>2018</td>
#       <td>1</td>
#       <td>31</td>
#       <td>15</td>
#       <td>42</td>
#       <td>20</td>
#       <td>Wednesday</td>
#       <td>495000</td>
#       <td>drdi7xmsj0nm</td>
#       <td>NPAFFXASZPACSNMVVRGCKPBKPZQDCKMUUCTCAFRJXFWGGL...</td>
#       <td>None</td>
#       <td>0usbs4knns0s@dsschool.co.kr</td>
#       <td>nnvz4nsy03ob</td>
#       <td>1</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-01-31 06:15:13.343156</td>
#       <td>2018-01-31 06:15:13.343156</td>
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
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>aiym79ous7l8</td>
#       <td>고세준</td>
#       <td>0usbs4knns0s@dsschool.co.kr</td>
#       <td>01056007186</td>
#       <td>2018-01-31 15:42:20</td>
#       <td>입문반 22기</td>
#       <td>495,000</td>
#       <td>카드결제</td>
#       <td>결제 완료</td>
#       <td>NaN</td>
#       <td>22기</td>
#       <td>입문반</td>
#       <td>True</td>
#       <td>2018</td>
#       <td>1</td>
#       <td>31</td>
#       <td>15</td>
#       <td>42</td>
#       <td>20</td>
#       <td>Wednesday</td>
#       <td>495000</td>
#       <td>drdi7xmsj0nm</td>
#       <td>NPAFFXASZPACSNMVVRGCKPBKPZQDCKMUUCTCAFRJXFWGGL...</td>
#       <td>None</td>
#       <td>0usbs4knns0s@dsschool.co.kr</td>
#       <td>ihb40hmj9393</td>
#       <td>2</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-01-31 06:15:23.300754</td>
#       <td>2018-01-31 06:15:23.300754</td>
#       <td>False</td>
#       <td>False</td>
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
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>aiym79ous7l8</td>
#       <td>고세준</td>
#       <td>0usbs4knns0s@dsschool.co.kr</td>
#       <td>01056007186</td>
#       <td>2018-01-31 15:42:20</td>
#       <td>입문반 22기</td>
#       <td>495,000</td>
#       <td>카드결제</td>
#       <td>결제 완료</td>
#       <td>NaN</td>
#       <td>22기</td>
#       <td>입문반</td>
#       <td>True</td>
#       <td>2018</td>
#       <td>1</td>
#       <td>31</td>
#       <td>15</td>
#       <td>42</td>
#       <td>20</td>
#       <td>Wednesday</td>
#       <td>495000</td>
#       <td>drdi7xmsj0nm</td>
#       <td>NPAFFXASZPACSNMVVRGCKPBKPZQDCKMUUCTCAFRJXFWGGL...</td>
#       <td>None</td>
#       <td>0usbs4knns0s@dsschool.co.kr</td>
#       <td>p9p9ygppdbel</td>
#       <td>3</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>2018-01-31 06:15:45.486897</td>
#       <td>2018-01-31 06:15:45.486897</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>True</td>
#       <td>True</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>False</td>
#       <td>True</td>
#       <td>False</td>
#     </tr>
#   </tbody>
# </table>

# + [markdown] colab_type="text" id="PcQjQDobFxVB"
# 우선 users 테이블을 쿼리를 이용해 불러와주세요, 그 다음 payments와 users가 병합된 테이블에 다시 surveys를 병합합니다. 모든 병합은 inner로 진행합니다.

# + colab={} colab_type="code" id="tiR3sAaEFxVC"
query = "SELECT * FROM 'users'"

users = pd.read_sql(query, connect)

users.head()
# -

tmp = pd.merge(payments, users, left_on='이메일', right_on='email')
paid_survey = pd.merge(tmp, surveys, on = 'user_id')
paid_survey.head(3)

# + [markdown] colab_type="text" id="O1OsUYLRFxVG"
# ---

# + [markdown] colab_type="text" id="i8Sq-wpiFxVH"
# **9. 결제 데이터와 유저 데이터에는 동일한 id (e-mail), 유저 데이터와 설문조사 데이터에는 동일한 id (user_id)가 존재합니다. 각자 가져와서 SQL join으로 합쳐주세요.**

# + [markdown] colab_type="text" id="wWft13WpFxVI"
# 위와 똑같은 문제를 쿼리문을 이용해 풀어보도록 하겠습니다.
#
# 실제 데이터가 방대한 경우 users와 payments를 불러온 다음에 통합하는 것보다는 쿼리문으로 필요한 것만 골라서 받아오는 것이 자원활용을 효율적으로 할 수 있는 방법입니다.

# + [markdown] colab_type="text" id="W20jVaeBFxVJ"
# `SELECT () FROM () INNER JOIN () ON () INNER JOIN () ON ()`  구조의 쿼리문을 작성해주세요.

# + [markdown] colab_type="text" id="l8XMLwXqFxVK"
# 결과는 다음과 같이 나옵니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>payment_id</th>
#       <th>이름</th>
#       <th>이메일</th>
#       <th>연락처</th>
#       <th>신청날짜</th>
#       <th>신청수업</th>
#       <th>금액</th>
#       <th>결제방법</th>
#       <th>상태</th>
#       <th>user_id</th>
#       <th>mixpanel_id</th>
#       <th>payment_id</th>
#       <th>email</th>
#       <th>survey_id</th>
#       <th>user_id</th>
#       <th>question_id</th>
#       <th>answer1_selected</th>
#       <th>answer2_selected</th>
#       <th>answer3_selected</th>
#       <th>answer4_selected</th>
#       <th>answer5_selected</th>
#       <th>answer6_selected</th>
#       <th>answer7_selected</th>
#       <th>answer8_selected</th>
#       <th>answer9_selected</th>
#       <th>answer10_selected</th>
#       <th>answer11_selected</th>
#       <th>answer12_selected</th>
#       <th>created_at</th>
#       <th>updated_at</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>5vtq11wow61w</td>
#       <td>한서훈</td>
#       <td>3xy4zzr6k13x@dsschool.co.kr</td>
#       <td>01040513577</td>
#       <td>2018-01-03 14:44:12</td>
#       <td>입문반 19기</td>
#       <td>495,000</td>
#       <td>카드결제</td>
#       <td>결제 완료</td>
#       <td>orqcrchp0s2a</td>
#       <td>OJRXJURAXLJMMAWURTWSNBUJIRJJIVSHDHBBBPORBVRPPQ...</td>
#       <td>None</td>
#       <td>3xy4zzr6k13x@dsschool.co.kr</td>
#       <td>dt9gwdq9od02</td>
#       <td>orqcrchp0s2a</td>
#       <td>6</td>
#       <td>f</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>f</td>
#       <td>f</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-01-03 05:42:02.303657</td>
#       <td>2018-01-03 05:42:02.303657</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>209h7wqy7bdf</td>
#       <td>김재호</td>
#       <td>ao6kez00wxnh@dsschool.co.kr</td>
#       <td>010-6880-0251</td>
#       <td>2017-10-22 08:53:29</td>
#       <td>입문반 11기</td>
#       <td>495,000</td>
#       <td>카드결제</td>
#       <td>결제 완료</td>
#       <td>54ojyvp8ergj</td>
#       <td>REPODOLMGTJDYQVHMHOSDVDCLCXWQSKSJMUGCMXTTJBZSP...</td>
#       <td>None</td>
#       <td>ao6kez00wxnh@dsschool.co.kr</td>
#       <td>51yza3u3obtk</td>
#       <td>54ojyvp8ergj</td>
#       <td>6</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>t</td>
#       <td>t</td>
#       <td>t</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-01-06 08:47:19.325152</td>
#       <td>2018-01-06 08:47:19.325152</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>uh701zm4irgx</td>
#       <td>김재호</td>
#       <td>ao6kez00wxnh@dsschool.co.kr</td>
#       <td>010-7202-2433</td>
#       <td>2017-12-21 16:47:00</td>
#       <td>딥러닝 2기</td>
#       <td>1,043,000</td>
#       <td>카드결제</td>
#       <td>결제 완료</td>
#       <td>54ojyvp8ergj</td>
#       <td>REPODOLMGTJDYQVHMHOSDVDCLCXWQSKSJMUGCMXTTJBZSP...</td>
#       <td>None</td>
#       <td>ao6kez00wxnh@dsschool.co.kr</td>
#       <td>51yza3u3obtk</td>
#       <td>54ojyvp8ergj</td>
#       <td>6</td>
#       <td>f</td>
#       <td>f</td>
#       <td>t</td>
#       <td>t</td>
#       <td>t</td>
#       <td>t</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>None</td>
#       <td>2018-01-06 08:47:19.325152</td>
#       <td>2018-01-06 08:47:19.325152</td>
#     </tr>
#   </tbody>
# </table>

# +
query = "SELECT * FROM 'payments' inner join 'users' on payments.이메일 = users.email inner join 'surveys' on users.user_id = surveys.user_id"

paid_survey2 = pd.read_sql(query, connect)
paid_survey2.head(3)

# + [markdown] colab_type="text" id="ZRAfx6fBFxVQ"
# ---

# + [markdown] colab_type="text" id="gBPdLrnGFxVS"
# **10. 8번에서 merging한 데이터 중 필요한 컬럼만 추려주세요. 그리고 데이터를 클리닝해주세요.**

# + [markdown] colab_type="text" id="u96OELFkFxVT"
# 모든 테이블을 병합한 상태이기 때문에 데이터의 컬럼이 과도하게 많은 상태입니다. 모든 컬럼을 분석에 사용할 필요가 없기 때문에 사용할 컬럼만 골라 데이터를 슬라이싱하려고 합니다. 사용할 컬럼을 아래에 적어놓았습니다. 컬럼명이 다른 경우 수정해서 사용해주세요.

# + colab={} colab_type="code" id="bb6_326SFxVU"
# 분석에 필요한 컬럼들의 리스트입니다.
selected_columns = ['user_id',  '이름', '연락처', '이메일', '신청수업', '금액(int)', '결제방법', '신청날짜', '상태(bool)', 'mixpanel_id']

selected_columns += [
    'question_id',
    'answer1_selected(bool)', 'answer2_selected(bool)', 'answer3_selected(bool)',
    'answer4_selected(bool)', 'answer5_selected(bool)', 'answer6_selected(bool)',
    'answer7_selected(bool)', 'answer8_selected(bool)', 'answer9_selected(bool)',
    'answer10_selected(bool)', 'answer11_selected(bool)', 'answer12_selected(bool)'
]

selected_columns += [
    'created_at', 'updated_at'
]

#위의 리스트를 이용하여 데이터에 필요한 컬럼만 남겨주세요.

selected_paid_survey = paid_survey[selected_columns]
selected_paid_survey.head(3)

# + [markdown] colab_type="text" id="Ry9zrlQGFxVa"
# 사용하고 있는 데이터는 payments_complete와 surveys를 병합한 데이터로 전부 결제를 완료한 사람들의 설문조사 데이터입니다. 하지만, 결제를 한 이후에도 설문조사를 하신 경우 있고 한 사람이 여러번 설문조사를 한 경우가 있는데 결제를 한 이후에도 설문조사를 한 경우는 삭제하고 여러번 설문조사를 한 경우는 첫번째 설문 조사만 남기고 중복정보도 제거해주어야 합니다.
#
# 먼저 신청날짜와 created_at 컬럼을 이용하여 결제를 한 이후에도 설문조사를 한 경우는 삭제하여 주세요. 또한, 이메일과 신청수업, question_id 3개가 중복되는 경우는 drop_duplicates()를 이용해 최신의 정보만 남겨주세요. 중복을 제거하고 남길 데이터를 선택하는 방법은 keep 옵션을 활용하면 됩니다. **단 중복제거하기 전에 "이메일", "question_id", "created_at" 컬럼을 기준으로 sorting 해야 합니다.**

# + colab={} colab_type="code" id="fJF5_ioMFxVb"
selected_paid_survey.drop(selected_paid_survey.loc[selected_paid_survey['신청날짜'] < selected_paid_survey['created_at']].index, inplace = True)
selected_paid_survey
# -

selected_paid_survey = selected_paid_survey.sort_values(by = ["이메일", "question_id", "created_at"])
selected_paid_survey.drop_duplicates(['이메일', '신청수업', 'question_id'], keep = 'last', inplace=True)
selected_paid_survey.shape

# + [markdown] colab_type="text" id="7HDuNlKyFxVg"
# ---

# + [markdown] colab_type="text" id="Ou7RSweNFxVh"
# **11. 위에서 정리한 결과를 바탕으로 결제를 한 사람들의 설문조사 1,3번 응답결과를 정리해주세요.**

# + [markdown] colab_type="text" id="DmxT2kRcFxVi"
# 이 문제를 풀기 위해 많은 전처리 과정을 거쳐왔습니다. 실제로 결제를 한 사람들의 1,3번 질문 대답을 피벗 테이블을 이용하여 정리해주세요. 그리고, 설문조사를 완료한 모든 사람의 결과와 이를 비교해주세요.

# + [markdown] colab_type="text" id="cF459eh6FxVj"
# 정리를 마칠 경우 아래와 같은 결과가 나오게 됩니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>answer1_selected(bool)</th>
#       <th>answer2_selected(bool)</th>
#       <th>answer3_selected(bool)</th>
#       <th>answer4_selected(bool)</th>
#       <th>answer5_selected(bool)</th>
#       <th>answer6_selected(bool)</th>
#       <th>answer7_selected(bool)</th>
#       <th>answer8_selected(bool)</th>
#       <th>answer9_selected(bool)</th>
#       <th>answer10_selected(bool)</th>
#       <th>answer11_selected(bool)</th>
#       <th>answer12_selected(bool)</th>
#     </tr>
#     <tr>
#       <th>question_id</th>
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
#       <td>0.314103</td>
#       <td>0.115385</td>
#       <td>0.262821</td>
#       <td>0.076923</td>
#       <td>0.230769</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#       <td>0.000000</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>0.474359</td>
#       <td>0.391026</td>
#       <td>0.269231</td>
#       <td>0.429487</td>
#       <td>0.294872</td>
#       <td>0.262821</td>
#       <td>0.217949</td>
#       <td>0.410256</td>
#       <td>0.121795</td>
#       <td>0.211538</td>
#       <td>0.391026</td>
#       <td>0.147436</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="wp037q4XFxVk"
pivot_tmp = pd.pivot_table(selected_paid_survey, index = 'question_id', values = selected_paid_survey.columns[11:-2], aggfunc = 'mean')
pivot_tmp2 = pivot_tmp[selected_paid_survey.columns[11:-2]].loc[[1,3]]
pivot_tmp2

# + [markdown] colab_type="text" id="Q0uw0KfHFxVo"
# 이제 위의 결과와 비교를 해야합니다. 표 2개를 놓고 직접적으로 비교하는 방법도 있지만, 역시 그래프로 비교하는 것이 더 직관적인 경우도 있습니다.
#
# 지금의 경우도 마찬가지로 그래프로 둘의 차이를 비교하는 것이 훨씬 보기 좋습니다. 판다스에서는 기본으로 데이터프레임에서 `plot()`메소드를 제공합니다. 이는 내부적으로 matplotlib이라는 시각화 툴을 불러와 그래프를 그려줍니다. 이 plot 메소드를 이용해 데이터프레임을 쉽게 그래프로 변환할 수 있습니다. 시각화에 관련된 상세한 내용은 3주차에 다루도록 하겠습니다. DataFrame.plot()에 관련된 옵션은 [다음 링크](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html)를 참조해주세요.

# + [markdown] colab_type="text" id="39BXCbr9FxVq"
# 모든 설문조사 데이터로 수행한 위에서 만든 결과와 결제한 사람들의 설문조사 결과를 DataFrame.plot()을 이용해 비교해주세요. 적절한 그래프의 종류를 설정하는 것이 중요합니다. kind와 legend 옵션만을 이용했을 때, 다음과 같은 결과가 나옵니다.
#
# <img src="https://i.imgur.com/k1ooH1g.png" width="400">

# + colab={} colab_type="code" id="CFctrewAFxVq"
# 그래프를 주피터 화면에 띄우기 위한 주피터 명령어입니다.
# %matplotlib inline
pivot_3.plot(kind='bar', legend = False)
pivot_tmp2.plot(kind='bar', legend = False)

# + [markdown] colab_type="text" id="IrSRX7OSFxVw"
# 모든 설문조사 결과와 결제한 사람들의 설문조사 결과는 상당히 비슷한 양상을 보입니다. 그런데, 1번 질문의 5번 응답 '최신 데이터사이언스 트렌드에 관심이 있어서' 응답을 한 경우는 결제율이 낮다는 것을 알 수 있습니다. 
#
# 아무래도 고가의 강의이다 보니, 관심만 있는 정도로는 구매로의 전환이 쉽게 일어나지 않습니다.
# 1번 응답 (현재 다니는 직장에서 데이터 사이언스를 활용하기 위해)의 비율이 압도적으로 높고, 두 번째는 전업 데이터 사이언티스트로 이직/전직하기 입니다. 
#
# 모든 사람을 대상 설문조사 결과와 결제자 대상 설문조사 결과를 3번 질문에서도 비교해 봤을 때, 응답 8번 또한 눈에 띄게 줄어든 것을 확인할 수 있습니다. 8번의 응답은 '마케팅 데이터를 분석하여 마케팅의 효율을 높이기' 입니다. 이를 바탕으로 마케팅에 관심이 있는 사람들은 데이터 마케팅 강의로 이탈하거나 사이언스 강의를 수강하지 않는다고 생각할 수 있습니다. 
#
# 현재 설문조사 결과를 종합해봤을 떄, 직장에서 업무에 데이터 사이언스를 활용하면서 '추천 시스템'을 만들거나 텍스트 데이터를 다루는 것에 대한 수요가 매우 높음을 확인할 수 있습니다.
#
# 엑셀에도 텍스트를 다룰 수 있는 기능들이 많이 있지만, 파이썬은 다양한 오픈소스와 함께 자유도가 높아 잘만 배워둔다면 엑셀에 비해 텍스트를 훨씬 쉽게 다룰 수 있습니다. 
#
# 또한, 카카오 같은 플랫폼 사업자나 여러 이커머스 기업들은 추천시스템 연구를 꾸준히 진행하고 있고 그 수요도 몹시 높은 편입니다. 이를 통해 향후 제작할 컨텐츠에서 텍스트나 추천시스템의 비중을 늘려볼까 합니다.

# + [markdown] colab_type="text" id="ztw-WAjxFxVx"
# ---

# + [markdown] colab_type="text" id="L-p9LiCFFxVx"
# **12. created_at은 세션이 생성된 시간이고 '신청날짜'는 실제로 수업을 신청한 시간입니다. DS School 홈페이지에 처음 접근한 순간부터 결제까지 걸린 시간을 계산해주세요. 단, 신청날짜가 created_at보다 작은(먼저인) 경우가 있는데 이를 제외하고 구해주세요.**

# + [markdown] colab_type="text" id="xNv-l9oTFxVy"
# 대부분의 사용자가 DS School 홈페이지에 접속하자마자 결제를 하는 것이 아닌, 충분한 고민 후에 결제를 진행합니다. 사람들이 결제를 하는데까지 고민하는 시간을 잘 정리한다면 마케팅 부서에서 리타게팅 전략을 펼칠 때 소중한 자료로 활용할 수 있을 것입니다.

# + [markdown] colab_type="text" id="zg40DwT4FxVz"
# `신청날짜`와 `created_at`을 이용하여 결제소요시간에 해당하는 시리즈 데이터를 만들어주세요. 결과는 다음과 같은 모양이 나옵니다.
#
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>time</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>887</th>
#       <td>09:14:16.752474</td>
#     </tr>
#     <tr>
#       <th>888</th>
#       <td>09:14:12.718888</td>
#     </tr>
#     <tr>
#       <th>889</th>
#       <td>09:13:59.302001</td>
#     </tr>
#     <tr>
#       <th>890</th>
#       <td>09:13:55.157445</td>
#     </tr>
#     <tr>
#       <th>891</th>
#       <td>09:13:51.359780</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="NaMLWpgpFxV0"
time = selected_paid_survey['신청날짜']-selected_paid_survey['created_at']
time

# + [markdown] colab_type="text" id="3Ri_wq9ZFxV7"
# 예를 들어 09:14:16의 경우에는 9시간 14분 16초 걸렸다는 의미입니다. 이를 쉽게 그래프화 하기 위해 .dt를 이용하여 일 단위로 환산해 줍시다.
# 9시간 14분 16초를 일로 환산한다면 0.384907일 이 됩니다.

# + colab={} colab_type="code" id="IhLT9nTZFxV8"
time2 = time/pd.to_timedelta(1, unit='D')
time2

# + [markdown] colab_type="text" id="xoew-Eg_FxWC"
# 위에서 만든 데이터를 시각화를 통해 정리하려고 합니다. 우리가 얻고 싶은 결과는 a%의 고객은 세션 생성후 b일 안에 결제한다. 라는 함수를 만들어내는 것입니다. 이를 위해서 seaborn의 distplot을 사용합니다.

# + colab={} colab_type="code" id="3TCzsbeuFxWC"
#그래프를 그리기 위한 library를 불러옵니다.
import seaborn as sns
import matplotlib.pyplot as plt

# + colab={} colab_type="code" id="E7ijKPV7FxWH"
# seaborn의 경우 테마설정을 다음과 같이 할 수 있습니다. 사전 구성된 테마는 다음과 같습니다. {darkgrid, whitegrid, dark, white, ticks}
sns.set_style("whitegrid", {'grid.linestyle': '--'})

# + [markdown] colab_type="text" id="5Q3_YG6lFxWN"
# sns.distplot을 이용해 분포 그래프를 그려주세요. 그래프의 모양이 아래와 비슷하게 나오면 됩니다.

# + [markdown] colab_type="text" id="-_MoIQn1FxWO"
# <img src='https://i.imgur.com/O57UhVX.png' width=600>

# + colab={} colab_type="code" id="Te-cdZt_FxWP"
# distplot을 그려주세요, kde_kws={'cumulative' : True} 옵션을 통해 누적분포를 그리는 것이 좋습니다. 또한, hist=False로 하는 것이 보기에 좋을 수 있습니다.
plt.figure(figsize = (12,4))
sns.distplot(time2, kde_kws={'cumulative' : True}, hist = False)

# + [markdown] colab_type="text" id="L7U_y2YuFxWW"
# 위의 분포를 통해 결제를 한 사람들 중 80% 이상이 10일 이내 결제, 그리고 나머지 20%는 훨씬 많은 고민을 한다는 것을 파악할 수 있습니다. 이를 통해 DS School에 관심을 가졌지만 아직 결제를 하지 않은 잠재고객들의 결제 가능성을 역으로 추정해 리타겟팅 전략의 예산 분배를 진행할 수 있습니다. 
#
# ---

# + [markdown] colab_type="text" id="za3SBhk1FxWY"
# **13. 믹스패널 데이터를 불러와 주세요. 그리고 이를 users와 payments 테이블과 병합해주세요.** 

# + [markdown] colab_type="text" id="UT0E-2IvFxWZ"
# 이번엔 마케팅 캠페인별 효율을 믹스패널 데이터를 이용해 비교분석하려고 합니다. 마케팅을 진행할 때, 사후분석을 위해 링크에 utm 파라미터들을 추가합니다. utm 파라미터에 대한 소개는 [다음 링크](https://brunch.co.kr/@jiyeonsongofnt/13) 를 참조해주세요. utm_campaign 파라미터에 캠페인 별로 값을 입력해놓으면 유입된 사용자를 캠페인 별로 추적하는 것이 가능해집니다.
#
# 우선 mixpanel 데이터를 `pd.read_csv()`를 이용해 읽어와주세요. 그 다음, mixpanel_id를 이용해 users 테이블과 병합, payment_id를 이용해 payments와 병합해주세요. users와는 inner, payments와는 믹스패널이 left가 되도록 하여 병합해주세요.
#
# 결과는 다음과 같이 나오게 됩니다.
#
#

# + [markdown] colab_type="text" id="XjwmUUIYFxWb"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>class_name</th>
#       <th>created_at</th>
#       <th>initial_referring_domain</th>
#       <th>utm_campaign [first touch]</th>
#       <th>utm_campaign [last touch]</th>
#       <th>utm_content [first touch]</th>
#       <th>utm_content [last touch]</th>
#       <th>utm_medium [first touch]</th>
#       <th>utm_medium [last touch]</th>
#       <th>utm_source [first touch]</th>
#       <th>utm_source [last touch]</th>
#       <th>utm_term [first touch]</th>
#       <th>utm_term [last touch]</th>
#       <th>initial_referrer</th>
#       <th>last_seen</th>
#       <th>os</th>
#       <th>browser</th>
#       <th>city</th>
#       <th>country_code</th>
#       <th>distinct_id</th>
#       <th>user_id</th>
#       <th>mixpanel_id</th>
#       <th>payment_id</th>
#       <th>email</th>
#       <th>이름</th>
#       <th>이메일</th>
#       <th>연락처</th>
#       <th>신청날짜</th>
#       <th>신청수업</th>
#       <th>금액</th>
#       <th>결제방법</th>
#       <th>상태</th>
#       <th>연락처(clean)</th>
#       <th>기수</th>
#       <th>수업타입</th>
#       <th>상태(bool)</th>
#       <th>신청날짜(연)</th>
#       <th>신청날짜(월)</th>
#       <th>신청날짜(일)</th>
#       <th>신청날짜(시)</th>
#       <th>신청날짜(분)</th>
#       <th>신청날짜(초)</th>
#       <th>신청날짜(요일)</th>
#       <th>금액(int)</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>NaN</td>
#       <td>2017-09-01T09:27:57</td>
#       <td> direct</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td> direct</td>
#       <td>2017-09-01T09:30:07</td>
#       <td>Android</td>
#       <td>Chrome</td>
#       <td>Seoul</td>
#       <td>KR</td>
#       <td>DEDFPJKWKNGOKXACEKRZQZUXDPBCJYHQKHWPBSQMCJCJUC...</td>
#       <td>j81umpsxbqer</td>
#       <td>DEDFPJKWKNGOKXACEKRZQZUXDPBCJYHQKHWPBSQMCJCJUC...</td>
#       <td>None</td>
#       <td>xgyd2m7cz1tz@dsschool.co.kr</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaT</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>NaN</td>
#       <td>2017-09-25T11:08:25</td>
#       <td> direct</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td> direct</td>
#       <td>2017-09-25T11:08:33</td>
#       <td>Windows</td>
#       <td>Chrome</td>
#       <td>Seoul</td>
#       <td>KR</td>
#       <td>JENBBLWHSHUABKXPQBCOQJFNMRZAUAKECJEKVIUHQRWHET...</td>
#       <td>gc3riqbpec5a</td>
#       <td>JENBBLWHSHUABKXPQBCOQJFNMRZAUAKECJEKVIUHQRWHET...</td>
#       <td>None</td>
#       <td>ww4rloe4l6to@dsschool.co.kr</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaT</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>NaN</td>
#       <td>2017-11-27T16:59:25</td>
#       <td>dsschool.pagedemo.co</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>http://dsschool.pagedemo.co/</td>
#       <td>2017-11-27T16:59:36</td>
#       <td>iOS</td>
#       <td>Facebook Mobile</td>
#       <td>Seoul</td>
#       <td>KR</td>
#       <td>DGJIUGOFHLKOAFHAABHBGGRWGXJRWGYUAQXGLFNIWAXJVG...</td>
#       <td>h47v07u6u5zm</td>
#       <td>DGJIUGOFHLKOAFHAABHBGGRWGXJRWGYUAQXGLFNIWAXJVG...</td>
#       <td>None</td>
#       <td>i97zkjstv1mz@dsschool.co.kr</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaT</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>NaN</td>
#       <td>2017-11-30T15:44:16</td>
#       <td> direct</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td> direct</td>
#       <td>2017-11-30T15:44:27</td>
#       <td>Windows</td>
#       <td>Internet Explorer</td>
#       <td>Suwon-si</td>
#       <td>KR</td>
#       <td>AOPLSNBPLOMLIMRAFVFZDBGSKZYKATBOTFRQVECUAKWEPT...</td>
#       <td>v6ln67rwsqo4</td>
#       <td>AOPLSNBPLOMLIMRAFVFZDBGSKZYKATBOTFRQVECUAKWEPT...</td>
#       <td>86dpwpocr5gi</td>
#       <td>w2gcxxhaam4s@dsschool.co.kr</td>
#       <td>이초현</td>
#       <td>g8zyxqrdgcgf@dsschool.co.kr</td>
#       <td>01088615300</td>
#       <td>2017-12-17 09:26:56</td>
#       <td>중급반 4기</td>
#       <td>594,000</td>
#       <td>카드결제</td>
#       <td>결제 완료</td>
#       <td>NaN</td>
#       <td>4기</td>
#       <td>중급반</td>
#       <td>True</td>
#       <td>2017.0</td>
#       <td>12.0</td>
#       <td>17.0</td>
#       <td>9.0</td>
#       <td>26.0</td>
#       <td>56.0</td>
#       <td>Sunday</td>
#       <td>594000.0</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>NaN</td>
#       <td>2018-01-01T16:03:02</td>
#       <td> direct</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td> direct</td>
#       <td>2018-01-01T16:03:09</td>
#       <td>Windows</td>
#       <td>Chrome</td>
#       <td>Seoul</td>
#       <td>KR</td>
#       <td>MKYQTIHFMYVVIYKHXYLVMNDVMBNLLMHULEPWWVYTVMLLLS...</td>
#       <td>mbwhfxfmmowu</td>
#       <td>MKYQTIHFMYVVIYKHXYLVMNDVMBNLLMHULEPWWVYTVMLLLS...</td>
#       <td>None</td>
#       <td>rnippqcfcr09@dsschool.co.kr</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaT</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#   </tbody>
# </table>

# + colab={} colab_type="code" id="TG56xv2TFxWd"
mix = pd.read_csv('mixpanel_people_profiles_revised.csv')
# -

mix_tmp = pd.merge(mix, users, left_on = 'distinct_id', right_on ='mixpanel_id', how='inner')
mix_fin = pd.merge(mix_tmp, payments, on = 'payment_id', how = 'left')
mix_fin.head(3)

# + [markdown] colab_type="text" id="a_S6PNSlFxWk"
# **14. 위에서 정리한 믹스패널 데이터를 바탕으로 캠페인별 유입 id의 수에 비해 결제 비율이 가장 높은 광고 캠페인을 찾아주세요.**

# + [markdown] colab_type="text" id="SyGoThPbFxWm"
# 직접 접속한 고객들도 있고, 개인정보 보호 브라우저 등을 사용하는 고객들로 인해 항상 유입 경로를 추적하는게 가능하지는 않습니다.
#
# `utm_campaign [first touch]`의 경우 해당 고객이 '처음'으로 유입된 캠페인이 무엇인지에 대한 정보입니다. 해당 컬럼이 비어있지 않은 데이터만 남기고, 피벗 테이블을 이용해 `utm_campaign [first touch]`별 실제 결제 비율을 구해주세요. 결과는 다음과 같이 나오게 됩니다.

# + [markdown] colab_type="text" id="WY-WNllNFxWn"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>상태(bool)</th>
#     </tr>
#     <tr>
#       <th>utm_campaign [first touch]</th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>dsschoolintro</th>
#       <td>0.333333</td>
#     </tr>
#     <tr>
#       <th>dripinsta7</th>
#       <td>0.066667</td>
#     </tr>
#     <tr>
#       <th>kang1</th>
#       <td>0.066667</td>
#     </tr>
#     <tr>
#       <th>5why2</th>
#       <td>0.055556</td>
#     </tr>
#     <tr>
#       <th>startup</th>
#       <td>0.054054</td>
#     </tr>
#     <tr>
#       <th>leveltest</th>
#       <td>0.041667</td>
#     </tr>
#     <tr>
#       <th>search2</th>
#       <td>0.040000</td>
#     </tr>
#     <tr>
#       <th>purchase_complete</th>
#       <td>0.035714</td>
#     </tr>
#     <tr>
#       <th>fbpage</th>
#       <td>0.030303</td>
#     </tr>
#     <tr>
#       <th>univmajor</th>
#       <td>0.028037</td>
#     </tr>
#   </tbody>
# </table>
# -

mix_fin_tmp = mix_fin[mix_fin['utm_campaign [first touch]'].notnull()]

# + colab={} colab_type="code" id="XaTKRpLjFxWo"
mix_fin_tmp['상태(bool)'] = mix_fin_tmp['상태(bool)'].replace(True, 1).replace(False,0).replace(np.NaN,0)
# -

mix_pivot1 = pd.pivot_table(mix_fin_tmp, index = 'utm_campaign [first touch]', values = '상태(bool)', aggfunc = 'mean')
mix_pivot1.sort_values(by='상태(bool)',ascending = False).head(10)

# + [markdown] colab_type="text" id="UOxMkekIFxWy"
# head와 tail을 보면 극단적으로 많거나 (33%) 0%인 것을 확인할 수 있습니다. 이는 적은 예산을 쓴 캠페인은 해당 캠페인으로 부터 유입된 고객 자체가 적기 때문에 결과가 극단적으로 나오는 것입니다.
#
# 따라서, 유입 고객의 수가 20명 이상인 캠페인에 대해서만 위의 분석을 진행하기로 합니다. campaign으로부터 유입된 고객이 20명 이상인 캠페인만을 이용해 위의 피벗 테이블을 다시 만들어주세요. 결과는 다음과 같이 나오게 됩니다.
#

# + [markdown] colab_type="text" id="amgKR6qiFxWz"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>상태(bool)</th>
#     </tr>
#     <tr>
#       <th>utm_campaign [first touch]</th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>dripinsta7</th>
#       <td>0.066667</td>
#     </tr>
#     <tr>
#       <th>startup</th>
#       <td>0.054054</td>
#     </tr>
#     <tr>
#       <th>leveltest</th>
#       <td>0.041667</td>
#     </tr>
#     <tr>
#       <th>search2</th>
#       <td>0.040000</td>
#     </tr>
#     <tr>
#       <th>purchase_complete</th>
#       <td>0.035714</td>
#     </tr>
#     <tr>
#       <th>fbpage</th>
#       <td>0.030303</td>
#     </tr>
#     <tr>
#       <th>univmajor</th>
#       <td>0.028037</td>
#     </tr>
#     <tr>
#       <th>sungwon</th>
#       <td>0.026316</td>
#     </tr>
#     <tr>
#       <th>Clab</th>
#       <td>0.024390</td>
#     </tr>
#     <tr>
#       <th>deeplearningtraffic</th>
#       <td>0.022152</td>
#     </tr>
#   </tbody>
# </table>
# -

mix_pivot1.loc[mix_fin_tmp['utm_campaign [first touch]'].value_counts()>20].sort_values(by='상태(bool)',ascending = False).head(10)

# + [markdown] colab_type="text" id="Yy8crgaIFxW6"
# 상위권의 캠페인들은 유입된 고객대비 결제율이 다른 캠페인에 비해 상당히 높은 것을 파악할 수 있습니다. 결제가 마케팅의 최종 목표이기 때문에, 마케팅팀에 해당 캠페인의 리스트를 전달해주어 해당 캠페인의 컨텐츠 내용을 분석한 뒤 가설을 세워 더 효율이 좋은 캠페인을 만들 수 있습니다.

# + [markdown] colab_type="text" id="4RKPsxnMFxXA"
# ---

# + [markdown] colab_type="text" id="tejZYIfGFxXB"
# **15. 결제 데이터를 바탕으로 두 개 이상의 강의를 수강한 고객들을 찾아주세요.**
#
# DS School 강의에 만족도가 높은 고객분들은 여러개의 강의를 수강하고 가십니다. 이런 분들은 향후 오픈되는 강의도 수강하실 확률이 높기 때문에 VIP로 선정하여 DS School의 소식을 가장 최우선으로 전하고자 합니다. payments 테이블을 이용하여 이러한 고객분들을 찾아내어 구매 강좌수를 포함하여 데이터프레임으로 만들어주세요. 고객의 id는 이메일을 사용하시면 됩니다.
#
# 결과는 다음과 같이 나오게 됩니다.

# + [markdown] colab_type="text" id="xy8PRfF_FxXK"
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>구매 강좌수</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>1n04ko1pgq3r@dsschool.co.kr</th>
#       <td>4</td>
#     </tr>
#     <tr>
#       <th>w9df010ys6yd@dsschool.co.kr</th>
#       <td>3</td>
#     </tr>
#     <tr>
#       <th>18vwfdfclejc@dsschool.co.kr</th>
#       <td>3</td>
#     </tr>
#     <tr>
#       <th>yn4wl5lgz37f@dsschool.co.kr</th>
#       <td>3</td>
#     </tr>
#     <tr>
#       <th>zq1ccpk8bjj3@dsschool.co.kr</th>
#       <td>3</td>
#     </tr>
#   </tbody>
# </table>
# -

pivot_fin = pd.pivot_table(payments[payments['상태(bool)']==True], index = '이메일', values = 'payment_id', aggfunc = 'count').sort_values(by='payment_id', ascending = False).head(5)
pivot_fin.columns = ['구매 강좌수']
pivot_fin.head()

# + [markdown] colab_type="text" id="Sdho0faeFxXp"
# ## 제출
#
# 과제를 다 끝내셨으면 http://bit.ly/ds-assignment 에서 안내에 따라 과제를 제출하여 주세요! 과제를 제출해주시면 솔루션과 검토 결과를 드립니다. 오프라인 수업의 경우 과제를 제출하지 않으시더라도 솔루션은 다음 수업 시간에 제공해드립니다.
#
# 수업이나 과제 관련 질문, 수료증 문의 등은 담당 튜터(조교)에게 문의 주세요. 영수증 발급 등의 문의는 support@dsschool.co.kr 로 메일 주시면 담당자분이 응대해주실 겁니다. 기타 궁금한 사항은 슬랙으로 문의 주세요!

# + colab={} colab_type="code" id="Ou_cek6UFxXs"

