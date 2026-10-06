import matplotlib.pyplot as plt
weights = (2.5,3.0,4.5,5.0,6.5,7.0,8.5,9.0)
height = (20,22,25,27,40,42,45,48)
labels = ("cat","cat","cat","cat","dog","dog","dog","dog")
for w,h,l in zip(weights,height,labels):
    print(w,'kg',h,'cm->',l)

def rule_based_classifier(weight,height):
    if weight < 5 and height < 30:
        return 'cat'
    else:
        return 'dog'

print(rule_based_classifier(4.5,25))
print(rule_based_classifier(7.0,42))

avg_weight_cat = (2.5+3.0+4.5+5.0)/4
avg_height_cat = (20+22+25+27)/4
avg_weight_dog = (6.5+7.0+8.0+9.5)/4
avg_height_dog = (40+42+45+48)/4

print("Average of cat is:", avg_height_cat, 'cm', avg_weight_cat, 'kg')
print("Average of dog is:", avg_height_dog, 'cm', avg_weight_dog, 'kg')

def ai_classifier(weight, height):
    dist_cat = abs(weight - avg_weight_cat) + abs(height - avg_height_cat)
    dist_dog = abs(weight - avg_weight_dog) + abs(height - avg_height_dog)
    if dist_cat < dist_dog:
        return 'cat'
    else:
        return 'dog'

new_animals = [(5.2,29),(6.8,33),(6.3,31)]
for w,h in new_animals:
    rule_pred = rule_based_classifier(w,h)
    ai_pred = ai_classifier(w,h)
    print(f"{w} kg, {h} cm-> rule says {rule_pred}, ai says {ai_pred}")

plt.figure(figsize = (6,5))
colors = ['orange' if l == 'cat' else 'steelblue' for l in labels]
plt.scatter(weights,height,c = colors, s = 80, label = 'training_data')
for w,h in new_animals:
    plt.scatter(w,h,c = 'red', marker = 'x', s = 100)

plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Cat vs Dog")
plt.show()