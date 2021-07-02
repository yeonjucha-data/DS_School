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

# ## 클래스101 데이터 분석 팀에 오신 것을 환영합니다!
#
# (이 쥬피터 노트북은 다음의 링크 <b><big>http://bit.ly/dsa-0102</big></b> 데이터는 <b><big>https://bit.ly/dsa-01-class101</big></b> 에서 다운받을 수 있습니다.)
#
# <img src="https://drive.google.com/uc?export=download&id=1cUemVaa-CideqXyJIds4hsB9iqFqaysY" width="640px"/>
#
# <center><small><a href="https://class101.net/" target="_blank">클래스101</a> 홈페이지</small></center>
#
# 안녕하세요! [클래스101](https://class101.net/) 데이터 분석팀에 오신 것을 환영합니다. [클래스101](https://class101.net/)은 온라인으로 취미를 배울 수 있는 온라인 클래스 플랫폼이며, 2019년을 기점으로 빠르게 성장하고 있습니다.
#
# 오늘 이 쥬피터 노트북을 받은 수강생분들께서는 하루동안 [클래스101](https://class101.net/)의 일일 데이터 분석가로 활동하게 될 것입니다. [클래스101](https://class101.net/)의 2019년 5월 데이터부터 2020년 4월 데이터까지 총 1년간의 데이터를 바탕으로, 운영팀과 마케팅 팀을 포함한 클래스101의 데이터 분석팀이 데이터를 빠르게 다루고 분석할 수 있도록 데이터를 정리하는, 일명 데이터 클리닝(Data Cleaning) 업무를 하는 것이 오늘의 역할입니다.
#
# 하기에 제시한 15개의 데이터 분석 요청을 프로그래밍 언어 파이썬([Python](https://www.python.org/))과 파이썬의 데이터 분석 패키지 판다스([Pandas](https://pandas.pydata.org/))를 활용하여 풀어주세요.
#
# 숙련된 데이터분석가의 경우 하기의 요청을 늦어도 2시간 내에는 해결할 수 있습니다. 즉, **2시간 안에 모든 문제를 풀 수 있다면 합격입니다.**
#
# 문제를 풀 때 다른 자료를 참고하거나, 구글에 검색하는 것 모두 허용합니다. (문제 중에는 구글에 검색하지 않으면 풀 수 없는 문제도 준비해놓았습니다) 관련 자료는 [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)를 강력 추천합니다. 또한 이전 수업에서 학습한 내용을 참고하는 것도 적극 추천합니다.

# ### 사전 준비

# 파이썬의 데이터 분석 패키지 판다스(Pandas)를 읽어옵니다.
# 이를 pd라는 축약어로 사용합니다.
import pandas as pd

# ### 데이터 로딩하기

# 먼저 데이터를 로딩해오겠습니다. 데이터를 읽어올때는 [판다스(Pandas)](https://pandas.pydata.org/)의 [read_csv](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) 라는 기능을 사용합니다.
#
# 여기서 파일의 경로를 지정하는 방법에 주의하셔야 합니다. read_csv를 실행할 때 (**FileNotFoundError**)라는 이름의 에러가 난다면 경로가 제대로 지정이 되지 않은 것입니다. 만일 파일의 경로를 지정하는 법이 생각나지 않는다면 [다음의 링크](http://88240.tistory.com/122)를 통해 경로를 지정하는 법을 복습해주세요.

# **사용자(```users```) 데이터에 접근하기**
#
# 가장 먼저 읽어올 데이터는 사용자(```users.csv```) 데이터입니다. 이 데이터는 [클래스101](https://class101.net/)에 가입한 사용자(```users```)의 모든 정보를 담고 있으며, 이 데이터를 중심으로 매출과 누적 수강생 등 여러 핵심적인 분석을 하게 될 것입니다.

# +
# 판다스(pandas)의 read_csv를 활용하여 클래스101의 사용자(users) 데이터를 저장한 users.csv 를 읽어옵니다.
# 여기서 id 컬럼을 이 데이터의 인덱스(index)로 지정합니다.
# 이 데이터를 users라는 이름의 변수에 할당합니다.
users = pd.read_csv("data/users.csv", index_col = "id")

# users 변수에 할당된 데이터의 행렬 사이즈를 출력합니다.
# 출력은 (row, column) 으로 표시됩니다.
print(users.shape)

# head()로 users 데이터의 상위 5개를 띄웁니다.
users.head()
# -

# 사용자(```users```) 데이터의 각 컬럼에 대한 설명은 다음과 같습니다.
#
#   * ```id``` - 사용자(```users```)의 아이디. 이 컬럼을 인덱스(index)로 활용할 예정입니다.
#   * ```email``` - 사용자(```users```)의 이메일 정보입니다. 이메일을 기입하지 않을 가능성이 있으며, 이 경우에는 ```None```이라는 값이 들어갑니다. 개인정보 보호를 위해 가명화(Pseudonymisation) 처리하였습니다.
#   * ```phone``` - 사용자(```users```)의 전화번호입니다. 마찬가지로 전화번호를 기입하지 않을 가능성이 있으며, 이 경우에는 ```None```이라는 값이 들어갑니다.  개인정보 보호를 위해 가명화(Pseudonymisation) 처리하였습니다.
#   * ```name``` - 사용자(```users```)의 이름입니다. 마찬가지로 개인정보 보호를 위해 가명화(Pseudonymisation) 처리되어 있습니다.
#   * ```created_at``` - 사용자(```users```) 데이터를 생성(create)한 날짜입니다.
#   * ```updated_at``` - 사용자(```users```) 데이터를 수정(update)한 날짜입니다.
#   * ```deleted_at``` - 사용자(```users```) 데이터를 삭제(delete)한 날짜입니다.
#   * ```registration_date``` - 사용자(```users```) 회원가입을 한 날짜 정보가 담겨 있습니다. ```created_at``` 컬럼에서 연-월-일만 가져온 데이터입니다.

# **클래스(```klasses```) 데이터에 접근하기**
#
# 그 다음에 접근하고 싶은 데이터는 클래스(```klasses.csv```) 데이터입니다. 이 데이터는 [클래스101](https://class101.net/)에서 진행하고 있는 모든 수업 정보(ex: 이름, 카테고리 등)를 담고 있습니다. 이 데이터와 이후에 나올 클래스 수강권(```klass_tickets```) 데이터를 활용하면 수강생의 클래스 수강 여부를 파악할 수 있습니다.

# +
# 판다스(pandas)의 read_csv를 활용하여 클래스101의 클래스(klasses) 데이터를 저장한 klasses.csv 를 읽어옵니다.
# 여기서 id 컬럼을 이 데이터의 인덱스(index)로 지정합니다.
# 이 데이터를 klasses라는 이름의 변수에 할당합니다.
klasses = pd.read_csv("data/klasses.csv", index_col = "id")

