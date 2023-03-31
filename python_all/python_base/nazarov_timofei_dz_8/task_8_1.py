import re
RE_EMAIL_VAL = re.compile(r'^[a-z0-9]+([a-z0-9._-][a-z0-9]+)+[@][a-z0-9]+([a-z0-9-][a-z0-9]+)+\.[a-z]+$')


def email_parse(mail):
    mail = mail.lower()
    if not RE_EMAIL_VAL.match(mail):
        msg = f'wrong e-mail: {mail}'
        raise ValueError(msg)
    else:
        result = re.match(r'(?P<username>\S+)@(?P<domain>\S+)', mail).groupdict()
        return result


print(email_parse('m_0-Li.il@ma-il.ru'))
