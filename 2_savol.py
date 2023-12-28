# 2.(multithreading,decorators)
# Berilgan sonni teskarisini hisoblab beradigan funksiya yarating. Foydalanuvchi tomonidan probel bilan kiritilgan sonlarni alohida threadlarda hisoblab beradigan dastur tuzing.
# @printer nomli decorator yarating va bu funksiya qaytargan natijani konsolda chiqarib bersin.


from threading import Thread
def printer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print('teskari son=', result)
        return result
    return inner
@printer
def teskarison(son):
    s=str(son)
    ls=list()
    for i in s:
        ls.append(i)
    x=0
    for k in range(len(ls)):
        x+=int(ls[k])*(10**k)
    return x




if __name__ == "__main__":
    ls = list(map(int, input('sonlarni probel bilan kiriting\n').split(' ')))

    threads = []
    for i in ls:
        t = Thread(target=teskarison, args=(i,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
