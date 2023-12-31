# workday-calc
## 概要
土日、日本の祝日を加味して**working day**を計算してくれるツールです。

細かい話ではありますが、workking dayつまりは稼働日という考え方なので、開始日: 2023/8/27、終了日: 2023/8/27と入力した場合は1daysと返ってくる仕様になっています。

産休申請をする際に期間の他にworkdayも必要と言われたので、ツールを探したのですがパッと見つからなかったので作りました。

インストール方法
```
pip3 install https://github.com/konono/workday-calc
```

## 使い方
--start(-s): 開始日時を入力します(オプションです、入力をしなかった場合今の日付が入力されます)

--end(-e): 終了日時を入力します

--holidays: 日本の祝日以外の祝日(E.g. company holidayなど)を入力します。スペース区切りでdateフォーマットを入力してください。

dateの入力については以下のフォーマットが許容されています:

YYYY-MM-DD, YYYY-M-DD, YYYY-M-D, YYYY/MM/DD, YYYY/M/DD,YYYY/M/D, YYYY.MM.DD, YYYY.M.DD, YYYY.M.D, YYYYMMDD

--with-holiday(-w): **土日、祝日を加味しない開始日を含む、開始日から終了日までの日数**を計算します。

--debug: 与えられた期間にある祝日を表示します

```
❯ python3 cli.py --help
usage: python3 cli.py -s <date> -e <date> [option]
Available date formats is following:
YYYY-MM-DD, YYYY-M-DD, YYYY-M-D, YYYY/MM/DD, YYYY/M/DD,YYYY/M/D, YYYY.MM.DD, YYYY.M.DD, YYYY.M.D, YYYYMMDD

options:
  -h, --help            show this help message and exit
  --with-holiday, -w
                        To calculate the number of days with holiday.
  --debug               debug option

date:
  --start START_DATE, -s START_DATE
  --end END_DATE, -e END_DATE
  --holidays [HOLIDAYS ...]
                        A list of date format, space delimiter
```

## 使用例

```
❯ workday-calc -s 2023/10/18 -e 2024/01/31
start_date: 2023/10/18
end_date: 2024/01/31
workdays: 72 days

❯ python3 cli.py -s 2023/10/18 -e 2024/01/31 --holidays 2024/1/2 2024/1/3
start_date: 2023/10/18
end_date: 2024/01/31
workdays: 70 days

❯ workday-calc -s 2023/10/18 -e 2024/01/31 -w
start_date: 2023/10/18
end_date: 2024/01/31
days: 106 days

❯ workday-calc -s 2023/10/18 -e 2024/01/31 --debug
start_date: 2023/10/18
end_date: 2024/01/31
workdays: 72 days
holidays:
(datetime.date(2023, 11, 3), '文化の日')
(datetime.date(2023, 11, 23), '勤労感謝の日')
(datetime.date(2024, 1, 1), '元日')
(datetime.date(2024, 1, 8), '成人の日')
```
