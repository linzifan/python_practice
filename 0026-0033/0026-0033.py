# coding: utf-8
# 0026
def triangular_sum(num):
    if num == 0:
        return 0
    else:
        return num + triangular_sum(num - 1)
print triangular_sum(10)

# 0027
def number_of_threes(num):
    if num < 10:
        return int(num == 3)
    else:
        return int(num % 10 == 3) + number_of_threes(num // 10)
print number_of_threes(34534)

# 0028
def is_member(my_list, elem):
    if my_list == []:
        return False
    else:
        if my_list[0] == elem:
            return True
        else:
            my_list.pop(0)
            return is_member(my_list, elem)
is_member(['c', 'a', 't'], 'z')

# 0029
def remove_x(my_string):
    if my_string == "":
        return ""
    else:
        if my_string[0] == "x":
            return remove_x(my_string[1:])
        else:
            return my_string[0] + remove_x(my_string[1:])
remove_x("catxxdogx")

# 0030
def insert_x(my_string):
    if len(my_string) == 1:
        return my_string
    else:
        return my_string[0] + "x" + insert_x(my_string[1:])
insert_x("catdog")

# 0031
def list_reverse(my_list):
    if my_list == []:
        return []
    else:
        last_elem = my_list.pop()
        return [last_elem] + list_reverse(my_list)
list_reverse([2, 3, 1])

# 0032
def gcd(num1, num2):
    if num1 > num2:
        maxi, mini = num1, num2
    else:
        maxi, mini = num2, num1
    if maxi % mini == 0:
        return mini
    else:
        return gcd(mini, maxi % mini)
gcd(30,25)
def gcd(num1, num2):
    if num2 > num1:
        return gcd(num2, num1)
    if num2 == 0:
        return num1
    else:
        return gcd(num1 - num2, num2)
gcd(30, 25)

# 0033
def slice(my_list, first, last):
    if my_list == []:
        return []
    else:
        first_elem = [my_list.pop(0)]
        if first > 0:
            return slice(my_list, first - 1, last - 1)
        elif last > 0:
            return first_elem + slice(my_list, first - 1, last - 1)
        else:
            return []
slice(['a', 'b', 'c', 'd', 'e'], 2, 4)       
def test_slice():
    """
    Some test cases for slice
    """
    print "Computed:", slice([], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 1), "Expected: [1]"
    print "Computed:", slice([1, 2, 3], 0, 3), "Expected: [1, 2, 3]"
    print "Computed:", slice([1, 2, 3], 1, 2), "Expected: [2]"
    
test_slice()
