def time_generator (size,speed):
    return size / speed;


if __name__ == '__main__':
    print('<-------------------------Time download calculator------------------------------>')
    
    speed = int(input('Input the speed of your internet in Megabits for second: '))
    election = int(input('Select the size of the file: \n1.KB\n2.MB\n3.GB\n'))

    if election == 1:
        size = int(input('Input the size of file in KiloBytes: '))
        size = size * 0.008
        result = time_generator (size, speed)

    elif election == 2:
        size = int(input('Input the size of file in MegaBytes: '))
        size = size * 8
        result = time_generator (size, speed)

    elif election == 3:
        size = int(input('Input the size of file in GigaBytes: '))
        size = size * 8000
        result = time_generator (size, speed)
        print (result)
    
    else:
        print('Wrong election, please try again....\n')

    

   