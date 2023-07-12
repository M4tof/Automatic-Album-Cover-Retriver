import os
import time
from datetime import datetime, date
from mutagen import File

def StringToDate(StringData):
    correct=StringData[2]
    months = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
         'may': '05',
         'jun': '06',
         'jul': '07',
         'aug': '08',
         'sep': '09',
         'oct': '10',
         'nov': '11',
         'dec': '12'
        }
    Mon=StringData[1].lower()
    Mon1 = months[Mon]
    correct=correct+"/"+Mon1+"/"+str(StringData[4])
    return correct

Number = 0

def GetCover(mp3_file):
    global Number
    Number += 1
    audio = File(mp3_file)
    if 'APIC:' in audio:
        apic = audio.tags['APIC:'].data
        name = str(Number)+'cover.jpg'
        with open(name, 'wb') as f:
            f.write(apic)
        print('Album cover saved as album_cover.jpg')
    else:
        print('No album cover found')

ChronologicalOrder=[]

FolderLocation = 'G:\Music\My'

Folders = (os.listdir(FolderLocation))
Dates=[]
for folder in Folders:
    fullpath = FolderLocation + '\\' + folder
    CreationTime = os.path.getctime(fullpath)
    CreationTime = time.ctime(CreationTime)
    CreationTime = CreationTime.split()
    Dates.append([fullpath,StringToDate(CreationTime)])
ChronologicalOrder = sorted(Dates,key=lambda x: datetime.strptime(x[1], '%d/%m/%Y'))

del Dates
del Folders

for item in ChronologicalOrder:
    #print("\n"+item[0])
    #print(os.listdir(item[0])[2])
    filepath = item[0]+"\\"+os.listdir(item[0])[-1]
    
    GetCover(filepath)
    print(filepath+"\n")
    