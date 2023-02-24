import sys
from Utility import Utility
from Solution import Solution

class Driver:

    def __init__(self):
        if len(sys.argv) < 2:
            print("Please provide the testcase filepath as a command line argument")
            return
        input = Utility().read_file(sys.argv[1])
        s = Solution(len(input.hospital_preferences), len(input.student_preferences), input.hospital_preferences, input.student_preferences, input.hospital_open_slots)
        solution = s.get_matches()
        #print("Your Solution")
        #print("=============================================")
        print(solution)

Driver()
