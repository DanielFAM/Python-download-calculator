def time_generator (size,speed):
    return size / speed;

def time_download_calculator(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds-hours*3600)/60)
    seconds = int(seconds-(hours*3600 + minutes*60))
    print ('Estimated time for download: ', hours,'Hours ',minutes,'Minutes ',seconds, 'Seconds ' )


if __name__ == '__main__':
    print('<-------------------------Time download calculator------------------------------>')
    
    speed = int(input('Input the speed of your internet in Megabits for second: '))
    election = int(input('Select the size of the file: \n1.KB\n2.MB\n3.GB\n'))

    if election == 1:
        size = int(input('Input the size of file in KiloBytes: '))
        size = size * 0.008
        result = time_generator (size, speed)
        time_download_calculator(result)

    elif election == 2:
        size = int(input('Input the size of file in MegaBytes: '))
        size = size * 8
        result = time_generator (size, speed)
        time_download_calculator(result)

    elif election == 3:
        size = int(input('Input the size of file in GigaBytes: '))
        size = size * 8000
        result = time_generator (size, speed)
        time_download_calculator(result)
    
    else:
        print('Wrong election, please try again....\n')

    

   