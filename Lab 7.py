
def main():

    person_info = {
        'name': 'Cole Tompsett',
        'student_id': 10261437,
        'pizza_toppings':[
                            'Pepperoni',
                            'Cheese',
                            'Sausage',
                        ],
        'movies':[
                    {'Title': 'Shrek',
                     'Genre': 'Family',
                    },
                    {'Title': 'Scooby Doo 2: Monsters Unleashed',
                     'Genre':'Mystery',
                    }
                ],
    }

    person_info['movies'].insert(1,{'Title': 'Deadpool','Genre':'Action'})

    new_toppings = ('Bacon','Olives','Mushrooms')
    topping_sort(person_info, new_toppings)

    new_toppings_V2 =('Chicken','Pineapple')
    topping_sort(person_info, new_toppings_V2)

    sentence(person_info)

    return

#Appends new pizza toppings and adds new toppings to the data structure
def topping_sort(person_info,new_toppings):

    for _ in new_toppings:
        person_info['pizza_toppings'].append(_)

    person_info['pizza_toppings'].sort()    
    
    return(person_info)

#prints a sentence describing the person
def sentence(person_info):
    count =1
    print("Hi Jeremy, my name is ", person_info['name'], " and my student ID is ", person_info['student_id'],".", sep ='')
    print("My ideal pizza has", end =" ")
    for _ in person_info['pizza_toppings']:
        
        if count== len(person_info['pizza_toppings']):
            print("and",_,sep=' ',end='.\n')
            count=0
        else:
            print( _ , end=", ")
            
        count+=1
    
    print("I like to watch ",end='')
    for m in person_info['movies']:

        if count== len(person_info['movies']):
            print("and", m['Genre'] ,sep=' ',end= ' movies.\n')
            count=0
            
        else:
            print(m['Genre'] , end=", ")
        count+=1
        
    print("Some of my favourites are",end=' ')
    for T in person_info['movies']:
        if count == len(person_info['movies']):
            print("and ", T['Title'],sep='',end='!')

        else:
            print(T['Title'],end=', ')
            count+=1

main()