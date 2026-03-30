
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

# 1. Vẽ lưới 2x2
print("--- Lưới 2x2 ---")
do_twice(print_row)
print_beams()

# 2. Vẽ lưới 4x4
def print_beams4():
    do_four(print_beam)
    print('+')

def print_posts4():
    do_four(print_post)
    print('|')

def print_row4():
    print_beams4()
    do_four(print_posts4)

print("\n--- Lưới 4x4 ---")
do_four(print_row4)
print_beams4()