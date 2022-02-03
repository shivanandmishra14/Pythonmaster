available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]

print(available_parts)

# s[i] = x
# available_parts[3] = "music system"
# print(available_parts)

# s[i:j]= t
print(available_parts[3:])
available_parts[3:] = "Trackball"
print(available_parts)

available_parts[3:] = ["Trackball"]
print(available_parts)
