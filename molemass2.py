names = ["H","C","N","O","P","S","K","F"]
mass = [1.0079, 12.0107, 14.0067, 15.9994, 30.9738, 32.0660, 39.0983, 18.9984]
Dict = {}
for i in range(len(names)):
    Dict[names[i]] = mass[i]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def molemass2(mol):
    if  mol.isdigit() == True:
        return a[0]
    else:
        return (mol.count(names[0])*Dict[names[0]]) + (mol.count(names[1])*Dict[names[1]])+ (mol.count(names[2])*Dict[names[2]]) + (mol.count(names[3])*mass[3])+ (mol.count(names[4])*mass[4]) + (mol.count(names[5])*mass[5])+ (mol.count(names[6])*mass[6]) + (mol.count(names[7])*mass[7])+ (mol.count(names[1])*Dict[names[1]])+ (mol.count(names[2])*Dict[names[2]]) + (mol.count(names[3])*mass[3])+ (mol.count(names[4])*mass[4]) + (mol.count(names[5])*mass[5])+ (mol.count(names[6])*mass[6]) + (mol.count(names[7])*mass[7])