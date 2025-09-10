print('BIENVENUE SUR VOTRE BANQUE')

createname = input('Cree votre nom : ')
createmdp = input('Cree mdp : ')

print('Merci d avoire cree votre compte. ')

name = input("Entrez votre nom : ")

while name != createname:
     name = input("Faux ! Entrez votre nom : ")

     if name == createname:
        print("Merci")

mdp = input("Entrez votre MDP: ")

while mdp != createmdp:
     mdp = input("Faux ! Entrez votre MDP: ")

     if mdp == createmdp:
        print("Merci Bienvenue")

sold = 100


if sold != 0:
     print('vous avez ' + str(sold) )

yesno = input('Que voulez vous faire Envoyer(yes) Quitter(no) : ')

if yesno == 'no':
    print('aurevoir')
elif yesno == 'yes':
    envoie = int(input('choisisez le montant : vous avez ' + str(sold)  ))
else:
    print('erreur')

if envoie >= sold:
     print('vous avez pas assez')
elif envoie <= sold: 
     sold = sold - envoie
     print(sold)
else:
     print('erreur')

print('Il vous reste ' + str(sold)  )
        
