def weight_on_planets():
   weight = float(input("What do you weigh on earth? ")) #changes input from a string to a float
   marsWeight = weight * 0.38 #converting to Mars weight
   jupiterWeight = weight * 2.34 #converting to Jupiter weight
   print("\nOn Mars you would weigh" , marsWeight , "pounds." + "\nOn Jupiter you would weigh" , jupiterWeight , "pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()
