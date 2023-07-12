import os
import time
from datetime import datetime, date
from mutagen import File

def StringToDate(StringData):
    correct=StringData[2]
    months = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
         'May': '05',
         'Jun': '06',
         'Jul': '07',
         'Aug': '08',
         'Sep': '09',
         'Oct': '10',
         'Nov': '11',
         'Dec': '12'
        }
    Mon1 = months[StringData[1]]
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

FolderLocation = 'G:\Music\My' #lowest directory level containing all the other folders

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

for item in ChronologicalOrder:
    filepath = item[0]+"\\"+os.listdir(item[0])[-1]
    GetCover(filepath)
    print(filepath+" Finished \n")
    