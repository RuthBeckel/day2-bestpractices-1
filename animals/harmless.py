#!/usr/bin/env python


class HMammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Wild Cat']
    
    def printMembers(self):
        print('Printing members of the harmless Mammals class')
        for member in self.members:
            print('\t%s ' % member)

class HBirds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
        
    def printMembers(self):
        print('Printing members of the harmless Birds class')
        for member in self.members:
            print('\t%s ' % member)

class HFish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Salmon', 'Herring']
        
    def printMembers(self):
        print('Printing members of the harmless Fish class')
        for member in self.members:
            print('\t%s ' % member)