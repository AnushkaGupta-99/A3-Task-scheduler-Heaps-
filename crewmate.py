'''
    Python file to implement the class CrewMate
'''

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        self.treasure_assigned=[]
        self.load_assigned=0
        # Write your code here
        pass
    
    # Add more methods if required
    def add_treasure_to_member(self,value):
        self.treasure_assigned.append(value)
        self.load_assigned+=value
        pass

    def set_load(self,load):
        self.load_assigned=load
