# this program uses charge, mass, and n# alternating magnetic fields intto give V energy of a particle
import math

print('\n')

# might make mass equal to electron or proton equivelants
# would then be tied to charge (q)
print('Please enter particle type (electron = e and proton = p)') #or particle type? #e=1.6*10**-19
m = input()

qe = 1.602176634e-19
me = 9.1093837015e-31
mp = 9.1093837015e-31

if m =='e':
    q = qe
    m = me
    print('charge = −1.602176634x10^−19 C')
    print('mass = 9.1093837015x10^−31 Kg')
elif m == 'p': 
    q = qe
    m = mp
    print('charge = +1.602176634x10^−19 C')
    print('mass = 9.1093837015x10^−31 Kg') 
print('\n')

print('Now, enter a voltage potential of your first field? (must be greater than 0)')
Vo = input()

#math module functions
print('\n')

acc_1 = 2*q*float(Vo)/m

print("Your particle accelerated to (m/s): ", round(math.sqrt(acc_1),1))


#def eq_1(n):
    #math.sqrt(n*q*Vo/m)
#eq_1()


#print('Your particle accelerated to: ' + round(math.sqrt(acc_1),1)+ 'm/s')

#print("sqrt: ", math.sqrt(2*float(q)*float(Vo)/float(m)))




#print('Please enter starting field strength')
#E_s= input()

 
#v=0
#might make velocity lead/ other molecules after being heated in a cathode 
#print()

#KE=.5 * float(m)*float(v)**2
#print('Starting Kinetic Energy is '+ str(float(KE)) +' Joules')

#print()
#first acceleration


#print('Now, Enter the number of Electric Fields you want in your accelerator')
#E_n= input()
#print()
#print('Your accelerator has ' + str(int(E_n)) +' alternating Magnetic Fields')
#print()
#print('How strong should the first Magnetic Field be?')
#E_s= input()



