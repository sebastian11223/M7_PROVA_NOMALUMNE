import pandas as pd
import matplotlib.pyplot as plt
arxiu = pd.read_csv("Martín Sebastia Casco Merino - Llistat.csv", usecols=['NOTES'])
nombres = pd.read_csv("Martín Sebastia Casco Merino - Llistat.csv", usecols=['NAME'])
names = nombres.groupby(by='NAME').mean()
notes = arxiu.groupby(by='NOTES').mean()
print(names)
print(notes)

#media
notas = pd.read_csv("Martín Sebastia Casco Merino - Llistat.csv", usecols=['NAME', 'NOTES'])

#def exer1():
#exercici 1
#print(notas)
#print(arxiu['NAMES'])
#media de las notas

#print(arxiu.loc[['NAME'],['NOTES'].mean()])
notatas = notas.groupby(by="NAME").mean()
plt.plot(notatas)
#plt.xlabel('names')
#plt.ylabel('notes')
plt.show()