# klasses 변수에 할당된 데이터의 행렬 사이즈를 출력합니다.
# 출력은 (row, column) 으로 표시됩니다.
print(klasses.shape)

# head()로 klasses 데이터의 상위 5개를 띄웁니다.
klasses.head()
# -

# 클래스(```klasses```) 데이터의 각 컬럼에 대한 설명은 다음과 같습니다.
#
#   * ```id``` - 클래스(```klasses```)의 아이디. 이 컬럼을 인덱스(index)로 활용할 예정입니다.
#   * ```category_id``` - 카테고리(```categories```)의 아이디. 이 컬럼을 활용하여 카테고리(```categories```) 데이터와 연결할 수 있습니다.
#   * ```is_deleted``` - 해당 클래스(```klasses```)가 삭제되었으면 1이, 삭제되지 않았으면 0이 기록되어있습니다.
#   * ```created_at``` - 클래스(```klasses```) 데이터를 생성(create)한 날짜입니다.
#   * ```updated_at``` - 클래스(```klasses```) 데이터를 수정(update)한 날짜입니다.
#   * ```deleted_at``` - 클래스(```klasses```) 데이터를 삭제(delete)한 날짜입니다.

# **클래스 수강권(```klass_tickets```) 데이터 접근하기**
#
# 클래스(```klasses```) 데이터를 성공적으로 가져왔다면, 이번에는 클래스 수강권(```klass_tickets.csv```) 데이터에 접근해보겠습니다. 이 데이터는 사용자가 클래스를 수강한 정보를 담고 있으며, 이 데이터에 있는 상세 정보를 활용하는 것은 물론, ```user_id```와 ```klass_id```와 같은 외래키(Foreign Key)를 활용해 사용자(```users```) 데이터와 클래스(```klasss```) 데이터에 접근할 수 있습니다.

# +
# 판다스(pandas)의 read_csv를 활용하여 클래스101의 클래스 수강권(klass_tickets) 데이터를 저장한 klass_tickets.csv 를 읽어옵니다.
# 여기서 id 컬럼을 이 데이터의 인덱스(index)로 지정합니다.
# 이 데이터를 klass_tickets라는 이름의 변수에 할당합니다.
klass_tickets = pd.read_csv("data/klass_tickets.csv", index_col = "id")

# klass_tickets 변수에 할당된 데이터의 행렬 사이즈를 출력합니다.
# 출력은 (row, column) 으로 표시됩니다.
print(klass_tickets.shape)

# head()로 klass_tickets 데이터의 상위 5개를 띄웁니다.
klass_tickets.head()
# -

# 클래스 수강권(```klass_tickets```) 데이터의 각 컬럼에 대한 설명은 다음과 같습니다.
#
#   * ```id``` - 클래스 수강권(```klass_tickets```)의 아이디. 이 컬럼을 인덱스(index)로 활용할 예정입니다.
#   * ```user_id``` - 사용자(```useres```)의 아이디입니다. 이 컬럼을 활용하여 사용자(```useres```) 데이터와 연결할 수 있습니다.
#   * ```klass_id``` - 클래스(```klasses```)의 아이디입니다. 이 컬럼을 활용하여 클래스(```klasses```) 데이터와 연결할 수 있습니다.
#   * ```available_days``` - 해당 수강권(```klass_ticketes```)의 유효기간입니다. 일(day)로 기록되어 있습니다. (즉, 300일은 수강권이 개시된 날짜로부터 300일 동안 유효한 수강권이라는 의미)
#   * ```is_paid``` - 수강권(```klass_ticketes```)의 구매 여부입니다. 구매하였으면 1이, 구매하지 않았으면 0이 기록되어 있습니다.
#   * ```created_at``` - 수강권(```klass_ticketes```) 데이터를 생성(create)한 날짜입니다.
#   * ```updated_at``` - 수강권(```klass_ticketes```) 데이터를 수정(update)한 날짜입니다.
#   * ```finished``` - 수강권(```klass_ticketes```)이 만료되는 날짜입니다.
#   * ```deleted_at``` - 수강권(```klass_ticketes```) 데이터를 삭제(delete)한 날짜입니다.

# **카테고리(```categories```) 데이터에 접근하기**
#
# 마지막으로 접근하고 싶은 데이터는 카테고리(```categories```) 데이터입니다. 이 데이터는 [클래스101](https://class101.net/)에서 진행하고 있는 모든 수업의 카테고리(ex: 요리, 운동, 디자인, 커리어 등)에 대한 정보를 담고 있습니다. 이 데이터와 앞서 언급한 클래스(```klasses```) 데이터를 연결하면 수업 카테고리마다의 세부 통계치(ex: 신규 수강생, 누적 수강생 등)를 파악할 수 있습니다.

# +
# 판다스(pandas)의 read_csv를 활용하여 클래스101의 카테고리(categories) 데이터를 저장한 categories.csv 를 읽어옵니다.
# 여기서 id 컬럼을 이 데이터 의 인덱스(index)로 지정합니다.
# 이 데이터를 categories라는 이름의 변수에 할당합니다.
categories = pd.read_csv("data/categories.csv", index_col = "id")

# categories 변수에 할당된 데이터의 행렬 사이즈를 출력합니다.
# 출력은 (row, column) 으로 표시됩니다.
print(categories.shape)

# head()로 categories 데이터의 상위 5개를 띄웁니다.
categories.head()
# -

# 카테고리(```categories```) 데이터의 각 컬럼에 대한 설명은 다음과 같습니다.
#
#   * ```id``` - 카테고리(```categories```)의 아이디. 이 컬럼을 인덱스(index)로 활용할 예정입니다.
#   * ```title``` - 카테고리(```categories```)의 제목입니다. ```요리```, ```운동```, ```디자인```, ```커리어``` 등 총 41개의 카테고리가 존재합니다.

# ### 데이터 정리
#
# 가장 먼저 데이터를 정리하는(Data Cleaning) 업무부터 시작하겠습니다. 데이터를 분석하기 전, 사전에 데이터를 깔끔하게 정리하는 과정을 거쳐야 데이터를 수월하게 분석할 수 있습니다. (실제 현업에서 활동하는 데이터 분석가(Data Analyst)는 전체 업무 시간의 50% ~ 70%를 데이터를 정리하는데 사용합니다)
#
# 만일 파이썬과 판다스를 능숙하게 사용할 수 있다면 남들보다 빠르게 데이터를 정리하고 분석할 수 있습니다. 반면 파이썬과 판다스를 능숙하게 사용할 수 없다면, 남들보다 데이터를 정리하는데 시간이 오래 걸리게 되고 이는 곧 생산성의 차이로 이어집니다. 그러므로 빠른 시간 안에 효율적으로 데이터를 정리하는 스킬은 무엇보다도 중요합니다.
#
# 먼저 클래스101의 데이터에서 정리가 필요한 몇몇 부분을 다뤄보겠습니다.

