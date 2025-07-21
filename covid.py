import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('vaccination.csv',sep=';')
#print(df.columns.tolist())
#print(df.head())

df['jour'] = pd.to_datetime(df['jour'])

df_simple = df[['jour','n_dose1_h','n_complet_h','n_rappel_h']]
df_simple = df_simple.sort_values('jour')

#print(df_simple.head(25))
## Gerer les valeurs NaN
df_simple = df_simple.fillna(0)

plt.figure(figsize=(20,26))
plt.subplot(1,2,1)
plt.plot(df_simple['jour'], df_simple['n_dose1_h'], label='DOSE 1 ')
plt.plot(df_simple['jour'], df_simple['n_complet_h'], label='COMPLET ')
plt.plot(df_simple['jour'], df_simple['n_rappel_h'], label='RAPPEL ')

plt.xlabel('Date')
plt.ylabel('Dose/complet/rappel')
plt.title('Evolution de la couverture vaccinale du COVID-19 en france')
plt.legend(loc='upper left')
plt.grid(True)

## Vitesse de progression 
## 1. Lisage des données 
df_journalier = df_simple.groupby('jour').sum().reset_index()
df_journalier['dose1_moyenne_7j'] = df_journalier['n_dose1_h'].rolling(window=7).mean()

##print(df_journalier.head(25))

## Calcul de la progession 
df_simple['Progression journaliere'] = df_simple['n_dose1_h'].diff()

print(df_simple.head())

ax1 = plt.subplot(1,2,2)
# Ax1  Y gauche progression journalière 
color = 'tab:purple'
plt.gcf().autofmt_xdate()
ax1.plot(df_simple['jour'],df_simple['Progression journaliere'], color=color)
ax1.set_xlabel("Date")
ax1.set_ylabel("Progression journalière")
ax1.tick_params(axis='y', labelcolor=color)

# ax2 Y droite 
ax2 = ax1.twinx()
color = 'tab:red'
df_simple['Cumul_dose1'] = df_simple['n_dose1_h'].cumsum()
ax2.plot(df_simple['jour'], df_simple['Cumul_dose1'], color=color)
ax2.set_ylabel('Cumul dose 1', color=color)
ax2.tick_params(axis='y', labelcolor=color)


plt.title('Progression et cumul des vaccinations')
plt.gcf().autofmt_xdate()

plt.tight_layout()
# Exporter les données vers un nouveau CSV
df_simple.to_csv('vaccination_analyse.csv', sep=';', index=False)

print("Fichier CSV 'vaccination_analyse.csv' exporté avec succès.")


plt.savefig("Vaccination_covid.png", format="PNG")
plt.show()

