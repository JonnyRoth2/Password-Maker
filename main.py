from random import randint

def create_password():
    character_count=input("How many characters in you password do you want ")
    
    count=0
    passwords=''
    if character_count.isdigit():
        numbers_characters=int(character_count)    
        numbers_password=input("Do you want numbers in your password please type y for yes n for no ")
        symbol_password=input("Do you want symbols in your password please type y for yes n for no ")
        if symbol_password=='y' and numbers_password=='y':
            while count<numbers_characters:
                count+=1
                random_ascii=randint(33,126)
                transformed_character=chr(random_ascii)
                passwords+=transformed_character
            return passwords
        elif numbers_password=='y' and symbol_password=='n':
            while count<numbers_characters:
                count+=1
                random_ascii1=randint(48,57)
                random_ascii2=randint(65,90)
                random_ascii3=randint(97,122)
                random_ascii=randint(0,2)
                if random_ascii==0:
                    transformed_character=chr(random_ascii1)
                    passwords+=transformed_character
                elif random_ascii==1:
                    transformed_character=chr(random_ascii2)
                    passwords+=transformed_character
                elif random_ascii==2:
                    transformed_character=chr(random_ascii3)
                    passwords+=transformed_character
            return passwords
        elif numbers_password=='n' and symbol_password=='n':
            while count<numbers_characters:
                count+=1
                random_ascii4=randint(97,122)
                random_ascii5=randint(65,90)
                random_ascii=randint(0,1)
                if random_ascii==0:
                    transformed_character=chr(random_ascii4)
                    passwords+=transformed_character
                elif random_ascii==1:
                    transformed_character=chr(random_ascii5)
                    passwords+=transformed_character
            return passwords
        else:
            while count<numbers_characters:
                count+=1
                random_ascii6=randint(33,47)
                random_ascii7=randint(58,126)
                random_ascii=randint(0,1)
                if random_ascii==0:
                    transformed_character=chr(random_ascii6)
                    passwords+=transformed_character
                elif random_ascii==1:
                    transformed_character=chr(random_ascii7)
                    passwords+=transformed_character
            return passwords
    else:
        return 'x'


def write_password(password:str):
    newlines=''
    user_file=input("please input your file name ")
    what_for=input("please enter what this password goes to ")
    words=['\n',what_for, '-', password,'\n']
    with open(user_file,'r+') as f:
        for line in f:
            if len(line)>0:
                newlines+'\n'
        for word in words:
            f.write(newlines+word)
def main():
    begin=input("Would you like to create a password y for yes n for no ")
    if begin=='y':
        password=create_password()
        #Perhaps a hash function could go here
        if password=='x':
                print("ERROR A CHARACTER HAS BEEN ENTERED THAT IS NOT A NUMBER PLEASE TRY AGAIN")
        else:
            write_password(password)
    else:
        print("No password requested")

main()
