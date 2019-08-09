import check50
import check50.c

@check50.check()
def exists():
    """fahrenheit.c exists"""
    check50.exists("fahrenheit.c")



def number(num):
    return fr"(?<!\d){num.replace('.', '\\.')}(?!\d)"
