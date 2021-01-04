# seoul-gyeonggi-metro-boarding
Docker, Elasticsearch, Kibana를 이용한 수도권 지하철 승하차 인원 모티너링, 분석하는 토이 프로젝트


## output
* 데이터 실시간 시각화
* 2020-06-01 ~ 2020-12-16 까지의 지하철 승하차 인원에 대한 대시보드
![localhost_5601_app_kibana (1) (1)](https://user-images.githubusercontent.com/55729930/102807245-a2af8500-4401-11eb-8d81-e2c756d6620b.png)

## crawling
* 서울시 공공데이터 open api 데이터를 크롤링

## todo
* 코드정리
  * `run.py`, `crawl.py`, `put_es.py`, `conf.py`로 코드 분할하기
  * PEP 8 Style Guide 따르도록 수정하기.
