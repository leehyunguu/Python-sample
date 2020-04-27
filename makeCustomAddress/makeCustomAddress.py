import glob, os
import configparser
import csv
import itertools

# DB에 넣을 파일 읽기(여러개)
fileList = glob.glob("makeCustomAddress/*.txt")
print(fileList)
do = {}
si = {}
dong = {}
idx = 0
for file in fileList:
  with open(file, 'r', encoding="utf-8") as textFile:
    csvData = csv.reader(textFile, delimiter="|")
    for row in itertools.islice(csvData, 1, None):
      if row[1] not in do:
        do[row[1]] = row[7][:2]
      if row[1] + ',' + row[3] not in si:
        si[row[1] + ',' + row[3]] = row[7][:5]
      if row[1] + ',' + row[3] + ',' + row[19] not in dong and row[19] is not '':
        idx = idx + 1
        dong[row[1] + ',' + row[3] + ',' + row[19]] = row[7][:5] + str(idx).zfill(7)

resultFile = open('makeCustomAddress/결과2.csv', "w", encoding="utf-8", newline='')
writer = csv.writer(resultFile)
for key, value in do.items():
  writer.writerow([value, key, '1'])
  
for key, value in si.items():
  writer.writerow([value, key.split(',')[1], '2'])
  
for key, value in dong.items():
  writer.writerow([value, key.split(',')[2], '3'])

resultFile.close()