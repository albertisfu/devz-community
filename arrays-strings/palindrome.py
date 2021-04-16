
# Alberto Islas 
# Check if a string is palindrome


def normalize_string(string):
    #lowercase string and remove ","
    string = string.replace(" ", "").lower()
    string = string.replace(",", "").lower()
    return string

def is_palindrome(string):
    #check if is palindrome function

    #special characters to search  inside string
    special = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"}
    print("---------------")
    print("Test: ", string)
    string = normalize_string(string)

    #determine max range to traverse string, if string is even len(string)/2, if is odd len(string) round down integer
    if (len(string) % 2) == 0:
        max_range = len(string)/2
    else:
        max_range = round(len(string)/2) - 1

    max_range = int(max_range)
 
    for i in range(max_range):
        #access to string elements from right and left
        right = string[i]
        left = string[-i-1]

        try:
            #search for accented characters stored in "special" hash, if found replace with no accented character
            right = special[right]
            left = special[left]
        except KeyError:
            #if is not accented, keep same character
            right = right
            left = left
        
        #compare left character with their right equivalent character, if different break for and return False
        if right != left:
            return False
    
    return True


string = "La ruta nos aportó otro paso natural"
string1 = "Yo de todo te doy"
string2 = "A ti no, bonita"
string3 = "Ella te dará detalle"

string4 = "Esto no es palindromo"
string5 = "Esto tampoco es palindromo"


print(is_palindrome(string))
print(is_palindrome(string1))
print(is_palindrome(string2))
print(is_palindrome(string3))
print(is_palindrome(string4))
print(is_palindrome(string5))