# **1. 사용자(```users```) 데이터의 날짜 정보를 ```datetime``` 형태로 변환해주세요.**
#
# 사용자 데이터에는 날짜와 시간(```datetime```) 정보를 저장한 총 네 개의 컬럼이 있습니다.
#
#   * ```created_at``` - 사용자(```users```) 데이터를 생성(create)한 날짜입니다.
#   * ```updated_at``` - 사용자(```users```) 데이터를 수정(update)한 날짜입니다.
#   * ```deleted_at``` - 사용자(```users```) 데이터를 삭제(delete)한 날짜입니다.
#   * ```registration_date``` - 사용자(```users```) 회원가입을 한 날짜 정보가 담겨 있습니다. ```created_at``` 컬럼에서 연-월-일만 가져온 데이터입니다.
#
# 이 컬럼은 날짜(또는 날짜와 시간) 데이터를 저장하고 있는데, 이 컬럼을 활용하여 1) 월별 신규 사용자 또는 2) 시간당 신규 사용자 등의 패턴을 분석할 수 있습니다.
#
# 문제는, 판다스에서 처음 이 컬럼을 읽어왔을 때는 날짜와 시간(```datetime```) 형태로 저장되어 있는 것이 아닌, 문자열(```string```, ```str```) 형태로 저장이 되어있습니다. 그러므로 이 컬럼의 형태를 날짜와 시간(```datetime```)으로 변경해줘야, 이후 이 컬럼을 데이터를 분석할 때 용이하게 사용할 수 있습니다.
#
# 그런 의미에서 ```created_at```, ```updated_at```, ```deleted_at```, ```registration_date``` 이렇게 네 개의 컬럼의 타임을 ```datetime```으로 변경해주세요. 변경 후 판다스(Pandas)의 [dtypes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html) 기능을 실행하면 다음과 같은 결과가 나와야 합니다. (ex: ```users.dtypes```)

# <pre>
# email                        object
# phone                        object
# name                         object
# created_at           datetime64[ns]
# updated_at           datetime64[ns]
# deleted_at           datetime64[ns]
# registration_date    datetime64[ns]
# dtype: object
# </pre>

# PS) 판다스(Pandas)의 [to_datetime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) 기능을 사용하면 손쉽게 컬럼의 형태를 ```datetime```으로 변경해줄 수 있습니다.

users['created_at'] = pd.to_datetime(users['created_at'])
users['updated_at'] = pd.to_datetime(users['updated_at'])
users['deleted_at'] = pd.to_datetime(users['deleted_at'])
users['registration_date'] = pd.to_datetime(users['registration_date'])
users.dtypes

# **2. 클래스(```klasses```) 데이터의 ```is_deleted``` 컬럼 값을 ```0```, ```1```에서 ```True```, ```False```로 바꿔주세요.**
#
# 이번에는 클래스(```klasses```) 데이터의 ```is_deleted``` 컬럼을 정리해보겠습니다. 이 컬럼은 해당 클래스(```klasses```)가 삭제되었는지 여부를 나타내는 컬럼인데, 클래스가 삭제되었으면 ```1```이, 삭제되지 않았으면 ```0```이라는 값을 기록합니다.
#
# 이 컬럼을 그대로 사용하는 것도 가능하지만, 직관적이고 가독성을 높이기 위해서, 값을 ```1```, ```0```이 아닌 ```True```, ```False```로 변경하고 싶습니다. 최종적으로 다음의 결과가 나와야 합니다.

# <table border="1" class="dataframe" style="float: left;">
# 	<thead>
# 		<tr style="text-align: right;">
# 			<th></th>
# 			<th>is_deleted</th>
# 			<th>is_deleted(bool)</th>
# 		</tr>
# 		<tr>
# 			<th>id</th>
# 			<th></th>
# 			<th></th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<th>5qyiobiuqwm5of3wjn7b8u3o</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 		<tr>
# 			<th>sg0xpv8oz6vtqv75j0uk3mzq</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 		<tr>
# 			<th>0w78clopemxncz6h0aqmnhf3</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 		<tr>
# 			<th>pv274nmwxb77k79zdddicl88</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 		<tr>
# 			<th>p3b9n3g8z2vo5ch9u2jkfj38</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 	</tbody>
# </table>

# PS) 판다스(Pandas)의 [replace](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html) 기능을 사용하면 손쉽게 데이터를 ```1```, ```0```에서 ```True```, ```False```로 변경할 수 있습니다.

klasses['is_deleted(bool)'] = klasses['is_deleted'].replace(0, False).replace(1,True)
klasses[['is_deleted','is_deleted(bool)']].head()

# **3. 클래스 수강권(```klass_tickets```) 데이터의 ```is_paid``` 컬럼 값을 ```0```, ```1```에서 ```True```, ```False```로 바꿔주세요.**
#
# 이번에는 위와 유사하게, 클래스 수강권(```klass_tickets```) 데이터의 ```is_paid``` 컬럼을 정리해보겠습니다. 이 컬럼은 해당 클래스 수강권(```klass_tickets```)이 실제 구매한 것인지 아닌지 여부를 나타내는 컬럼인데, 수강권을 구매했다면 ```1```이, 구매하지 않았으면 ```0```이라는 값을 기록합니다. 마찬가지로 직관적이고 가독성을 높이기 위해서, 값을 ```1```, ```0```이 아닌 ```True```, ```False```로 변경하고 싶습니다. 최종적으로 다음의 결과가 나와야 합니다.

# <table border="1" class="dataframe" style="float: left;">
# 	<thead>
# 		<tr style="text-align: right;">
# 			<th></th>
# 			<th>is_paid</th>
# 			<th>is_paid(bool)</th>
# 		</tr>
# 		<tr>
# 			<th>id</th>
# 			<th></th>
# 			<th></th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<th>8u4iqyurthy66f1lxzvg2mmo</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 		<tr>
# 			<th>hywaasrsu2uipjh7hox8btzk</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 		<tr>
# 			<th>a7a0kmzuiu8lncc5xcdomkd2</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 		<tr>
# 			<th>5ddaf8rkhfff4910pwk56vcn</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 		<tr>
# 			<th>kri4yddw8xweaqy1ka9ul7uk</th>
# 			<td>0</td>
# 			<td>False</td>
# 		</tr>
# 	</tbody>
# </table>

klass_tickets['is_paid(bool)'] = klass_tickets['is_paid'].replace(0, False).replace(1,True)
klass_tickets[['is_paid','is_paid(bool)']].head()

