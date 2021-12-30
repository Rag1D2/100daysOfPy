# Python Lists
us_states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine',
             'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

# Get the number of items in a list
print(len(us_states))

# Get a specific state from list
print(us_states[0])  # 0 is the first item in the list: "Delaware"
print(us_states[21])  # Alabama

# Can also use negative index (this causes python to count from the back end of the list)
print(us_states[-2])  # Alaska
print(us_states[-1])  # hawaii

# Can change items in a list
us_states[1] = "Pencilvania"
print(us_states[1])

# Add new item to END OF THE LIST
us_states.append("Mattyland")
print(us_states[-1])

# Extending a list takes a smaller list and adds ALL of the items to the original list
us_states.extend(["Ragsland", "Midgard", "Nirn"])
print(us_states[-1])
