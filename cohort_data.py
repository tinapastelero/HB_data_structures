def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """

    houses = set()

    student_list = open(filename)
    for line in student_list:
        student = line.split("|")
        student_house = student[2]
        houses.add(student_house)
        
    return houses

    student_list.close()

def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    #create empty lists to take names
    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    #open file
    student_list = open(filename)
    
    #for loop to iterate over student list
    for line in student_list:
        student_info = line.rstrip().split("|")
        student_name = student_info[0] + " " + student_info[1]

        #if statement to write student names to lists based on cohort
        if student_info[4] == "Winter 2015":
            winter_15.append(student_name)
        elif student_info[4] == "Spring 2015":
            spring_15.append(student_name)
        elif student_info[4] == "Summer 2015":
            summer_15.append(student_name)
        elif student_info[4] == "TA":
            tas.append(student_name)

    #sort cohort lists alphabetically by first name
    winter_15.sort()
    spring_15.sort()
    summer_15.sort()
    tas.sort()

    #add sorted lists to all_students list
    all_students = [winter_15,spring_15,summer_15,tas]

    student_list.close()

    return all_students



def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    #open file
    student_list = open(filename)
    
    #for loop to iterate over student list
    for line in student_list:
        student_info = line.rstrip().split("|")
        student_name = student_info[1]

        #if statement to write student names to lists based on cohort
        if student_info[2] == "Gryffindor":
            gryffindor.append(student_name)
        elif student_info[2] == "Hufflepuff":
            hufflepuff.append(student_name)
        elif student_info[2] == "Slytherin":
            slytherin.append(student_name)
        elif student_info[2] == "Dumbledore's Army":
            dumbledores_army.append(student_name)
        elif student_info[2] == "Order of the Phoenix":
            order_of_the_phoenix.append(student_name) 
        elif student_info[2] == "Ravenclaw":
            ravenclaw.append(student_name)           
        elif student_info[4] == "TA":
            tas.append(student_name)
        elif student_info[4] == "I":
            instructors.append(student_name)    

    #sort cohort lists alphabetically by first name
    gryffindor.sort()
    hufflepuff.sort()
    slytherin.sort()
    dumbledores_army.sort()
    order_of_the_phoenix.sort()
    ravenclaw.sort()
    tas.sort()
    instructors.sort()

    #add sorted lists to all_students list
    all_students = [gryffindor, hufflepuff, slytherin, dumbledores_army, order_of_the_phoenix, ravenclaw, tas, instructors]

    student_list.close()

    return all_students

def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of data student.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    #open file
    student_working_list = open(filename)
    
    #for loop to open file, convert each line to a list, and convert each list to a tuple
    for line in student_working_list:
        student_info = line.rstrip().split("|")
        student_name = student_info[0] + " " + student_info[1]
        student_info2 = []
        student_info2.append(student_name)
        student_info2.extend(student_info[2:])
        student_list.append(tuple(student_info2))    
    
    return student_list

print all_students_tuple_list('cohort_data.txt')


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
