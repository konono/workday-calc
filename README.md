# workday-calc
## 概要
土日、日本の祝日を加味してworking dayを計算してくれるツールです。

産休申請をする際に期間の他にworkdayも必要と言われたので、ツールを探したのですがパッと見つからなかったので作りました。

インストール方法
```
pip3 install workday-calc
or
pip3 install git+https://github.com/konono/workday-calc
```

## 使い方
--start(-s): 開始日時を入力します

--end(-e): 終了日時を入力します

dateの入力については以下のフォーマットが許容されています:
YYYY-MM-DD, YYYY-M-DD, YYYY-M-D, YYYY/MM/DD, YYYY/M/DD,YYYY/M/D, YYYY.MM.DD, YYYY.M.DD, YYYY.M.D, YYYYMMDD


--without_workday(-w): **土日、祝日を加味しない日数**を計算します。

--debug: 与えられた期間にある祝日を表示します

```
❯ workday-calc --help
usage: python3 cli.py -s <date> -e <date> [option]
Available date formats is following:
YYYY-MM-DD, YYYY-M-DD, YYYY-M-D, YYYY/MM/DD, YYYY/M/DD,YYYY/M/D, YYYY.MM.DD, YYYY.M.DD, YYYY.M.D, YYYYMMDD

options:
  -h, --help            show this help message and exit
  --without_workday, -w
                        To calculate the number of days without considering working days, specify the
                        WITHOUT_WORKDAY option.
  --debug               debug option

date:
  --start START_DATE, -s START_DATE
  --end END_DATE, -e END_DATE
```

## 使用例

```
❯ workday-calc -s 2023/10/18 -e 2024/01/31
start_date: 2023/10/18
end_date: 2024/01/31
workdays: 72 days

❯ workday-calc -s 2023/10/18 -e 2024/01/31 -w
start_date: 2023/10/18
end_date: 2024/01/31
days: 105 days

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
