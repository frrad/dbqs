import random


def name():
    first = ['Sarah', 'Sam', 'Jimmy', 'Johnny',
             'Wanda', 'Wendy', 'Larry', 'Lumpy',
             'Stephanie', 'Fred', 'David']
    last = ['Smith', 'Jones', 'Peters', 'Stein',
            'Sandwich', 'Cooper', 'Fletcher',
            'Oh', 'Robinson', 'Staub']

    a, b = random.randrange(len(first)), random.randrange(len(last))
    return first[a] + ' ' + last[b]


def department():
    departments = ['HR', 'Taxidermy', 'Baking', 'Databases',
                   'Data Science']

    a = random.randrange(len(departments))
    return departments[a]


def salary():
    return str(random.randint(50000, 150000))


def date():
    y = random.randint(1999, 2018)
    m = random.randint(1, 12)
    d = random.randint(1, 28)
    return "%d-%02d-%02d" % (y, m, d)


def row(i):
    return "%d,%s,%s,%s,%s" % (i, name(), salary(), department(), date())


random.seed(0)
# print 'idnumber,name,salary,department,join_date'
for i in xrange(1, 10000):
    print row(i)
