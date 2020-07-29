# 공개되어 있는 데이터를 이용해 나만의 데이터분석 기록소
## 데이터 분석 프로세스
1. Python에 기반한 웹 크롤링 라이브러리를 이용해 데이터 수집
  - BeautifulSoup 
  - Selenium
  - Scrapy
2. 수집한 데이터를 데이터 종류에 맞게 데이터베이스에 서빙
  - RDBMS인 MySQL
  - NoSQL인 MongoDB 
3. 데이터베이스에 저장한 데이터를 추출하여 데잍 전처리, 분석
  - SQL 쿼리를 이용해 직접 데이터베이스에서 추출
  - 데이터베이스의 데이터를 csv파일로 export하여 추출
  - 대화형 인터페이스인 Jupyter notebook을 이용해 데이터 EDA, 시각화, 전처리, 분석 진행
4. 분석한 내용을 기반으로 해결하고자 하는 문제에 맞는 예측 모델링 진행
  - 통계에 기반한 모델(eg.ARIMA) 사용
  - 딥러닝을 포함한 머신러닝 모델 사용
    * Scikit-learn
    * Tensorflow Backend를 사용하는 Keras

