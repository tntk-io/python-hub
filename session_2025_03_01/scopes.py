# Global
def edit_text():
    global text
    text = input('Prompting the user again: ')


text = input('Initial input (will be overwritten): ')
print('Initial input:', text)
edit_text()
print('Input after second prompt:', text)


# Nonlocal
def modify(x):
    print('Locals:', locals())
    print('Globals:', globals())
    print('Before square:', x)

    def square():
        nonlocal x
        x = x ** 2

    square()
    print('After square:', x)


x = 10
print('Global:', x)
modify(x)
print('Global after modify:', x)
