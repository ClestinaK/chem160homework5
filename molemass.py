names = ["H","C","N","O","P","S","K","F"]
mass = [1.0079, 12.0107, 14.0067, 15.9994, 30.9738, 32.0660, 39.0983, 18.9984]
Dict = {}
for i in range(len(names)):
   Dict[names[i]] = mass[i]

def molemass(mol):
    return(mol.count(names[0])*Dict[names[0]]) + (mol.count(names[1])*Dict[names[1]])+ (mol.count(names[2])*Dict[names[2]]) + (mol.count(names[3])*Dict[names[3]])+ (mol.count(names[4])*Dict[names[4]]) + (mol.count(names[5])*Dict[names[5]])+ (mol.count(names[6])*Dict[names[6]]) + (mol.count(names[7])*Dict[names[7]])