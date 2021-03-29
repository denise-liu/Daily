import random

play_game='y'
start =1
end =100
direction ="N"
smallest =start
larget = end

while play_game=='y':
    smallest =start
    larget = end
    print('Guess a number! between 1 and 100:')
    try_number=random.randint(start,end)
    print(try_number)
    counter=0
    direction="N"
    while direction!='C':
        direction=input('Is it too large(L),too small(s),or correct(C)')
        if direction=='S':
            if try_number>smallest:
                smallest=try_number+1
            try_number=random.randint(smallest,larget)
            print(try_number)
        if direction=="L":
            if try_number<larget:
                larget=try_number-1
                try_number=random.randint(smallest,larget)
                print(try_number)
        counter=counter+1
    print("I got it! I tried "+str(counter)+ 'times.')
    play_game=input('Continue?')