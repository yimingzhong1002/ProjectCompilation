def matches_character(input_character: str, template_character: str) -> bool:
    """Return True if any of the following conditions are met (returns
    False otherwise)
        - input_charater and template_character are the same
        - template_character is '#' and input_character is a number
        - template_character is '&' and input_character is a letter
    matches_chracter("2", "#") -> True
    matches_chracter("b", "#") -> False
    matches_chracter("b", "&") -> True

    """
    if input_character.isdecimal():
        return (template_character == '#')
    elif input_character.isalpha():
        return (template_character == '&')
    else:
        return False
            

def matches_string(input_string: str, template_string: str) -> bool:
    """Return True if: for every position p from 0 to the length of the strings,
    one of the following conditions is met:
          - input_string[p] and template_string[p] are the same
          - template_string[p] is '#' and input_string[p] is a number
          - template_string[p] is '&' and input_string[p] is a letter
    matches_string("(437)972-7810", "(###)###-####") -> True
    matches_string("abc1234", "&&#####") -> False
    matches_string("123", "123") -> True
    matches_string("123", "456") -> False
    """
    if len(input_string) != len(template_string):
        return False
    for i in range(len(template_string)):
        if template_string[i] == "#":
            matches_character(input_string[i], template_string[i])
            continue
        elif template_string[i] == "&":
            matches_character(input_string[i], template_string[i])
            continue
        elif template_string[i] == input_string[i]:
            continue
    return True

    
        
def matches_repeated_character(input_string, template_character):
    #FOR Mastery of variables. Check whether input_string matches
    #1 or more repititions of template_character
    print("Need to implement this code (for mastery)")
    print("HINT: instead of returning True/False, try to the length of the repetition")
    print("e.g., 'ABC123' and '&' would return 3, and 'ABC123' and '#' would return 0")

def matches_repeated_string(input_string, template_string):
    #FOR Mastery of variables. Same idea as matches string, but now
    # can represent 1 or more numbers, and & can represent 1 or more letters
    # e.g., phone_template would be "(#)#-#" or e-mail template could be "&@&.&"
    print("Need to implement this code (for mastery)")


phone_template = "(###)###-####"
donor_id_template = "&&####"
time_template = "##:##&M"

#MAKE YOUR MENU HERE
result = matches_string("(248)434-5508", phone_template)
print("result should be true at this point: " + str(result))

result = matches_string("1-800-call-me", phone_template)
print("result should be false at this point: " + str(result))



