import re
def change_case(orig_string:str)->str:
    new_char=[]
    for char in orig_string:
        if char.isupper():
            new_char.append(char.lower())
        elif char.islower():
            new_char.append(char.upper())
    return "".join(new_char)

def split_in_half(orig_string:str)->tuple[str,str]:
    mid=len(orig_string)//2
    return orig_string[:mid],orig_string[mid:]

def remove_special_characters(orig_string:str)->str:
    return re.sub(r'[^a-zA-Z0-9]','',orig_string)

if __name__ == "__main__":
    print(change_case("HeLLllooo"))
    print(split_in_half("Helpp how are you doing pls follow and subscribe"))
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))