# **4. 클래스(```klasses```) 데이터와 클래스 수강권(```klasses_tickets```) 데이터의 날짜 정보를 datetime 형태로 변환해주세요.**
#
# 사용자(```users```) 데이터와 유사하게, 클래스(```klasses```) 데이터와 클래스 수강권(```klasses_tickets```) 데이터에도 날짜와 시간(```datetime```) 정보를 저장한 컬럼들이 있습니다.
#
# **클래스(```klasses```) 데이터**
#   * ```created_at``` - 클래스(```klasses```) 데이터를 생성(create)한 날짜입니다.
#   * ```updated_at``` - 클래스(```klasses```) 데이터를 수정(update)한 날짜입니다.
#   * ```deleted_at``` - 클래스(```klasses```) 데이터를 삭제(delete)한 날짜입니다.
#   
# **클래스 수강권(```klasses_tickets```) 데이터**
#   * ```created_at``` - 수강권(```klass_ticketes```) 데이터를 생성(create)한 날짜입니다.
#   * ```updated_at``` - 수강권(```klass_ticketes```) 데이터를 수정(update)한 날짜입니다.
#   * ```finished``` - 수강권(```klass_ticketes```)이 만료되는 날짜입니다.
#   * ```deleted_at``` - 수강권(```klass_ticketes```) 데이터를 삭제(delete)한 날짜입니다.
#   
# 1번 문제와 유사하게, 이 컬럼들의 형태를 ```datetime```으로 변경해주세요. 변경 후 판다스(Pandas)의 [dtypes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html) 기능을 실행하면 다음과 같은 결과가 나와야 합니다.

# **클래스(```klasses```) 데이터의 데이터 타입(```dtypes```)**
# <pre>
# category_id                 object
# is_deleted                   int64
# created_at          datetime64[ns]
# updated_at          datetime64[ns]
# deleted_at          datetime64[ns]
# is_deleted(bool)              bool
# dtype: object
# </pre>

# **클래스 수강권(```klasses_tickets```) 데이터의 데이터 타입(```dtypes```)**
# <pre>
# user_id                   object
# klass_id                  object
# available_days           float64
# is_paid                    int64
# created_at        datetime64[ns]
# updated_at        datetime64[ns]
# finished_at       datetime64[ns]
# deleted_at        datetime64[ns]
# dtype: object
# </pre>

klasses['created_at'] = pd.to_datetime(klasses['created_at'])
klasses['updated_at'] = pd.to_datetime(klasses['updated_at'])
klasses['deleted_at'] = pd.to_datetime(klasses['deleted_at'])
klasses.dtypes

klass_tickets['created_at'] = pd.to_datetime(klass_tickets['created_at'])
klass_tickets['updated_at'] = pd.to_datetime(klass_tickets['updated_at'])
klass_tickets['finished_at'] = pd.to_datetime(klass_tickets['finished_at'])
klass_tickets['deleted_at'] = pd.to_datetime(klass_tickets['deleted_at'])
klass_tickets.dtypes

# **5. 수강권(```klass_tickets```) 데이터의 유효기간(```available_days```) 컬럼 값을 정수형(```int```)로 변경해주세요.**
#
# 이번에는 수강권(```klass_tickets```) 데이터의 유효기간(```available_days```) 컬럼을 정리해보겠습니다. 유효기간(```available_days```)은 수강신청 후 해당 수업(클래스)를 들을 수 있는 기간을 숫자로 나타낸 컬럼입니다. 가령 10이라는 값이 들어가 있다면 수강 신청 후 최대 열흘까지 수업을 들을 수 있다는 의미이며, 100이라는 값이 들어가 있다면 수강 신청 후 최대 100일까지 수업을 들을 수 있다는 의미입니다.
#
# 현재 이 컬럼은 소수점을 포함할 수 있는 실수형(```float```)으로 되어있지만, 날짜에는 소수점이 들어가지 않기 때문에 소수점을 포함하지 않는 정수형(```int```)으로 변환해주면 차후 이 컬럼을 다루는데 더 용이할 것 같습니다. 그러므로 유효기간(```available_days```) 컬럼의 데이터 형태(Data Type)을 정수형(```int```)으로 바꿔주세요. 최종적으로 다음의 결과가 나와야 합니다.

# <table border="1" class="dataframe" style="float: left;">
# 	<thead>
# 		<tr style="text-align: right;">
# 			<th></th>
# 			<th>available_days</th>
# 			<th>available_days(int)</th>
# 		</tr>
# 		<tr>
# 			<th>id</th>
# 			<th></th>
# 			<th></th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<th>8u4iqyurthy66f1lxzvg2mmo</th>
# 			<td>393.0</td>
# 			<td>393</td>
# 		</tr>
# 		<tr>
# 			<th>hywaasrsu2uipjh7hox8btzk</th>
# 			<td>900.0</td>
# 			<td>900</td>
# 		</tr>
# 		<tr>
# 			<th>a7a0kmzuiu8lncc5xcdomkd2</th>
# 			<td>112.0</td>
# 			<td>112</td>
# 		</tr>
# 		<tr>
# 			<th>5ddaf8rkhfff4910pwk56vcn</th>
# 			<td>112.0</td>
# 			<td>112</td>
# 		</tr>
# 		<tr>
# 			<th>kri4yddw8xweaqy1ka9ul7uk</th>
# 			<td>112.0</td>
# 			<td>112</td>
# 		</tr>
# 	</tbody>
# </table>

# PS) 판다스(Pandas)의 [astype](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.astype.html) 기능을 사용하면 손쉽게 데이터의 형태(Data Type)을 변경할 수 있습니다.

klass_tickets['available_days(int)'] = klass_tickets['available_days'].astype(int)
klass_tickets.head()

# ### 분석 리포트 생성

# 데이터를 다 정리했으면, 이제 본격적으로 데이터 분석(Data Analysis)을 해보겠습니다.
#
# 이번 과제의 사실상의 메인 주제는 분석 리포트 생성입니다. 분석 리포트는 데이터 분석가가 하는 가장 일반적인 업무 중 하나인데, 회사의 데이터를 가져와 월별 주요 지표(매출, 신규 가입자 수, 특정 카테고리별 판매량 등)를 정리하는 업무라고 생각하시면 됩니다.
#
# 만일 데이터 분석가가 분석 리포트를 정확하고 빠르게 만들어줄 수 있다면, 회사의 다른 이해관계자들이 데이터를 근거삼아 올바른 의사결정을 할 수 있을 것입니다. 반면 데이터 분석가가 분석 리포트를 만들 때 세부 지표를 잘못 계산해주거나, 분석 리포트를 만드는 시간이 오래 걸린다면 회사의 주요 이해관계자들이 근거 기반의 의사결정을 하는데 어려움을 겪을 것입니다.
#
# 그런 의미에서, 이번에는 클래스101의 2020년 4월 기준 주요 지표를 추출해서 의사결정을 내려보겠습니다.
#

