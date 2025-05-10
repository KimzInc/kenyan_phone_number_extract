
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
# \d{9,10}

# alternative pattern: r'(?:\+254|0|\(254\)|0254)\d{9}'
_phone_pattern = r'(?:\+254|0|\(254\)|0254)\d{9,10}'

matches = re.findall(_phone_pattern, text)

# print(matches)

# clean all phone numbers 

def get_standard_cell_numbers(phone: str):
    phone = phone.replace("(", "").replace(")", "")
    if phone.startswith("0"):
        return "+254" + phone[1:]
