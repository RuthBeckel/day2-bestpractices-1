#!/usr/bin/env python


class DMammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant']
    
    def printMembers(self):
        print('Printing members of the dangerous Mammals class')
        for member in self.members:
            print('\t%s ' % member)

class DBirds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Eagle']
        
    def printMembers(self):
        print('Printing members of the dangerous Birds class')
        for member in self.members:
            print('\t%s ' % member)

class DFish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Shark']
        
    def printMembers(self):
        print('Printing members of the dangerous Fish class')
        for member in self.members:
            print('\t%s ' % member)