##Description: Python code implementing Monte Carlo algorithm to calculate and plot the magnetization of two spins at increasing temperatures.
##Author: Jester Itliong
##Date: November 7, 2022

import numpy as np
import matplotlib.pyplot as plt 
import random

#Section 1 - Initialize everything
n = 2                    #number of spins
kb = 1                   #boltzmann constant set to 1
s = np.ones(n)           #array for the spins
J = 1                    #interaction parameter set to 1
steps = 500              #number of steps
Mag = []                 #array to store average magnetization per spin per step
E = []                   #array to store energies per step
Mag_per_T = []           #array to store average magnetization per spin per temperature over the steps
Tstart = 1               #Temperature loop indices
Tstop = 1000
Tstep = 100 

#Section 2 - Generate inital array of spins for n elements using loop and if statements
count1 = 0
i = 0
while count1<n:
  coin = random.random() #random number between 0 and 1
  if coin <.5:           #gives spin-up (+1) if generated number is less than 0.5
    s[i] = 1
  else:                  #gives spin-down (-1) if generated number is greater than or equal to 0.5
    s[i] = -1
  count1+=1
  i+=1
print(s)

#Section 3 - Set initial value of energy based on the Hamiltonian
energy = 0                                #initial value of energy set to 0
for i in range(n-1):
    energy = energy - J*(s[i]*s[i+1])     #Hamiltonian
print('Initial Spin Configuration: ', s)
print('Initial Energy E = ', energy )
m = np.mean(s)                            #initial value of magnetization per spin
print('Initial magnetization per spin M  = ', m )

#Section 4 - Implement Monte-Carlo Algorithm
current_energy = energy  #current/initial energy of the initial spin config
for T in (range(Tstart,Tstop,Tstep)):  #loop for temperature variations
  for i in (range(steps)):
    r_n = np.random.randint(n)         #generating integer random number
    si = s[r_n]                        #indexing spin location   
    sright = s[(r_n+1)%n]              #location of right spin
    sleft = s[(r_n-1)%n]               #location of left spin
    dE = 2*J*si*(sleft+sright)         #change in energy
    r = np.random.random()             #random number between 0 and 1
    if r < min(1, np.exp(-(dE)/(kb*T))):
      s[r_n] = -1*s[r_n]               #flip spins if condition is met
      current_energy += dE
    else:
      s[r_n] = s[r_n]                  #else do not flip spins

    ave_spins = np.abs(s.mean())       #average magnetization per spin per step

    E.append(current_energy)           #storing energy
    Mag.append(ave_spins)              #storing magnetization

  Mag_ave = np.mean(Mag)               #storing average magnetization per spin over the steps
  Mag_per_T.append(Mag_ave)            #storing average magnetization per spin per temperature over the steps
  print('At T = ', T, 'K, the Final Spin Configuration is', s, ' and the Average Magnetization over the time step is', Mag_ave)

#Section 5 - Plot the results
Tplot = np.arange(Tstart,Tstop,Tstep)
plt.title("<M> vs. T")
plt.xlabel("T (K)")
plt.ylabel("<M>")
plt.plot(Tplot,Mag_per_T, '-o')
plt.savefig("M_plot.pdf", dpi = 300)
