__author__ = 'nekmo'

def human_join(list, and_='and', sep=', '):
    if len(list) == 1:
        return list[0]
    return '%s %s %s' % (sep.join(list[:-1]), and_, list[-1])