import os
import cx_Oracle
import configparser

# 한글 쿼리를 지원하게 하기 위해 사용
os.environ["NLS_LANG"] = ".AL32UTF8"

# Config 파일 읽기
config = configparser.ConfigParser()
# 한글 Config를 읽으려면 뒤에 encoding값이 필요
config.read("./config.ini", encoding='utf-8')

database = config["database"]
con = cx_Oracle.connect(database["connectionString"])
cur = con.cursor()

selectQueryString = database['selectQueryString']
insertQueryString = database['insertQueryString']

for row in cur.execute(selectQueryString):
  print(row)

# Insert 후에는 Commit 필수
cur.execute(insertQueryString)
con.commit()