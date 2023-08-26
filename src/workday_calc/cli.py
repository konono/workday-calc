import arrow
import jpholiday
import os
import workdays

from argparse import ArgumentParser


def parser():
    usage = (f'python3 {format(os.path.basename(__file__))} -s <date> -e <date> [option]\n'
             'Available date formats is following: \n'
             'YYYY-MM-DD, YYYY-M-DD, YYYY-M-D, YYYY/MM/DD, YYYY/M/DD,'
             'YYYY/M/D, YYYY.MM.DD, YYYY.M.DD, YYYY.M.D, YYYYMMDD')
    argparser = ArgumentParser(usage=usage)

    date_group = argparser.add_argument_group("date")
    date_group.add_argument('--start', '-s', type=str,
                            dest='start_date', required=True)
    date_group.add_argument('--end', '-e', type=str,
                            dest='end_date', required=True)
    argparser.add_argument('--without_workday', '-w', action='store_true', required=False,
                           help='To calculate the number of days without considering working days,\
                                 specify the WITHOUT_WORKDAY option.')
    argparser.add_argument('--debug', action='store_true', required=False,
                           help='debug option')
    args = argparser.parse_args()
    return args


def workdays_calc(args):
    start_date = arrow.get(args.start_date)
    end_date = arrow.get(args.end_date)
    print(f'start_date: {start_date.format("YYYY/MM/DD")}')
    print(f'end_date: {end_date.format("YYYY/MM/DD")}')
    if args.without_workday:
        print(f'days: {(end_date - start_date).days} days')
    else:
        jphd = jpholiday.between(start_date.datetime, end_date.datetime)
        holidays = [arrow.get(d[0].strftime("%Y/%m/%d")) for d in jphd]
        # convert datetime.date to arrow -> arrow.get(d[0].strftime("%Y/%m/%d")
        print(f'workdays: '
              f'{(workdays.networkdays((start_date), arrow.get(end_date), holidays=holidays))} days')
        if args.debug:
            print('holidays:')
            for d in jphd:
                print(d)


def main():
    args = parser()
    workdays_calc(args)


if __name__ == "__main__":
    main()