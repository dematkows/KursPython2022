def uppercase_decorator(func_param):
    def make_big():
        text = func_param()
        return text.upper()

    return make_big


@uppercase_decorator
def get_string():
    return "Hakuna Matata"


print(get_string())
