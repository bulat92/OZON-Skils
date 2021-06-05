import glob
import pickle

for name in glob.glob('*.dat'): #с помощью glob.glob('*.dat') получаем названия всех файлов с расширением .dat
    file = open(name, 'rb') #открываем их по очереди
    print(pickle.load(file))# загружаем выводим
    file.close()