# **6. 2020년 4월 기준 전체 가입자와 신규 가입자를 구해주세요.**
#
# 먼저 가장 기본적인 지표부터 살펴보겠습니다. 이번에 계산할 지표는 ```전체 가입자```와 ```신규 가입자```입니다. ```전체 가입자```와 ```신규 가입자```는 회사의 성장 여부를 확인할 수 있는 중요한 지표중에 하나입니다. 서비스에 ```전체 가입자```와 ```신규 가입자```가 늘어나면 늘어날수록 회사는 더 성장하고 있다고 판단할 수 있으며, 반면 서비스의 ```전체 가입자```와 ```신규 가입자```가 늘어나지 않는다면 서비스의 성장세가 주춤해졌다고 판단할 수 있습니다.
#
# 그런 의미에서, 2020년 4월 기준 클래스101의 ```전체 가입자```와 ```신규 가입자```의 총 인원수를 구해주세요. ```전체 가입자```는 **484,747 명**, ```신규 가입자```는 **49,464 명**이 나왔다면 정상적으로 계산했다고 판단할 수 있습니다.

total_2004 = users.index[users['registration_date'] < '2020-05-01']
len(total_2004)

new_2004 = users.index[(users['registration_date'] >='2020-04-01') & (users['registration_date'] < '2020-05-01')]
len(new_2004)

# **7.2020년 4월 기준 ```전체 수강생```. 즉, 수강권을 구매한 구매자를 찾아주세요.**
#
# 이번에는 비슷하지만 다른 지표를 계산하겠습니다. 바로 ```수강생```입니다.
#
# 사용자가 서비스에 가입했다고 하더라도, 아직 수강 신청을 하지 않았다면 회사의 매출에 기여하지 않았다고도 판단할 수 있습니다. 그런 의미에서, 사용자보다는 ```수강생```(=수강 신청을 한 사람, 내지는 상품을 구매한 사람)을 계산하는 것이 더 정확할 수 있습니다.
#
# 그런 의미에서, 2020년 4월 1일부터 2020년 4월 30일 사이에 클래스101의 수업을 ```구매```한 ```전체 수강생```의 인원 수를 구해주세요. 계산 결과 총 **15,284 명**이 나왔다면 성공적으로 ```전체 수강생```을 구한 것입니다.
#
# PS) 한 명의 수강생이 여러 개의 수업을 수강 신청했다고 하더라도, 실제 수강 신청한 수강생은 1명이라는 것에 주의해주세요.

# +
klass_tickets['created_at_norm'] = klass_tickets['created_at'].dt.normalize() # 시간을 제외하고 년/월/일만 추출
#klass_tickets.query("'2020-04-01' <= created_at_norm < '2020-05-01'")
april = (klass_tickets['created_at_norm'] >= '2020-04-01') &  (klass_tickets['created_at_norm'] < '2020-05-01')
paid = klass_tickets['is_paid(bool)'] == True

len(klass_tickets.loc[april&paid,'user_id'].value_counts()) #unique한 값 개수 세기 (https://rfriend.tistory.com/267)
# -

# **8. 2020년 4월 30일 기준 유효 수강생. 즉 이미 수업을 듣고 있는 수강생을 구해주세요.**

# 이번에는 보다 더 자세한 지표를 계산해보겠습니다. 바로 ```유효 수강생```입니다.
#
# ```전체 수강생```과 ```유효 수강생```의 가장 큰 차이점은, "실제 이 서비스(클래스101)을 이용하는 것을 고려하고 있는가?"의 여부입니다. ```전체 수강생```은 수강 신청일(수업을 신청한 날짜)를 기준으로 계산하기 때문에 실제 수업을 듣고 있는 사용자는 반영되지 않을 가능성이 높습니다. 하지만 ```유효 수강생```은 실제 이 서비스를 이용하고 있는 수강생이 몇 명인지를 계산하기 때문에, 서비스의 실사용자가 몇 명인지를 파악할 수 있습니다.
#
# (참고로 교육업이 아닌 다른 서비스에서는, 이와 유사한 지표로 ```DAU(Daily Active Users)``` 또는 ```MAU(Maily Active Users)```를 계산하고 있습니다. ```유효 수강생```은 이와 유사한 개념이라고 보시면 됩니다)
#
# 그런 의미에서, 2020년 4월 30일 기준 ```유효 수강생```의 총 인원을 계산해주세요. 계산 결과 총 **71,996 명**이 나왔다면 성공적으로 ```유효 수강생```을 구한 것입니다.
#
# PS) 마찬가지로 한 명의 수강생이 여러 개의 수업을 수강 신청했다고 하더라도, 실제 수강 신청한 수강생은 1명이라는 것에 주의해주세요.

klass_ongoing = (klass_tickets['created_at'] <= '2020-05-01') & (klass_tickets['finished_at'] >= '2020-05-01')
len(klass_tickets.loc[klass_ongoing, 'user_id'].value_counts())

# **9. 2020년 4월 이후에 생긴 신규 클래스를 찾고, 이 신규 클래스를 수강 신청한 사용자의 총 인원수를 구해주세요.**

# 이번에는 수강생(```users```)가 아닌 클래스(```klasses```)에 관련된 지표를 계산해보겠습니다. 클래스101과 같은 교육업에서는 신규 컨텐츠(=클래스)를 지속적으로 생산해내는 것이 중요합니다. 그런 의미에서 2020년 4월 1일 이후 새롭게 런칭한 클래스(```klasses```)의 성과를 확인해보고 싶습니다.
#
# 2020년 4월 1일 이후에 런칭한 신규 클래스(```klasses```)의 총 수강생(```users```)을 구해주세요. 최종적으로 총 **244 명**이 나왔다면 성공적으로 지표를 구한 것입니다.

klass_and_ticket = pd.merge(klass_tickets,klasses,left_on = 'klass_id', right_on = 'id') #테이블 join (http://www.gisdeveloper.co.kr/?p=8255)
new = klass_and_ticket['created_at_y']>'2020-04-01'
len(klass_and_ticket[new])

# **10. 2020년 4월 이후에 생긴 신규 클래스 중, ```직무``` 카테고리 클래스를 수강 신청한 사용자의 총 인원수를 구해주세요.**

# 이번에는 위 문제를 응용해보겠습니다. 클래스101에는 ```커리어```, ```직무```, ```드로잉```, ```공예```, ```디자인``` 등등 다양한 카테고리의 수업이 있습니다. 이 수업 중 2020년 4월 기준 클래스101이 가장 집중하고 있는 카테고리는 바로 ```직무``` 카테고리입니다.
#
# 그런 의미에서, 2020년 4월 이후에 생긴 신규 클래스 중, ```직무``` 카테고리 클래스를 수강 신청한 사용자의 총 인원을 구해주세요. 계산 결과 총 **163 명**이 나왔다면 성공적으로 지표를 구한 것입니다.

plus_category = pd.merge(klass_and_ticket, categories, left_on = 'category_id', right_on = 'id')
career = plus_category['title'] == '직무'
len(plus_category[career & (plus_category['created_at_y']>'2020-04-01')])

