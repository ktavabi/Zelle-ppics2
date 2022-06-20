"""Notebook script"""

# %% codecell
import math
from ast import literal_eval

def get_area_vol():
    """Calculate volume & surface area of sphere given the radius"""
    # volume = 4/3*pi*r**3'
    # srf area = 4pi*r**

    rad = literal_eval(input("Enter length of radius"))
    vol = 4/3 * math.pi * rad**3
    area = 4 * math.pi * rad**2
    return(rad, area, vol)

r, a, v = get_area_vol()

# [Multiline f-string](https://the-examples-book.com/book/python/printing-and-f-strings)
multiline_string = f"For circle with radius {r} units. "\
                   f"The volume is {v:.1f} cubic units, "\
                   f"and the area is {a:.1f} sq. units."
print(multiline_string)

# %% codecell
def price_pizza():
    """Calc cost per square inch of pie given diameter & price"""
    # get price & diameter vars
    # calculate area via get_area_vol
    # calc price per sq unit (inches) --> int

    diameter = literal_eval(input("Enter pie size(in)"))
    price = literal_eval(input("Enter price($xx.xx)"))
    area = 4 * math.pi * (diameter * 0.5)**2
    return price / area


ppsq = price_pizza()
print(f"Price per squre inch: {ppsq:.2f}")

# %% markdown
## bytecode
# Python source code is compiled into bytecode, the internal representation
# of a Python program in the CPython interpreter.
# The bytecode is also cached in .pyc files so that executing the same file
# is faster the second time (recompilation from source to bytecode can be
# avoided).
# This “intermediate language” is said to run on a virtual machine that
# executes the machine code corresponding to each bytecode.
# Do note that bytecodes are not expected to work between different Python
# virtual machines, nor to be stable between Python releases.

# %% codecell
def moleclular_weight():
    """Calculate molecular weight of hydrocarbon based on atomic numbers"""
    # grab n of each H, C, O atoms
    # compute sum of products

    n_H, n_C, n_O = literal_eval(input(
    "Enter numbers of Hydrogen, Carbon, and Oxygen atoms"))
    wts = {'H': 1.0079, 'C': 12.011, 'O': 15.9994}
    return n_H * wts['H'] + n_C * wts['C'] + n_O * wts['O']


print(f'The molecular weight of molecule is {moleclular_weight():.2f} grams/mole')

# %% codecell
def strike_distance():
    """Calculate distance to lightning strike from time between flash & sound"""
    # grab time
    # compute distance as product or rate and time
    # convert to miles

    time = literal_eval(input("Enter time(min) elapsed"))
    dist = 1100 * time * 60  # 1100ft/sec * X * sec
    return dist/5280  # feet to miles

print(f'Distance to lightning strike: {strike_distance():.2f} miles')
