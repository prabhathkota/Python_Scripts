class Person:   
    '''Represents a person.'''  
    count = 0   
  
    def __init__(self, name):   
        '''Initializing data.'''  
        self.name = name   
        print('\n Initializing %s' % self.name)   
  
        # To count the people   
        Person.count += 1   
  
    def displayName(self):   
        ''' Saying Hello'''  
        print('My name is %s.' % self.name)   
       
    def count_people(self):   
        '''Prints the count.'''  
        if Person.count == 1:   
            print('I am the only person here.')   
        else:   
            print('We have %d persons here.' % Person.count)   
  
Winston = Person('Winston Churchil')   
Winston.displayName()   
Winston.count_people()   
  
Abraham = Person('Abraham Lincoln')   
Abraham.displayName()   
Abraham.count_people()   