# ### 심화 분석
#
# 위의 분석 리포트는 2020년 4월을 기준으로 생성하는 것입니다. 하지만 데이터 분석가가 실제 현업에서 데이터를 분석하게 되면, 단순히 특정 연월을 기준으로 분석하는 것이 아닌, 전체 연월 또는 전체 카테고리 등 훨씬 더 포괄적인 분야에 대한 분석을 해야합니다. 그런 의미에서, 이번에는 앞서 진행한 분석 리포트 생성보다 더 디테일한 분석을 진행해보도록 하겠습니다.

# **11. 월별 신규 가입 사용자(```users```) 수를 구해주세요.**
#
# 앞서 분석 리포트를 생성할 때는 2020년 4월만을 기준으로 신규 가입 사용자를 구했습니다. 하지만 실제 데이터를 분석할 때는 특정 연월 뿐만 아니라 전체 연월을 계산하여, 이를 통해 신규 가입 사용자가 늘어나고 있는지(=회사가 성장하고 있는지), 내지는 신규 가입 사용자가 늘어나지 않는지(=회사가 정체되어 있는지) 확인합니다. 그런 의미에서 2019년 1월부터 2020년 5월까지의 신규 사용자의 증가 추세를 계산해주세요. 최종적으로 다음의 결과가 나와야 합니다.

# <table border="1" class="dataframe" style="float: left;">
# 	<thead>
# 		<tr style="text-align: right;">
# 			<th></th>
# 			<th>name</th>
# 		</tr>
# 		<tr>
# 			<th>registration_date(ym)</th>
# 			<th></th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<th>2019-01</th>
# 			<td>13934</td>
# 		</tr>
# 		<tr>
# 			<th>2019-02</th>
# 			<td>18494</td>
# 		</tr>
# 		<tr>
# 			<th>2019-03</th>
# 			<td>16096</td>
# 		</tr>
# 		<tr>
# 			<th>2019-04</th>
# 			<td>21147</td>
# 		</tr>
# 		<tr>
# 			<th>2019-05</th>
# 			<td>25510</td>
# 		</tr>
# 		<tr>
# 			<th>2019-06</th>
# 			<td>39519</td>
# 		</tr>
# 		<tr>
# 			<th>2019-07</th>
# 			<td>30389</td>
# 		</tr>
# 		<tr>
# 			<th>2019-08</th>
# 			<td>21647</td>
# 		</tr>
# 		<tr>
# 			<th>2019-09</th>
# 			<td>22143</td>
# 		</tr>
# 		<tr>
# 			<th>2019-10</th>
# 			<td>21041</td>
# 		</tr>
# 		<tr>
# 			<th>2019-11</th>
# 			<td>16217</td>
# 		</tr>
# 		<tr>
# 			<th>2019-12</th>
# 			<td>25367</td>
# 		</tr>
# 		<tr>
# 			<th>2020-01</th>
# 			<td>34225</td>
# 		</tr>
# 		<tr>
# 			<th>2020-02</th>
# 			<td>45120</td>
# 		</tr>
# 		<tr>
# 			<th>2020-03</th>
# 			<td>84434</td>
# 		</tr>
# 		<tr>
# 			<th>2020-04</th>
# 			<td>49464</td>
# 		</tr>
# 		<tr>
# 			<th>2020-05</th>
# 			<td>15253</td>
# 		</tr>
# 	</tbody>
# </table>

import datetime as dt
users['registration_date(ym)'] = users['registration_date'].dt.strftime('%Y-%m') #datetime 객체를 문자열로 변환(https://rfriend.tistory.com/498)

# PS) 판다스(Pandas)의 [pivot_table](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html)을 사용하면 어렵지 않게 위 문제를 풀 수 있습니다.

pd.pivot_table(users, index ='registration_date(ym)', values = 'name', aggfunc = 'count')

# **12. 월별 수강권(```klass_tickets```)을 구매한 사용자 수를 구해주세요.**
#
# 이번에는 비슷한 방식으로, 신규 가입 사용자(```users```)가 아닌 실제 구매한 수강권(```klass_tickets```)을 구매한 사용자를 계산해보겠습니다. 마찬가지로 특정 연월(ex: 2020년 4월)이 아닌 전체 연월을 기준으로 계산해야 회사의 실질적인 성장세를 파악할 수 있습니다. 최종적으로 다음의 결과가 나와야 합니다.
#

# <table border="1" class="dataframe" style="float: left;">
# 	<thead>
# 		<tr style="text-align: right;">
# 			<th></th>
# 			<th>user_id</th>
# 		</tr>
# 		<tr>
# 			<th>created_at(ym)</th>
# 			<th></th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<th>2019-04</th>
# 			<td>161</td>
# 		</tr>
# 		<tr>
# 			<th>2019-05</th>
# 			<td>328</td>
# 		</tr>
# 		<tr>
# 			<th>2019-06</th>
# 			<td>3003</td>
# 		</tr>
# 		<tr>
# 			<th>2019-07</th>
# 			<td>4382</td>
# 		</tr>
# 		<tr>
# 			<th>2019-08</th>
# 			<td>4072</td>
# 		</tr>
# 		<tr>
# 			<th>2019-09</th>
# 			<td>5978</td>
# 		</tr>
# 		<tr>
# 			<th>2019-10</th>
# 			<td>9019</td>
# 		</tr>
# 		<tr>
# 			<th>2019-11</th>
# 			<td>7501</td>
# 		</tr>
# 		<tr>
# 			<th>2019-12</th>
# 			<td>8849</td>
# 		</tr>
# 		<tr>
# 			<th>2020-01</th>
# 			<td>13623</td>
# 		</tr>
# 		<tr>
# 			<th>2020-02</th>
# 			<td>11587</td>
# 		</tr>
# 		<tr>
# 			<th>2020-03</th>
# 			<td>21483</td>
# 		</tr>
# 		<tr>
# 			<th>2020-04</th>
# 			<td>15284</td>
# 		</tr>
# 		<tr>
# 			<th>2020-05</th>
# 			<td>8870</td>
# 		</tr>
# 	</tbody>
# </table>

# PS) pivot_table을 사용할 때, 집계 방식(```aggfunc```)을 [pd.Series.nunique](https://stackoverflow.com/a/51367441)로 설정하면 전체 데이터의 개수가 아닌, 고유한 데이터(```unique```)의 개수를 계산할 수 있습니다.

klass_tickets['created_at(ym)'] = klass_tickets['created_at'].dt.strftime('%Y-%m')

ticket_paid = klass_tickets['is_paid'] == 1
pd.pivot_table(klass_tickets[ticket_paid], index = 'created_at(ym)', values = 'user_id', aggfunc = pd.Series.nunique)

# **13. 카테고리(```categories```)별 운영 중인 클래스(```klasses```) 수를 구해 주세요.**

