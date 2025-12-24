# def hello(n):
#     for i in range(0,n):
#         print("Hello user")

# hello(4)

# def hello():
#     return 'hello my man'
# print(hello().upper())

def hello(greetings,name = 'You'):
    return '{} {} you are Greetings'.format(greetings,name)

print(hello('HI','Yashwanth').lower())