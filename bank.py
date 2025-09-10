import time

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
while sold != 1:
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
          time.sleep(1)
          print("1")
          time.sleep(1)
          print("2")
          time.sleep(1)
          print("3")
          print(sold)
     else:
          print('erreur')

     print('Il vous reste ' + str(sold)  )

print('Vous avez plus assez merci de vous reconnectez quand vous aurez assé !')
          

