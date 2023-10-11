def ran_check(num, low, high):
    if num>=low and num<=high:
        return f"{num} is in the range between {low} and {high}"
    else:
        return f"{num} is not in the range between {low} and {high}"

print(ran_check(1, 1, 5))
# For Boolean
def ran_check(num, low, high):
    return num in range(low, high+1)

print(ran_check(1, 1, 5))