# 이번에는 수업 카테고리(```categories```)별 운영중인 클래스(```klasses```)의 개수를 구해보겠습니다. 카테고리별 클래스의 개수를 구할 수 있으면 현재 크리에이터들이 가장 활발하게 수업이 올리는 클래스가 어떤 것인지를 확인할 수 있습니다. (여기에 연월별 클래스 생성 현황까지 포함하면, 카테고리의 트렌드를 확인할 수 있는 좋은 분석 자료가 됩니다) 최종적으로 다음의 결과가 나와야 합니다.

# <table border="1" class="dataframe" style="float: left;">
# 	<thead>
# 		<tr style="text-align: right;">
# 			<th></th>
# 			<th>id</th>
# 		</tr>
# 		<tr>
# 			<th>title</th>
# 			<th></th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<th>미술</th>
# 			<td>2143</td>
# 		</tr>
# 		<tr>
# 			<th>공예</th>
# 			<td>2035</td>
# 		</tr>
# 		<tr>
# 			<th>디지털 드로잉</th>
# 			<td>1122</td>
# 		</tr>
# 		<tr>
# 			<th>라이프 스타일</th>
# 			<td>1081</td>
# 		</tr>
# 		<tr>
# 			<th>요리/음료</th>
# 			<td>865</td>
# 		</tr>
# 		<tr>
# 			<th>디자인/개발</th>
# 			<td>583</td>
# 		</tr>
# 		<tr>
# 			<th>사진/영상</th>
# 			<td>500</td>
# 		</tr>
# 		<tr>
# 			<th>부업/창업/재테크</th>
# 			<td>410</td>
# 		</tr>
# 		<tr>
# 			<th>음악</th>
# 			<td>383</td>
# 		</tr>
# 		<tr>
# 			<th>직무</th>
# 			<td>268</td>
# 		</tr>
# 		<tr>
# 			<th>시그니처</th>
# 			<td>215</td>
# 		</tr>
# 		<tr>
# 			<th>디자인</th>
# 			<td>92</td>
# 		</tr>
# 		<tr>
# 			<th>개발</th>
# 			<td>77</td>
# 		</tr>
# 		<tr>
# 			<th>DIY</th>
# 			<td>76</td>
# 		</tr>
# 		<tr>
# 			<th>자기계발</th>
# 			<td>45</td>
# 		</tr>
# 		<tr>
# 			<th>커리어</th>
# 			<td>30</td>
# 		</tr>
# 		<tr>
# 			<th>댄스</th>
# 			<td>26</td>
# 		</tr>
# 		<tr>
# 			<th>영화</th>
# 			<td>20</td>
# 		</tr>
# 		<tr>
# 			<th>홈/인테리어</th>
# 			<td>13</td>
# 		</tr>
# 		<tr>
# 			<th>악기/음악</th>
# 			<td>8</td>
# 		</tr>
# 		<tr>
# 			<th>스포츠</th>
# 			<td>8</td>
# 		</tr>
# 	</tbody>
# </table>

klass_categories = pd.merge(klasses, categories, left_on = 'category_id', right_on = 'id')

p = pd.pivot_table(klass_categories, index = 'title', values = 'category_id', aggfunc = 'count')
p.sort_values('category_id', ascending =False) #피벗테이블 value 정렬 (https://www.debugcn.com/ko/article/22734340.html)

# **14. 누적 수강생 수(```klass_tickets```)가 가장 많은 Top 10 클래스의 ID와 그 수강생 수를 구해 주세요.**

# 이번에는 클래스101에서 가장 판매량이 높은 클래스(```klasses```)를 찾아보겠습니다. 전체 클래스에서, 누적 수강생 수(```klass_tickets```)가 가장 많은 상위 10개의 클래스를 찾아주세요. 이 클래스가 클래스101 매출의 핵심이라고 볼 수 있습니다. 최종적으로 다음의 결과가 나와야 합니다.

# <table border="1" class="dataframe" style="float: left;">
# 	<thead>
# 		<tr style="text-align: right;">
# 			<th></th>
# 			<th>user_id</th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<th>lmcl8av2otsu7ewe5z46hmkf</th>
# 			<td>17022</td>
# 		</tr>
# 		<tr>
# 			<th>sz0hxjm1lp6gr15b8aum5lud</th>
# 			<td>15708</td>
# 		</tr>
# 		<tr>
# 			<th>svo3axw7j71qng7lb38y4hvp</th>
# 			<td>7062</td>
# 		</tr>
# 		<tr>
# 			<th>z3q0rfq9dclclzuxcwxbms73</th>
# 			<td>6762</td>
# 		</tr>
# 		<tr>
# 			<th>u85yqtgerauwfvpj9pz6j0bx</th>
# 			<td>6347</td>
# 		</tr>
# 		<tr>
# 			<th>zkoj2ivzj7uslzruxdnxp29c</th>
# 			<td>5851</td>
# 		</tr>
# 		<tr>
# 			<th>7ez0fe3y40h37ciew2dc8tww</th>
# 			<td>5104</td>
# 		</tr>
# 		<tr>
# 			<th>z25usytcgptslj82zop7g4ad</th>
# 			<td>4482</td>
# 		</tr>
# 		<tr>
# 			<th>wtdzp6q2tbs2aqauq28amagm</th>
# 			<td>2848</td>
# 		</tr>
# 		<tr>
# 			<th>gpa4lutkt2t2ig1k9y2bq948</th>
# 			<td>2630</td>
# 		</tr>
# 	</tbody>
# </table>

p2 = pd.pivot_table(klass_and_ticket, index = 'klass_id', values = 'user_id', aggfunc = 'count')
p2.sort_values('user_id', ascending = False).head(10)

# **15. 월별, 그리고 클래스 카테고리별 신규 구매자 수를 구해 주세요.**
#
# 마지막으로, 클래스101의 전체 판매 현황을 자세하게 확인할 수 있는 단 하나의 분석 테이블을 계산해보겠습니다. 바로 1) 월별, 2) 카테고리별, 3) 클래스의 신규 구매자 수입니다. 이 지표를 계산할 수 있다면 카테고리별로 클래스 수강생이 늘어나고 있는지(=해당 카테고리가 성장하고 있는지), 정 반대로 클래스 수강생이 늘어나지 않고 정체되고 있는지를 파악할 수 있기 때문에, 회사의 현황을 파악하기에 매우 용이합니다. 최종적으로 다음의 결과가 나와야 합니다.

