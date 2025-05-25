'''
    This file contains the class definition for the StrawHat class.
'''
from crewmate import CrewMate
import heap
import treasure
from custom import Node

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        self.m=m
        self.non_zero_load_crewmates=[]
        #contains all crewmate information
        all_crewmates=[]
        for i in range(m):
            crew=CrewMate()
            key=crew.load_assigned
            node=Node(key,crew)
            all_crewmates.append(node)
        self.load_heap=heap.Heap(heap.compare_size_node,all_crewmates)

        
    
            

        
        # Write your code here
        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        crewmate=self.load_heap.extract_full()#will give you the crewmate node with least load_assigned/completiontime
        if crewmate.value.load_assigned==0:
            treasure.set_priority()
            tnode=Node(treasure.priority,treasure)

            crewmate.value.load_assigned+=treasure.size+treasure.arrival_time
            crewmate.value.treasure_assigned.append(tnode)
            crewmate.key=treasure.size+treasure.arrival_time                #crewmate_key is essentially completion time
            node=Node(crewmate.key,crewmate.value)
            self.load_heap.insert(node)

            self.non_zero_load_crewmates.append(crewmate.value)#crewmate.value is a crewmate object

        else:
            treasure.set_priority()
            tnode=Node(treasure.priority,treasure)

            new_time=max(crewmate.value.load_assigned,treasure.arrival_time)+treasure.size
            crewmate.value.load_assigned=new_time
            crewmate.value.treasure_assigned.append(tnode)
            crewmate.key=new_time
            node=Node(crewmate.key,crewmate.value)
            self.load_heap.insert(node)

            
        
            
        
        

        
            
    
    def get_completion_time(self):
        '''Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures'''
        final_list=[]
        for crewmate in self.non_zero_load_crewmates:#crewmate is crewmate object with all its information
            prev_time=0
            treasure_heap=heap.Heap(heap.compare_priority_and_id,[])#treasure_assigned is a list with node object:key-priority of treasure, value:treasure
            for i in range(len(crewmate.treasure_assigned)):
        
                if i==0:
                    new_treasure=treasure.Treasure(crewmate.treasure_assigned[0].value.id,crewmate.treasure_assigned[0].value.size,crewmate.treasure_assigned[0].value.arrival_time)
                    new_treasure.set_priority()
                    prev_time=crewmate.treasure_assigned[0].value.arrival_time
                    node=Node(new_treasure.priority,new_treasure)

                    treasure_heap.insert(node)
                    #treasure_heap contains node object with key:priority,value:treasure object
                elif i!=0:
                    #prev_time=crewmate.treasure_assigned[i-1].value.arrival_time
                    treasure_in_processing=treasure_heap.extract_full()#i will extract priorobj, i will process it and then i will insert the new object in heap
                    curr_time=crewmate.treasure_assigned[i].value.arrival_time
                    time_diff=curr_time-prev_time
                    if time_diff>treasure_in_processing.value.size and treasure_in_processing.value.size>=0 and time_diff>=0:

                        while time_diff>0 and time_diff>treasure_in_processing.value.size and treasure_heap.array and treasure_in_processing.value.size>=0:
                            size1=treasure_in_processing.value.size
                            new_treasure6=treasure.Treasure(treasure_in_processing.value.id,0,treasure_in_processing.value.arrival_time)
                            new_treasure6.completion_time=prev_time+size1
                            #treasure_in_processing.value.completion_time=prev_time+treasure_in_processing.value.size
                            #treasure_in_processing.value.size=0# I MADE CHANGE
                            final_list.append(new_treasure6)
                            prev_time=prev_time+size1
                            time_diff=curr_time-prev_time
                            treasure_in_processing=treasure_heap.extract_full()

                        if time_diff==treasure_in_processing.value.size and treasure_in_processing.value.size>=0 and time_diff>=0:
                            new_treasure5=treasure.Treasure(treasure_in_processing.value.id,0,treasure_in_processing.value.arrival_time)
                        #treasure_in_processing.value.size=0#IS THIS ALLOWED
                            new_treasure5.completion_time=curr_time
                            final_list.append(new_treasure5)
                            #treasure_in_processing.value.size=0#IS THIS ALLOWED
                            #treasure_in_processing.value.completion_time=curr_time
                            #final_list.append(treasure_in_processing.value)
                            #time_diff=0
                            #prev_time=curr_time
            
                        else:#(the case when the size is greater than the remaining time difference)
                            
                            new_treasure1=treasure.Treasure(treasure_in_processing.value.id,treasure_in_processing.value.size,treasure_in_processing.value.arrival_time)

                            new_treasure1.size-=time_diff
                            new_treasure1.set_priority()
                            node1=Node(new_treasure1.priority,new_treasure1)
                            treasure_heap.insert(node1)
                            #prev_time=curr_time#IM ADDING THIS
                            


                    elif time_diff==treasure_in_processing.value.size and treasure_in_processing.value.size>=0 and time_diff>=0:
                        new_treasure4=treasure.Treasure(treasure_in_processing.value.id,0,treasure_in_processing.value.arrival_time)
                        #treasure_in_processing.value.size=0#IS THIS ALLOWED
                        new_treasure4.completion_time=curr_time
                        final_list.append(new_treasure4)
                        #prev_time=curr_time

                    else:#(the case when size is greater than the time difference, so the prev time becomes the current time)
                        new_treasure2=treasure.Treasure(treasure_in_processing.value.id,treasure_in_processing.value.size,treasure_in_processing.value.arrival_time)
                        new_treasure2.size-=time_diff
                        new_treasure2.set_priority()
                        node2=Node(new_treasure2.priority,new_treasure2)
                        treasure_heap.insert(node2)
                        #prev_time=curr_time#IM ADDING THIS
                    
                    new_treasure3=treasure.Treasure(crewmate.treasure_assigned[i].value.id,crewmate.treasure_assigned[i].value.size,crewmate.treasure_assigned[i].value.arrival_time)
                    new_treasure3.set_priority()
                    node3=Node(new_treasure3.priority,new_treasure3)
                    treasure_heap.insert(node3)
                    last_index=len(treasure_heap.array)-1
                    if treasure_heap.right_child(treasure_heap.parent(last_index))<=last_index:
                        try:
                            if not(heap.compare_priority_and_id(treasure_heap.array[treasure_heap.right_child(treasure_heap.parent(last_index))],treasure_heap.array[treasure_heap.left_child(last_index)])):
                                treasure_heap.swap(treasure_heap.array[treasure_heap.right_child(treasure_heap.parent(last_index))],treasure_heap.array[treasure_heap.left_child(last_index)])
                        except:
                            pass
                    prev_time=curr_time
            while len(treasure_heap.array) > 0:
                treasure_in_processing = treasure_heap.extract_full()
                if treasure_in_processing is not None:
                    x=treasure_in_processing.value.size
                    new_treasure7=treasure.Treasure(treasure_in_processing.value.id,treasure_in_processing.value.size,treasure_in_processing.value.arrival_time)
                    new_treasure7.completion_time = prev_time +x
                    final_list.append(new_treasure7)
                    prev_time += x
        final_list.sort(key=lambda treasure:treasure.id)
        return final_list
    
    
















            