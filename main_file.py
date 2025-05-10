
import re



text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet lectus non 
ligula pellentesque varius (254)113500084 id quis augue. Morbi at urna id massa sagittis porta. 
Quisque vitae 0723083003 metus at dolor porta euismod.+254706759269 Phasellus ullamcorper leo tristique 
quam suscipit, quis ultricies felis bibendum. Proin tincidunt diam vitae velit 
accumsan, in hendrerit sapien ultrices. 0718484575 Phasellus egestas dui vel dolor facilisis 
rhoncus. 
Mauris eleifend, felis eget tempus eleifend, dolor quam dictum arcu, eget 
hendrerit dui augue eget mauris. Nulla aliquam consequat quam, in auctor ante pulvinar ut.
"""

"""
+254113500084
0254706759269
0736244343
0723083003
(254)757820020

"""
# (?:\+254|0|\(254\) -- (?:...)
# \+254  - matches +254
# \(254\) - matches (254)
# 0254 matches 0254
# 0: local numbers start with zero
# \d{9,10} or \d{9}

# alternative pattern: r'(?:\+254|0|\(254\)|0254)\d{9}'
_phone_pattern = r'(?:\+254|0|\(254\)|0254)\d{9,10}'

# clean all phone numbers 

def get_standard_cell_numbers(phone: str):
    phone = phone.replace("(", "").replace(")", "")
    if phone.startswith("0"):
        return "+254" + phone[1:]
    elif phone.startswith("254"):
        return "+254" + phone[3:]
    elif phone.startswith("+254"):
        return phone
    elif phone.startswith("0254"):
        return "+254" + phone[4:]
    return phone

clean_cell_num = [get_standard_cell_numbers(m) for m in re.findall(_phone_pattern, text)]

# add to a text file 
with open("cell_numbers.txt", "w") as file:
    for number in clean_cell_num:
        file.write(number + "\n")
    
print("Numbers save to cell_numbers.txt")