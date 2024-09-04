# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step] --> step: increase index by x
#


# indexing[]

school = "Asia Pacific College"

first_word = school[:4]
second_word = school[5:12]
by_2 = school[::2]
reversed_school = school[::-1]

print(first_word)
print(second_word)
print(by_2)
print(reversed_school)

# slicing(start, stop) --> useful for formatted strings such as URLS

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) # we start at index[0] for start and count up til the last slash, which is index[7]. For the stop, we count backwards, starting from
                    # the right most index which is [-1] up to the period which is index[-4]

print(website1[slice])
print(website2[slice])

# Bonus: Capitalize the website names

web1 = website1[slice]
web2 = website2[slice]

print(f"This is {web1.capitalize()}. And this is {web2.capitalize()}.")



