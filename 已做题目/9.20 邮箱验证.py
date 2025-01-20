def count_at(mail):
    return mail.count('@')==1

def head_tail(mail):
    return mail[0]!= '@' and mail[-1]!= '@' and mail[0]!= '.' and mail[-1]!= '.'

def at_dot(mail):
    at_pos=mail.find('@')
    if mail[at_pos+1]=='.' or mail[at_pos-1]=='.':
        return False
    return "." in mail[at_pos:]

while True:
    try:
        email=input()
        if count_at(email) and head_tail(email) :
            print('YES' if at_dot(email) else 'NO')
        else:
            print('NO')
    except EOFError:
        break





