# Задача 3 - Генератор расписания. Создайте функцию, генерирующую
# расписание рабочих дней сотрудника.
#
# Условия:
# Функция принимает количество дней на которые нужно составить расписание,
# количество дней работы, количество дней отдыха и дату начала расписания.
# Функция возвращает расписание рабочих дней сотрудника, которое генерируется начиная
# с start_date на days дней вперед, учитывая что сотрудник чередует
# рабочие дни(work_days) и дни отдыха (rest_days).
# Функция должна вернуть данные в формате List[datetime.datetime]
#
# Тесты:
# days: 5, work_days: 2, rest_days: 1, start_date: datetime(2020, 1, 30) - >
#
# [
# datetime.datetime(2020, 1, 30, 0, 0),
# datetime.datetime(2020, 1, 31, 0, 0),
#  	datetime.datetime(2020, 2, 2, 0, 0),
# datetime.datetime(2020, 2, 3, 0, 0)
# ]
import datetime
days = 5
work_days = 2
rest_days = 2
start_date = datetime.datetime(2020, 1, 30)

def timetable(days, work_days, rest_days, start_date = datetime.datetime.now()):

    end_date = start_date + datetime.timedelta(days=days - 1)
    step = datetime.timedelta(days=1)

    work_step = datetime.timedelta(days=work_days)
    rest_step = datetime.timedelta(days=rest_days)


    timetable = [start_date]

    date = start_date
    while date < end_date:
        date += step
        if start_date + work_step == date:
            continue

        timetable.append(date)

    return timetable

print(timetable(days, work_days, rest_days, start_date))

