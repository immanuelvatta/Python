from object import TV, Screen, Monitor, Ultra_wide_monitor
from room import Room


# s1 = Screen(20)

# print(s1.is_on)
# s1.toggle_state()
# print(s1.is_on)

immanuel_room = Room(1000, "My Room", "Bedroom")

my_items = [
Monitor(24, "OLED", "2nd monitor"),
Monitor(24, "OLED", "3rd monitor"),
Monitor(24, "OLED", "4th monitor"),
Ultra_wide_monitor(86, "OLED", "Massive Monitor")
]
print(immanuel_room.objects)
# immanuel_room.add_to_room(immanuel_second_screen)
# immanuel_room.add_to_room(immanuel_third_screen)
# immanuel_room.add_to_room(immanuel_fourth_screen)
immanuel_room.add_many_to_room(my_items)
print(immanuel_room.objects)

immanuel_room.objects[-1].toggle_state()
print(immanuel_room.objects[-1].is_on)

# tv1 = TV("Immanuel's TV", 200,85, "LED")

# print(tv1.type)

# print(tv1.is_on)
# tv1.toggle_state()
# print(tv1.is_on)

# r1 = Room (20,"Immanuel's Bedroom", "Bedroom")

# r2 = Room (10, "Hallway Closet", "Closet")
# print(r1)
# print(r2)

# r1.info()
# r2.info()