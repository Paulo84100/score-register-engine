# functions



def notend() :
    noend = input()



def usage() :
    statement = input("a = view scores b = register a score\n")
    if statement == 'a' or statement == 'b' :
        print ("Ok")
        type(statement)
    else :
        print ("please select a or b\n")
        usage()


def type(letter) :
    if letter == 'a' :
        filename()
    else :
        Write()




def filename() :
    selectfile = input('type a for best score, b for last score, c for old scores and d for quit the read part\n')
    if selectfile == 'a' or selectfile == 'b' or selectfile == 'c' or selectfile == 'd' :
        ReadFile(selectfile)
    else :
        print ('please type a, b, c or d\n')
        filename()




def ReadFile(file) :
    if file == 'a' :
        file = open('best score.txt', 'r')
        cont = file.read()
        print ("\n\n\nYour best score is : "+cont+'\n\n\n')
        file.close()
        usage()
    elif file == 'b' :
        file = open('actual score.txt', 'r')
        cont = file.read()
        print ("\n\n\nYour last score is : "+cont+'\n\n\n')
        file.close()
        usage()
    elif file == 'c' :
        file = open('old score.txt', 'r')
        cont = file.read()
        print ("\n\n\nYour historic of score is : "+cont+'\n\n\n')
        file.close()
        usage()
    else :
        usage()
    

    
def Write() :
    a = input('Type a for write a new record and b for clean files\n')
    if a == 'a' or a == 'b' :
        WriteFile(a)
    else :
        print('Please type a or b\n')
        Write()
    







def WriteFile(f) :
    if f == 'a' :
        r = input('What is your new record in seconds not decimal ?\n')
        file = open('actual score.txt', 'w')
        file.write(r)
        file.close()
        file = open('old score.txt', 'r')
        cont = file.read()
        file.close()
        file = open('old score.txt', 'w')
        file.write(r+'-'+cont)
        file.close()
        file = open('best score.txt', 'r')
        cont = file.read()
        file.close()
        if r<cont or cont == '':
            file = open('best score.txt', 'w')
            file.write(r)
            file.close()
        print('\nscore saved\n')
        usage()
    else :
        t = input('are you sure ? Y/N\n')
        if t == 'Y' or t == 'y' :
            file = open('actual score.txt', 'w')
            file.write('')
            file.close
            file = open('old score.txt', 'w')
            file.write('')
            file.close
            file = open('best score.txt', 'w')
            file.write('')
            file.close
            print('files cleaned')
            usage()
        
        usage()
    usage()







# welcome message
print('Welcome to score register engine\n')
usage()
notend()
