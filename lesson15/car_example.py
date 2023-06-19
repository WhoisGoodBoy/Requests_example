def recieve_something(something):
    if type(something) == str:
        return something + 'modified_version'
    elif type(something) == int:
        return (something + 1)
    else:
        print('we receive only str and int')
        return something

print(recieve_something(5))
print(recieve_something('five'))
print(recieve_something([5]))