# <table border="1" class="dataframe" style="float: left;">
# 	<thead>
# 		<tr style="text-align: right;">
# 			<th>title</th>
# 			<th>DIY</th>
# 			<th>개발</th>
# 			<th>공예</th>
# 			<th>디자인</th>
# 			<th>디자인/개발</th>
# 			<th>디지털 드로잉</th>
# 			<th>라이프 스타일</th>
# 			<th>미술</th>
# 			<th>부업/창업/재테크</th>
# 			<th>사진/영상</th>
# 			<th>시그니처</th>
# 			<th>악기/음악</th>
# 			<th>요리/음료</th>
# 			<th>음악</th>
# 			<th>자기계발</th>
# 			<th>직무</th>
# 			<th>커리어</th>
# 		</tr>
# 		<tr>
# 			<th>created_at(ym)</th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 			<th></th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<th>2019-04</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>161</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2019-05</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>12</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>174</td>
# 			<td>0</td>
# 			<td>48</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>52</td>
# 			<td>0</td>
# 			<td>46</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2019-06</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>279</td>
# 			<td>13</td>
# 			<td>64</td>
# 			<td>705</td>
# 			<td>97</td>
# 			<td>340</td>
# 			<td>0</td>
# 			<td>575</td>
# 			<td>604</td>
# 			<td>0</td>
# 			<td>378</td>
# 			<td>30</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2019-07</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>561</td>
# 			<td>3</td>
# 			<td>313</td>
# 			<td>608</td>
# 			<td>139</td>
# 			<td>1081</td>
# 			<td>0</td>
# 			<td>403</td>
# 			<td>1123</td>
# 			<td>0</td>
# 			<td>163</td>
# 			<td>68</td>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2019-08</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>674</td>
# 			<td>0</td>
# 			<td>186</td>
# 			<td>596</td>
# 			<td>702</td>
# 			<td>1119</td>
# 			<td>0</td>
# 			<td>339</td>
# 			<td>200</td>
# 			<td>0</td>
# 			<td>341</td>
# 			<td>61</td>
# 			<td>0</td>
# 			<td>36</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2019-09</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>828</td>
# 			<td>0</td>
# 			<td>319</td>
# 			<td>887</td>
# 			<td>1821</td>
# 			<td>1430</td>
# 			<td>9</td>
# 			<td>391</td>
# 			<td>142</td>
# 			<td>0</td>
# 			<td>241</td>
# 			<td>75</td>
# 			<td>0</td>
# 			<td>138</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2019-10</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>921</td>
# 			<td>0</td>
# 			<td>299</td>
# 			<td>1125</td>
# 			<td>759</td>
# 			<td>1435</td>
# 			<td>3723</td>
# 			<td>370</td>
# 			<td>119</td>
# 			<td>0</td>
# 			<td>250</td>
# 			<td>54</td>
# 			<td>0</td>
# 			<td>374</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2019-11</th>
# 			<td>2</td>
# 			<td>0</td>
# 			<td>917</td>
# 			<td>0</td>
# 			<td>262</td>
# 			<td>1045</td>
# 			<td>233</td>
# 			<td>1506</td>
# 			<td>2453</td>
# 			<td>337</td>
# 			<td>435</td>
# 			<td>0</td>
# 			<td>142</td>
# 			<td>330</td>
# 			<td>0</td>
# 			<td>196</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2019-12</th>
# 			<td>4</td>
# 			<td>0</td>
# 			<td>753</td>
# 			<td>0</td>
# 			<td>290</td>
# 			<td>969</td>
# 			<td>181</td>
# 			<td>1167</td>
# 			<td>3851</td>
# 			<td>429</td>
# 			<td>924</td>
# 			<td>0</td>
# 			<td>125</td>
# 			<td>209</td>
# 			<td>0</td>
# 			<td>235</td>
# 			<td>0</td>
# 		</tr>
# 		<tr>
# 			<th>2020-01</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>1041</td>
# 			<td>0</td>
# 			<td>589</td>
# 			<td>1901</td>
# 			<td>399</td>
# 			<td>2397</td>
# 			<td>5648</td>
# 			<td>789</td>
# 			<td>763</td>
# 			<td>0</td>
# 			<td>185</td>
# 			<td>230</td>
# 			<td>0</td>
# 			<td>466</td>
# 			<td>29</td>
# 		</tr>
# 		<tr>
# 			<th>2020-02</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>1513</td>
# 			<td>0</td>
# 			<td>794</td>
# 			<td>2294</td>
# 			<td>345</td>
# 			<td>1973</td>
# 			<td>3184</td>
# 			<td>556</td>
# 			<td>480</td>
# 			<td>24</td>
# 			<td>313</td>
# 			<td>135</td>
# 			<td>39</td>
# 			<td>494</td>
# 			<td>32</td>
# 		</tr>
# 		<tr>
# 			<th>2020-03</th>
# 			<td>0</td>
# 			<td>0</td>
# 			<td>3419</td>
# 			<td>9</td>
# 			<td>1135</td>
# 			<td>3394</td>
# 			<td>1287</td>
# 			<td>3298</td>
# 			<td>5816</td>
# 			<td>722</td>
# 			<td>440</td>
# 			<td>10</td>
# 			<td>589</td>
# 			<td>588</td>
# 			<td>486</td>
# 			<td>1266</td>
# 			<td>166</td>
# 		</tr>
# 		<tr>
# 			<th>2020-04</th>
# 			<td>0</td>
# 			<td>10</td>
# 			<td>1218</td>
# 			<td>0</td>
# 			<td>663</td>
# 			<td>2324</td>
# 			<td>511</td>
# 			<td>1671</td>
# 			<td>6458</td>
# 			<td>726</td>
# 			<td>403</td>
# 			<td>14</td>
# 			<td>181</td>
# 			<td>346</td>
# 			<td>203</td>
# 			<td>1190</td>
# 			<td>92</td>
# 		</tr>
# 		<tr>
# 			<th>2020-05</th>
# 			<td>0</td>
# 			<td>4</td>
# 			<td>666</td>
# 			<td>4</td>
# 			<td>495</td>
# 			<td>1562</td>
# 			<td>564</td>
# 			<td>1237</td>
# 			<td>3306</td>
# 			<td>284</td>
# 			<td>130</td>
# 			<td>4</td>
# 			<td>135</td>
# 			<td>308</td>
# 			<td>145</td>
# 			<td>567</td>
# 			<td>35</td>
# 		</tr>
# 	</tbody>
# </table>

# +
m = pd.merge(klass_tickets, klasses, left_on = 'klass_id', right_on = 'id')
m2 = pd.merge(m, categories, left_on = 'category_id', right_on = 'id')

pd.pivot_table(m2[m2['is_paid'] == 1], index = 'created_at(ym)', columns = 'title', values = 'user_id', aggfunc = pd.Series.nunique,fill_value = 0)
# -

# ## 제출
#
# 과제를 다 끝내셨으면 http://bit.ly/ds-assignment 에서 안내에 따라 과제를 제출하여 주세요! 과제를 제출해주시면 솔루션과 검토 결과를 드립니다. 오프라인 수업의 경우 과제를 제출하지 않으시더라도 솔루션은 다음 수업 시간에 제공해드립니다.
#
# 수업이나 과제 관련 질문, 수료증 문의 등은 담당 튜터(조교)에게 문의 주세요. 영수증 발급 등의 문의는 support@dsschool.co.kr 로 메일 주시면 담당자분이 응대해주실 겁니다. 기타 궁금한 사항은 슬랙으로 문의 주세요!


