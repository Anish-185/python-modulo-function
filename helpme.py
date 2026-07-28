import re
def change_case(orig_string: str)->str:
    new_chars=[]
    for char in orig_string:
        if char.islower():
            new_chars.append(char.upper())
        elif char.isupper():
            new_chars.append(char.lower())
    return " ".join(new_chars)

def split_in_half(orig_string :str)->tuple[str,str]:
    mid=len(orig_string)//2
    return orig_string[:mid],orig_string[mid:]

def remove_special_charecters(orig_string:str)->str:
    return re.sub(r'[^a-zA-Z0-9]','',orig_string)
if __name__=="__main__":
    print(change_case("Hello"))
    print(split_in_half("hellothere how are you"))
    print(remove_special_charecters("hello ! How are @ you & there *"))
