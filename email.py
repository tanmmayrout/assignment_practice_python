import re  # Importing regular expression

def fun(s):

    email_pattern = r'^[\w|\-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'  # return True if s is a valid email, else return False Found on internet
    m = re.match(email_pattern, s)
    return m
