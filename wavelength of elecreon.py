import math

def wavelength():
    c = 3 * (10 ** 8)
    electron_rest_mass = 9.11 * (10 ** -31)  
    planck_constant = 6.626 * (10 ** -34)  
    electron_charge = 1.6 * (10 ** -19)  
    
    n1 = int(input("Enter the orbit number electron coming to = "))
    n2 = int(input("Enter the orbit number electron coming from = "))
    wavelength = (((n1 ** 2) * (n2 ** 2)) / ((n2 ** 2) - (n1 ** 2))) * 91.175

    if n1 == 1:
        series = "Lyman"
    elif n1 == 2:
        series = "Balmer"
    elif n1 == 3:
        series = "Paschen"
    elif n1 == 4:
        series = "Bracket"
    elif n1 == 5:
        series = "Pfund"
    elif n1 == 6:
        series = "Humphreys"
    else:
        series = "Unknown" 

    if wavelength < 380:
        color = "Ultraviolet"
    elif 380 <= wavelength < 450:
        color = "Violet"
    elif 450 <= wavelength < 475:
        color = "Blue"
    elif 475 <= wavelength < 495:
        color = "Cyan (Sky Blue)"
    elif 495 <= wavelength < 570:
        color = "Green"
    elif 570 <= wavelength < 590:
        color = "Yellow"
    elif 590 <= wavelength < 620:
        color = "Orange"
    elif 620 <= wavelength < 780:
        color = "Red"
    else:
        color = "Infrared"

    freq = (3 * (10 ** 8)) / (wavelength * (10 ** -9))
    energy = (freq * planck_constant) / electron_charge
    vel = math.sqrt((2 * energy * electron_charge) / electron_rest_mass)
    if vel < c:
        vel_factor = math.sqrt(1 - (vel / c) ** 2)
        mass = electron_rest_mass / vel_factor
    else:
        mass = float('inf')
    
    print(f'\n\nProperties of the electron: \n Wavelength = {wavelength:.2f} nm \n Frequency = {freq / 10 ** 12:.2f} THz \n Series = {series} \n Color/Type = {color} \n Energy = {energy:.2f} eV \n The velocity of an electron with such energy is = {vel / 1000:.2f} km/s (Relativistic mass in consideration) \n The relativistic mass will be = {mass:.5e} kg')

print("\n\nAttention: This program is APPLICABLE FOR BOHR MODEL ONLY. \nHappy Learning!!!!!")
wavelength()
