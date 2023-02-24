from Match import Match

class Solution:
    
    def __init__(self, m, n, hospital_list, student_list, hosp_open_slots):
        """
            The constructor exists only to initialize variables. You do not need to change it.
            :param m: The number of hospitals
            :param n: The number of students
            :param hospital_list: The preference list of hospitals, as a dictionary.
            :param student_list: The preference list of the students, as a dictionary.
            :param hosp_open_slots: Open slots of each hospital
            """
        self.m = m
        self.n = n
        self.hospital_list = hospital_list
        self.student_list = student_list
        self.hosp_open_slots = hosp_open_slots
        
    def preference(self, current, student, hospital):
        
        currenthospitalpref = self.student_list[student].index(current[student])
        hospitalprimepref = self.student_list[student].index(hospital)

        if hospitalprimepref < currenthospitalpref:
            return True
        else:
            return False    

    def get_matches(self):
        
        matchings = list()
        freehospital = list(self.hospital_list.keys())
        freestudent = list(self.student_list.keys())
        current = dict()
        openslots = self.hosp_open_slots

        #init current matchings dict
        for student in freestudent:
            current[student] = -1
  
        #while list of free hospitals isnt empty
        while freehospital:
            
            #grab an unpaired hospital
            hospital = freehospital[0]
            
            #find student from top of hospital pref list
            for student in self.hospital_list[hospital]:

                #if student is free
                if student in freestudent:

                    #set matching and remove student from free list
                    current[student] = hospital
                    freestudent.remove(student)

                    #decrement open slot
                    openslots[hospital] -= 1

                #check if all slots are full
                if openslots[hospital] == 0:
                    break
                
                else:

                    #check if an instability exists
                    if self.preference(current,student,hospital):

                        #swap hospitals that favors preferred hospital
                        freehospital.append(current[student])
                        openslots[current[student]] += 1
                        current[student] = hospital

                        #decrement open slot
                        openslots[hospital] -= 1
                        
                    #check if all slots are full
                    if openslots[hospital] == 0:
                        break                

            #pop matched hospital off            
            freehospital.pop(0)


        #create matchings from dict and output as list     
        for student in current:
            if current[student] > 0:
                matchings.append(Match(current[student],student))
                    
        return matchings


