def format_task_date(task_date):
    try:
        return task_date.strftime('%d.%m.%Y %H:%M')

    except ValueError:
        # Обработка случая, если формат даты не соответствует ожидаемому
        return "Некорректная дата"