# 1. Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp. W pętli spróbuj wykonać
# dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
items = [13, 'string', 2.45, 0, {}, True, False, []]

for i in items:
    try:
        x = i / 10
        print(x)
    except TypeError:
        print("Type error for", i)
    except ZeroDivisionError:
        print("zero div error", i)
