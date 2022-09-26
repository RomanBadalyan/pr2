import PySimpleGUI as sg
import re
import hashlib

## @package pyexample
#  Documentation for this module.
#
#  More details.

# тут мы добавили коммит

    ## Documentation for a method.
    #  @param self The object pointer.
    
def hash(fname, algo):
## this function allows you to select one of the hashing methods, then accesses the desired library
#   Args:
#       fname: file
#       algo: str
#       hash: hash
#   Returns:
#       hash.hexdigest().
#   Examples:
#       >>> check right files
#       GUI, hash
#
#       >>> check first file
#       print('Error: File 1 path not valid.')
#
#       >>> check second file
#       print('Error: File 1 path not valid.')
#
#       >>> values[1] is not True and values[2] is not True and values[4] is not True:
#       print('Error: Choose at least one type of Encryption Algorithm')
#
#       >>> invalid file name
#       print('Files do NOT match for ', algo)
##

    if algo == 'MD5':
        hash = hashlib.md5()
    elif algo == 'SHA1':
        hash = hashlib.sha1()
    elif algo == 'SHA256':
        hash = hashlib.sha256()
    with open(fname) as handle: #opening the file one line at a time for memory considerations
        for line in handle:
            hash.update(line.encode(encoding = 'utf-8'))
    return(hash.hexdigest())
layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('MD5'), sg.Checkbox('SHA1')
     ],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('SHA256')
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('File Compare', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        file1 = file2 = isitago = None
        # print(values[0],values[3])
        if values[0] and values[3]:
            file1 = re.findall('.+:\/.+\.+.', values[0])
            file2 = re.findall('.+:\/.+\.+.', values[3])
            isitago = 1
            if not file1 and file1 is not None:
                print('Error: File 1 path not valid.')
                isitago = 0
            elif not file2 and file2 is not None:
                print('Error: File 2 path not valid.')
                isitago = 0
            elif values[1] is not True and values[2] is not True and values[4] is not True:
                print('Error: Choose at least one type of Encryption Algorithm')
            elif isitago == 1:
                print('Info: Filepaths correctly defined.')
                algos = [] #algos to compare
                if values[1] == True: algos.append('MD5')
                if values[2] == True: algos.append('SHA1')
                if values[4] == True: algos.append('SHA256')
                filepaths = [] #files
                filepaths.append(values[0])
                filepaths.append(values[3])
                print('Info: File Comparison using:', algos)
                for algo in algos:
                    print(algo, ':')
                    print(filepaths[0], ':', hash(filepaths[0], algo))
                    print(filepaths[1], ':', hash(filepaths[1], algo))
                    if hash(filepaths[0],algo) == hash(filepaths[1],algo):
                        print('Files match for ', algo)
                    else:
                        print('Files do NOT match for ', algo)
        else:
            print('Please choose 2 files.')
window.close()
