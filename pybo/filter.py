# Date 포맷팅 필터
def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)