# demo1
# Tower Name Location
# Tokyo Skytree Japan
# Canton Tower China
# CN Tower Canada

tower = {
    "Tokyo Skytree": "Japan",
    "CN Tower": "Canada",
    "Canton Tower": "China",
}

# Let’s modify the dictionary:
# (a) Remove the entry whose location is "Canada"

# tower.pop('CN Tower')

tower_clone = tower.copy()
for key in tower_clone:
    if tower[key] == "Canada":
        tower.pop(key)

print(tower)



# (b) Add a new entry with tower name "Eiffel Tower" and
# location "Paris"
tower['Eiffel Tower'] = 'Paris'
print(tower)

# (c) Oops! Update the tower entry "Eiffel Tower" to have
# location "France"
tower['Eiffel Tower'] = 'France'
print(tower)

