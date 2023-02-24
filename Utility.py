import re
from PreferenceLists import PreferenceLists

class Utility:

    def read_file(self, input_file):
            f = open(input_file, 'r')
            
            hospPrefLists = {}
            studentPrefLists = {}
            hospOpenSlots = {}
            
            numberOfHospitals = int(f.readline())
            numberOfStudents = int(f.readline())
            
            for hospital in range(1, numberOfHospitals + 1):
            
                splitLine = f.readline().split()
                intValues = list(map(int, splitLine))
                
                hospOpenSlots[hospital] = intValues[0]
                hospPrefLists[hospital] = intValues[1:]
        
            for student in range(1, numberOfStudents + 1):
            
                splitLine = f.readline().split()
                intValues = list(map(int, splitLine))
                
                studentPrefLists[student] = intValues

            return PreferenceLists(studentPrefLists, hospPrefLists, hospOpenSlots)
