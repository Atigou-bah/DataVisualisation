import numpy as np
import matplotlib.pyplot as plt


# Etape 1 : Génération de données : 
np.random.seed(42) # Pour rendre le random stable 
mois = np.array(['Jan','Fev', 'Mar','Avr','Mai','Juin','Juil','Août','Sept','Oct','Nov','Dec'])


tendance = np.linspace(1000,2000,12) # tendance de fond 
aleatoire = np.random.normal(0,150,12) # bruit aleatoire 

ventes = tendance + aleatoire 
ventes = np.round(ventes,2) # arrondir les nombres à deux chiffre apres la virgule 

print("**** LES VENTES ****")
for i in range(0,len(mois)): 
    print(f"{mois[i]} : {ventes[i]}")

print(f"Total annuel :{ventes.sum()}")

print(f"Moyenne annuelle : {ventes.mean()}")

print(f"Meilleur mois :  {mois[ventes.argmax()]}")
print(f"Pire mois :  {mois[ventes.argmin()]}")

plt.figure(figsize=(10, 5))

plt.subplot(1,2,1)
plt.plot(mois,ventes, marker="o", color='b')
plt.xlabel("Mois")
plt.ylabel("Ventes")
plt.title("Evolution des ventes du mois")
plt.grid(True)



plt.subplot(1,2,2)
plt.bar(mois,ventes,color="skyblue")
plt.xlabel("Mois")
plt.ylabel("Ventes")
plt.title("Ventes par mois")
plt.grid(True)
plt.savefig("Evolution.png", format="PNG")

plt.show()




 
