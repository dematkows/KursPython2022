def format_less_than_10(day):
    if day < 10:
        return "0" + str(day)
    else:
        return day


def show_month(name, days):
    print(name)
    print()
    for day in days:
        day += 1
        if day % 7 == 0:
            print(format_less_than_10(day))
        else:
            print(format_less_than_10(day), end="\t")
    print()
    print()


data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

data = dict(data)

for name, days_range in data.items():
    show_month(name, days_range)
