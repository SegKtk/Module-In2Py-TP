segla = {'C':[20,20,20], 'PYTHON':[20,18,20], 'UML':[15,18,19], 'WEB':[15,20,19], 'SE':[15,16,14], 'ALGEBRE':[16,16,16], 'PROBA':[18,16,14] }
moyenneCours = {'C':(segla['C'][0]+segla['C'][1]+segla['C'][2])/3, 'PYTHON':(segla['PYTHON'][0]+segla['PYTHON'][1]+segla['PYTHON'][2])/3, 'UML':(segla['UML'][0]+segla['UML'][1]+segla['UML'][2])/3, 'WEB':(segla['WEB'][0]+segla['WEB'][1] + segla['WEB'][2])/3, 'SE':(segla['SE'][0] + segla['SE'][1]+segla['SE'][2])/3, 'ALGEBRE':(segla['ALGEBRE'][0]+segla['ALGEBRE'][1]+segla['ALGEBRE'][2])/3, 'PROBA':(segla['PROBA'][0]+segla['PROBA'][1]+segla['PROBA'][2])/3}
moyenneGene = (moyenneCours['C']+moyenneCours['PYTHON']+moyenneCours['UML']+moyenneCours['WEB']+moyenneCours['SE']+moyenneCours['ALGEBRE']+moyenneCours['PROBA'])/len(segla)

print("Ta moyenne est : " + str(moyenneGene))


#--------------E0


L = list(range(1,11))#creation de la liste L
#ajouter la valeur 11 a chaque element de la liste
L[0] += 11
L[1] += 11
L[2] += 11
L[3] += 11
L[4] += 11
L[5] += 11
L[6] += 11
L[7] += 11
L[8] += 11
L[9] += 11

#ajouter 22 a la fin de la liste
L.append(22)

#ajouter simultanement les valeurs 23 et 24 a la fin de la liste
L.extend([23,24])

#extraire deux sous-listes L1 et L2. L1 contenant le paires et L2 les impaires

L1 = L[0: : 2]
L2 = L[1: : 2]
print('L1 ===> ' + str(list(L1)) + ' et L2 ===> '+ str(list(L2)))

#Supprimer l'entree d'indice 3

del L[3]
print('\nAprès suppresion L = ' + str(list(L)) )

#--------------E1


d = {'nom':'Dupuis', 'prenom':'Jacque', 'age':30}
#coriger l'erreur dans le prénom
d['prenom'] = 'Jacques'

#afficher la liste des clés du dictionnaire
print(d.keys())
print('\t')

#afficher la liste des valeurs du dictionnaire
print(d.values())
print('\t')

#afficher la liste des paires clé-valeur du dictionnaire
print(d)
print('\t')

#ecrire la phrase 

print(d['prenom'] + ' ' + d['nom'] + ' a ' + str(d['age']) + ' ans')