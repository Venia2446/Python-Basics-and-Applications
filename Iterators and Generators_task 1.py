class multifilter:
    def judge_half(pos, neg): # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        pass
    def judge_any(pos, neg):# допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        pass
    def judge_all(pos, neg):# допускает элемент, если его допускают все функции (neg == 0)
        pass

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.itterables = iterable  # iterable - исходная последовательность
        self.funcs = [*funcs]# funcs - допускающие функции
        self.judge = judge # judge - решающая функция
        self.pos = 0
        self.neg = 0
    def __iter__(self): # возвращает итератор по результирующей последовательности
        for z in self.itterables:
            for x in self.funcs:
                if x(z) == True: # идея что мы перебираем функции и записываем в отдельный список
                    self.pos += 1
                else:
                    self.neg+=1
            yield self.judge(pos = self.pos, neg = self.neg) #берёт элемент прогоняет по внешним ункцийия - в зависимости от выбранной функции judje - какое будет решение - если условие допуска элемента True то оно его возвразает - если нет (False) то идёт к следующему элементу




def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]




print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))

