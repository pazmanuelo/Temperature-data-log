from time import sleep, strftime


def getTemp():
    '''Funcion para obtener
    la lactura de temperatura del sensor'''
    # Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before.
    tfile = open("/sys/bus/w1/devices/28-031656979fff/w1_slave")
    # Read all of the text in the file.
    text = tfile.read()
    # Close the file now that the text has been read.
    tfile.close()
    # Split the text with new lines (\n) and select the second line.
    secondline = text.split("\n")[1]
    # Split the line into words, referring to the spaces, and select the 10th word (counting from 0).
    temperaturedata = secondline.split(" ")[9]
    # The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
    temp = int(temperaturedata[2:])
    # Put the decimal point in the right place and display it.
    temp = format(temp / 1000, ".2f")
    return temp

now = strftime("%H%M--%d-%m-%Y")

def write_data(temp):
    with open("Temdata " + now + ".csv", "a",
              newline="") as log:
        log.write("{0},{1}\n".format(str(temp), strftime("%H%M%S")))

while True:
    temp = getTemp()
    write_data(temp)
    sleep(10)
