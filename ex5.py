my_name = 'Joe YA'
my_age = 33 # not a lie
my_height = 175.555555 # cms
my_weight = 75 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s." % my_name)
print("He's %d cms tall." % round(my_height))
print("He's %d kgs heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (
        my_age, my_height, my_weight, my_age + my_height + my_weight))
