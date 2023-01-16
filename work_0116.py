# 5.4

salutation = 'Professor'
name = 'David'
product = 'coffee machine'
verbed = 'was crashed'
room = 'office'
animals = 'rabbit'
amount = '20$'
percent = 10
spokesman = 'SoYoung'
job_title = 'Manager'


letter = f'''
\tDear {salutation} {name}.
\tThank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.

\tSend us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.

\tThank you for your support.
\tSincerely,
{spokesman}
{job_title}
'''

print(letter)


# 5.5
letter = '''
\tDear {} {}.
\tThank you for your letter. We are sorry that our {} {} in your {}. Please note that it should never be used in a {}, especially near any {}.

\tSend us your receipt and {} for shipping and handling. We will send you another {} that, in our tests, is {}% less likely to have {}.

\tThank you for your support.
\tSincerely,
{}
{}
'''
print(letter.format(salutation, name, product, verbed, room, room, animals, amount, product, percent, verbed, spokesman, job_title))


# 5.6

duck = 'duck'.title()
gourd = 'gourd'.title()
spitz = 'spitz'.title()

print('%sy Mc%sface' % (duck, duck))
print('%sy Mc%sface' % (gourd, gourd))
print('%sy Mc%sface' % (spitz, spitz))

# 5.7
print('{}y Mc{}face'.format(duck, duck))
print('{}y Mc{}face'.format(gourd, gourd))
print('{}y Mc{}face'.format(spitz, spitz))

#5.8
print(f'{duck}y Mc{duck}face')
print(f'{gourd}y Mc{gourd}face')
print(f'{spitz}y Mc{spitz}face')

#6.2
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    number += 1

#6.3
quess_me = 5
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
