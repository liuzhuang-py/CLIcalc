import operator

op_list = [
    ('+',operator.add),
    ('-',operator.sub),
    ('*',operator.mul),
    ('/',operator.truediv),
]

def get_func(op_str):
    return dict(op_list)[op_str]

def calc():
    print("=========计算器ctrl+c退出===========")
    print("liuzhuang software calc v2.0")
    while True:
        try:
            a = float(input("数字一："))
            op = input("运算符:")
            b = float(input("数字二："))
            fn = get_func(op)
            res = fn(a, b)
            print(f"结果:{res} ")
        except KeyError:
           print("运算符error 0X000001")
        except ValueError:
            print("数字error 0X000002")
        except ZeroDivisionError:
            print("除数为0error 0X000003")
        except KeyboardInterrupt:
            print("\n退出")
            return

calc()