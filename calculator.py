def time_generator (size,speed):
    return size / speed;


if __name__ == '__main__':
    print('<-------------------------Time download calculator------------------------------>')
    
    speed = input('Input the speed of your internet: ')
    election = input('Select the size of the file: \n1.KB\n2.MB\n3.GB\n')

    if election == 1:
        size = input('Input the size of file in KiloBytes: ')
        size = size * 0.008
        result = time_generator (size, speed)

    elif election == 2:
        size = input('Input the size of file in MegaBytes: ')
        size = size * 8
        result = time_generator (size, speed)

    elif election == 3:
        size = input('Input the size of file in GigaBytes: ')
        size = size * 8000
        result = time_generator (size, speed)

    

   