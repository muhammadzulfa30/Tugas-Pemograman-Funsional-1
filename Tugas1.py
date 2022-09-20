print("Program Returning Function")
list_integer = [30, 20, 10]
print('sum_square',(list_integer))

def sum_squares (a, b, c):
    return(a**2 + b**2 + c**2)

print ('Hasil = ', sum_squares(30,20,10))

print ('\nprogram triangular')
def triangular(n):
    if n==1:
        return(1)
    else:
        return (n + triangular(n-1))
jumlah = triangular(4)
print("triangular ke-4 = ",jumlah)

print('\nprogram pangkat')
def pangkat(a):
    return(a**2)

print('pangkat (3,2)')
print("Hasil =", pangkat(-3)) 

def isPalindrome(s):
  s = s.lower()
  s = s.replace(" ","")
  return s == s[::-1]

#kata = (input("Input kata : "))
kata1 = "No lemon, no melon"
kata2 = "Madam, I’m Adam"
print (isPalindrome(kata1))
print (isPalindrome(kata2))