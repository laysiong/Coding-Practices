import random

print("input name")

name = input('who is involve?\n')
name_list = name.split(sep=',')
random_pick = random.randrange(0,(len(name_list)-1))

clean_results = name_list[random_pick]
clean_results = clean_results.strip()
print(clean_results)