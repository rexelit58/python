# demonstrating performance improvement
import random
import time

names = ['sunny', 'bunny', 'chinny', 'vinny']
subjects = ['Python', 'Java', 'Blockchain']


def people_list(num):
    results = []
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choices(subjects)
        }
        results.append(person)
    return results


def people_generator(num):
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choices(subjects)
        }
    yield person


t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()
print('Time taken for list:', t2 - t1)

t1 = time.clock()
people = people_generator(1000000)
t2=time.clock()
print('Time taken for generator:', t2 - t1)

