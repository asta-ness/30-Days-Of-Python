emty_tuple =()
emty_tuple = tuple()
emty_tuple_1 = tuple()
sisters_tpl = ('Ona', 'Marijona')
brothers_tpl =('Petras', 'Antanas')

family_tpl = sisters_tpl+brothers_tpl
print(family_tpl)
print(len(family_tpl))
family_members = list(family_tpl)
family_members.append('Barbora')
family_members.append('Marijonas')
family_tpl = tuple(family_members)
print(family_tpl)
family_members = tuple(family_tpl)
print(family_members)

#unpacking
(father, mather, *siblings) = family_members
print(father)
print(mather)
print(siblings)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('carrots', 'potatoes')
animal = ('chicken', 'lamb')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
#ood_stuff_tp = list(food_stuff_tp)
#prfint(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list

slicing_items_from_food_stuff_tp = food_stuff_tp[3:5]
print((slicing_items_from_food_stuff_tp))

food_stuff_tp = list(food_stuff_tp)
slice_out_from_list = food_stuff_tp[0:2]
slice_out_from_list_1 = slice_out_from_list[:-1]
print(slice_out_from_list)

del food_stuff_tp
#print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)