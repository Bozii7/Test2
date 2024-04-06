import pandas as pd

fajl = pd.read_csv('onlinefoods.csv')

najveca_vrijednost = fajl.iloc[:, 0].max()
najmanja_vrijednost = fajl.iloc[:, 0].min()

print("Najveća vrijednost u prvoj koloni:", najveca_vrijednost)
print("Najmanja vrijednost u prvoj koloni:", najmanja_vrijednost)

kolona = fajl.iloc[:, 0]
prosjek = kolona.mean()
print("Prosjeci po kolonama:", prosjek)

najveca_vrijednost1 = kolona.max()

apsolutna_razlika = abs(najveca_vrijednost - prosjek)
postotna_razlika = (apsolutna_razlika / prosjek) * 100

print("Najveća vrijednost:", najveca_vrijednost)
print("Postotna razlika između prosječne i najveće vrijednosti:", postotna_razlika)

kolona1 = fajl['Age']
min_vrijednost = kolona1.min()
max_vrijednost = kolona1.max()
kolona_normalizirana = (kolona1 - min_vrijednost) / (max_vrijednost - min_vrijednost)

fajl['Age'] = kolona_normalizirana

fajl.to_csv('onlinefoods.csv', index=False)


