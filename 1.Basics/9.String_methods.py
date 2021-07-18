course='Python for Beginners';
print(course.upper());
print(course.lower());
print(course.find('n'));
print(course.find('E'));#returns -1 if character not found
#searching the word
print(course.find("Beginners"));
#find and replace
print(course.replace("Beginners","Absolute beginners"));
#check character or set of characters existing
print('Python' in course);#return TRUE OR FALSE
