#########################
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object
# without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
#########################


# Decorated function
def escape_unicode(f):
    def wrap(*args, **kwargs):
        text = f(*args, **kwargs)
        return ascii(text)
    return wrap


def display_text(text):
    return ascii(text)


@escape_unicode
def display_text_ascii(text):
    return text


if __name__ == '__main__':
    # print('మీరు ఎలా ఉన్నారు?')
    # print(ascii('మీరు ఎలా ఉన్నారు?'))
    print(display_text('మీరు ఎలా ఉన్నారు?'))
    print(display_text_ascii('మీరు ఎలా ఉన్నారు?'))


"""
Output:

'\u0c2e\u0c40\u0c30\u0c41 \u0c0e\u0c32\u0c3e \u0c09\u0c28\u0c4d\u0c28\u0c3e\u0c30\u0c41?'
'\u0c2e\u0c40\u0c30\u0c41 \u0c0e\u0c32\u0c3e \u0c09\u0c28\u0c4d\u0c28\u0c3e\u0c30\u0c41?'
"""

