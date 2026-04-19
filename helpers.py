class DateFormatter:

    #форматируем переданную дату к формату: (число)-е (название месяца)
    @staticmethod
    def format_date(date):

        months = {
            1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
            5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
            9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
        }
        day = date.day
        month = months[date.month]
        return f"{day}-е {month}"
