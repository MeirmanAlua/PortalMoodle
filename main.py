import json

class Student:
    def __init__(self, studentLogin, password):
        self.studentLogin = studentLogin
        self.password = password
        self.surname = ""
        self.bachelor = ""
        self.password = ""

    def login(self, studentLogin, password):
        opening = open('admin.json')
        data = json.load(opening)
        for student in data['accounts']['student']:
            if data['accounts']['student'][student]['login'] == studentLogin and data['accounts']['student'][student][
                'password'] == password:
                self.studentLogin = data['accounts']['student'][student]['login']
                self.password = data['accounts']['student'][student][
                    'password']
                self.surname = data['accounts']['student'][student]['surname']
                self.bachelor = data['accounts']['student'][student]['bachelor']
                self.password = data['accounts']['student'][student]['password']
                # if admin['login'] == login and admin['password'] == password:
                return True
        return print("wrong login or password")

    def printCourses(self):
        opening = open('admin.json')
        data = json.load(opening)
        counter = 1

        print()
        try:
            for course in data['courses']:
                for student in data['courses'][course]['students']:
                    if self.studentLogin == student['login']:
                        print("Course #" + str(counter) + " " + str(course))
                        counter += 1
        except TypeError:
            print("There are no courses")
        except ValueError:
            print("There are no courses")

        print()

    def printGrades(self):
        opening = open('admin.json')
        data = json.load(opening)

        try:
            decision = int(input("See all your marks or see specific subject mark (1 or 2): "))
        except ValueError:
            print("You must type a number (1 or 2) ! ")
        else:
            while decision < 0 or decision > 2:
                decision = int(input("Enter selection again: "))

            if decision == 1:
                opening = open('admin.json')
                data = json.load(opening)
                print()
                try:
                    for subject in data['accounts']['student'][self.studentLogin]['marks'].items():
                        print(subject)
                except ValueError:
                    print("No marks there")
                except TypeError:
                    print("No marks there")
                print()
            elif decision == 2:
                print()
                opening = open('admin.json')
                data = json.load(opening)

                print("Your subjects: ")
                try:
                    for subject in data['accounts']['student'][self.studentLogin]['marks']:
                        print(subject)
                except ValueError:
                    print("No subjects there")
                    return
                except TypeError:
                    print("No subjects there")
                    return
                print()


                subjectName = input("Input the subject: ")
                try:
                    print(data['accounts']['student'][self.studentLogin]['marks'][subjectName])
                except ValueError:
                    print("No mark(-s) there")
                    return
                except TypeError:
                    print("No mark(-s) there")
                    return
                print()

    def printTeachers(self):
        opening = open('admin.json')
        data = json.load(opening)

        counter = 1

        print("---------")
        try:
            for teacher in data['accounts']['teacher']:
                print("Teacher #" + str(counter) + " " + teacher)
                counter += 1
        except ValueError:
            print("There is an exception according to teacher(-s)")
            return
        except TypeError:
            print("There is an exception according to teacher(-s)")
            return
        print("---------")

    def enroll(self, subjectName):
        with open("admin.json") as jsonFile:
            jsonDecoded = json.load(jsonFile)

        isFound = False
        student = {}

        if len(jsonDecoded['courses'][subjectName]['students']) == 0:
            student = {'id': 1, 'surname': self.surname,
                       'login': self.studentLogin, 'password': self.password, 'bachelor': self.bachelor}
        else:
            student = {'id': jsonDecoded['courses'][subjectName]['students'][-1]['id'] + 1, 'surname': self.surname,
                       'login': self.studentLogin, 'password': self.password, 'bachelor': self.bachelor}

        try:
            for check in jsonDecoded['courses'][subjectName]['students']:
                if self.studentLogin == check['login']:
                    isFound = True
        except ValueError:
            print("There is an exception according to student's login")
            return
        except TypeError:
            print("There is an exception according to student's login")
            return

        if not isFound:
            with open("admin.json", "r+") as file:
                fileData = json.load(file)
                fileData['courses'][subjectName]['students'].append(student)
                file.seek(0)
                json.dump(fileData, file, indent=4)
        else:
            print("Student has already enrolled !")

    def unenroll(self, courseName):
        opening = open('admin.json')
        data = json.load(opening)

        try:
            for i in range(len(data['courses'][courseName]['students'])):
                if data['courses'][courseName]['students'][i]['login'] == self.studentLogin:
                    data['courses'][courseName]['students'].pop(i)
                    data.update()
                    json.dump(data, open("admin.json", "w"), indent=4)
                    break
        except ValueError:
            print("There is an exception according to student's login")
            return
        except TypeError:
            print("There is an exception according to student's login")
            return

        print()

    # def enrol(name, courses):
    #     opening = open('admin.json')
    #     data = json.load(opening)
    #     for student in data['accounts']['teacher']:
    #         if student['name'] == name:
    #             data['courses'][courses].update({'student': name})
    #         else:
    #             print("wrong login or password")

    def Interface(self, name):
        while 1:
            print("Welcome,", name)
            print("1. your courses:")
            print("2. enroll course")
            print("3. unenroll course")
            print("4. grades")
            print("5. teachers")
            print("6. exit ")
            try:
                selection = int(input("Enter selection (from 1 to 5): "))
            except ValueError:
                print("You must type a number and range is between 1 to 5 ! ")
            else:
                while selection < 0 or selection > 6:
                    selection = int(input("Enter selection again: "))

            if selection == 1:
                self.printCourses()
            elif selection == 2:
                subjectName = input("Enter the subject name: ")
                opening = open('admin.json')
                data = json.load(opening)

                if subjectName in data['courses']:
                    for login in data['courses'][subjectName]['students']:
                        if self.studentLogin == login['login']:
                            print("You have already enrolled to the course !")
                            starProgram()
                    self.enroll(subjectName)
                else:
                    print("This course is not in the system")

            elif selection == 3:
                subjectName = input("Enter the subject name: ")

                opening = open('admin.json')
                data = json.load(opening)

                try:
                    if subjectName in data['courses']:
                        for login in data['courses'][subjectName]['students']:
                            if self.studentLogin == login['login']:
                                self.unenroll(subjectName)
                    else:
                        print("This course is not in the system")
                except ValueError:
                    print("There is an exception according to subject")
                    return
                except TypeError:
                    print("There is an exception according to subject")
                    return
            elif selection == 4:
                self.printGrades()
            elif selection == 5:
                self.printTeachers()
            elif selection == 6:
                starProgram()


class Teacher:
    def __int__(self, key, teacherLogin, password):
        self.teacherLogin = teacherLogin
        self.password = password
        self.key = key

    def login(self, login, password):
        opening = open('admin.json')
        data = json.load(opening)
        for teacher in data['accounts']['teacher']:
            if data['accounts']['teacher'][teacher]['login'] == login and data['accounts']['teacher'][teacher][
                'password'] == password:
                self.teacherLogin = list(data['accounts']['teacher'].keys())[0]
                self.password = data['accounts']['teacher'][teacher]['password']
                self.key = data['accounts']['teacher'][teacher]['login']
                return True
        return print("wrong login or password")

    def printCourses(self):
        opening = open('admin.json')
        data = json.load(opening)

        counter = 1

        try:
            for course in data['accounts']['teacher'][self.teacherLogin]['courses']:
                print("Course №" + str(counter) + " " + str(course))
                counter += 1
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    def markStudent(self):
        with open("admin.json") as jsonFile:
            jsonDecoded = json.load(jsonFile)

        try:
            courseName = input("Enter the course name: ")
            studentLogin = input("Enter the student login: ")
            decision = int(input("How you want to mark the attendance? (1-present, 2-absent)"))
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return
        for course in jsonDecoded['courses']:
            if course == courseName:
                for student in jsonDecoded['courses'][courseName]['students']:
                    if studentLogin == student['login']:
                        if decision == 1:
                            student['mark'] = "present"
                            break
                        elif decision == 2:
                            student['absent'] = "absent"
                            break

        with open("admin.json", 'w') as jsonOutFile:
            json.dump(jsonDecoded, jsonOutFile, indent=4)

    def unenrollCourse(self):
        print("List of your courses you can enroll: ")
        self.printCourses()

        print()
        courseName = input("Enter the name of course you want to enroll: ")

        with open("admin.json") as jsonFile:
            jsonDecoded = json.load(jsonFile)

        print("List of students you are able to enroll: ")

        try:
            for student in jsonDecoded['courses'][courseName]['students']:
                print(student)
                print()
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

        try:
            studentId = int(input("Input the id of student you want to unenroll: "))
        except ValueError:
            print("There is an exception according to student id")
            return
        except TypeError:
            print("There is an exception according to student id")
            return

        opening = open('admin.json')
        data = json.load(opening)

        try:
            for i in range(len(data['courses'][courseName]['students'])):
                if data['courses'][courseName]['students'][i]['id'] == studentId:
                    data['courses'][courseName]['students'].pop(i)
                    data.update()
                    json.dump(data, open("admin.json", "w"), indent=4)
                    break
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    def enrollCourse(self):
        print("List of your courses you can enroll")
        self.printCourses()
        print()
        course = input("Enter the name of course you want to enroll")
        with open("admin.json") as jsonFile:
            jsonDecoded = json.load(jsonFile)

        print("List of students you are able to enroll: ")
        try:
            for student in jsonDecoded['accounts']['student']:
                print(student)
                print()
        except ValueError:
            print("There is an exception according to student(-s)")
            return
        except TypeError:
            print("There is an exception according to student(-s)")
            return

        try:
            name = input("Enter the name of student you want to enroll")
            student = jsonDecoded['accounts']['student'][name]
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

        isFound = False

        try:
            for check in jsonDecoded['courses'][course]['students']:
                if name == check['login']:
                    isFound = True
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

        if not isFound:
            with open("admin.json", "r+") as file:
                fileData = json.load(file)
                fileData['courses'][course]['students'].append(student)
                file.seek(0)
                json.dump(fileData, file, indent=4)
        else:
            print("Student has already enrolled !")

    def addGrade(self, courseName):
        with open("admin.json") as jsonFile:
            jsonDecoded = json.load(jsonFile)

        studentLogin = input("Enter the student login: ")

        try:
            for student in jsonDecoded['courses'][courseName]['students']:
                if student['login'] == studentLogin:
                    if "rate" not in student.keys():
                        rate = str(input("Enter the rate of the student " + str(student['login'] + " (from 0 to 10): ")))
                        student['rate'] = str(rate)
                        jsonDecoded['accounts']['student'][studentLogin]['marks'][courseName] = rate
                    else:
                        print("This student already has grade.")
                        break
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

        with open("admin.json", 'w') as jsonOutFile:
            json.dump(jsonDecoded, jsonOutFile, indent=4)

    def Interface(self, aty):
        while 1:
            print("Welcome,", aty)
            print("1. your courses:")
            print("2. mark student")
            print("3. unenroll course")
            print("4. enroll course")
            print("5. rate student")
            print("6. exit")
            try:
                selection = int(input("Enter selection (from 1 to 6): "))
            except ValueError:
                print("You must type a number and range is between 1 to 6 ! ")
            else:
                while selection < 0 or selection > 6:
                    selection = int(input("Enter selection again: "))

            if selection == 1:
                self.printCourses()
            elif selection == 2:
                print()
                self.markStudent()
            elif selection == 3:
                self.unenrollCourse()
            elif selection == 4:
                self.enrollCourse()
            elif selection == 5:
                courseName = input("Enter the course name: ")
                Teacher.addGrade(self, courseName)
            elif selection == 6:
                starProgram()


class Admin:
    def __int__(self, name, surname):
        self.name = name
        self.surname = surname

    def login(login, password):
        opening = open('admin.json')
        data = json.load(opening)
        for admin in data['accounts']['admin']:
            if admin['login'] == login and admin['password'] == password:
                return True
            else:
                print("wrong login or password")
        return False

    def add(role, person, surname, bachelor, login, password):
        opening = open('admin.json')
        data = json.load(opening)

        try:
            last_id = data["accounts"][role].keys()
            new_id = len(list(last_id)) + 1
            data["accounts"][role].update(
                {person: {"id": new_id, "surname": surname, "bachelor": bachelor, "login": login, "password": password,
                          "courses": []}})
            json.dump(data, open("admin.json", "w"), indent=3)
            print(f"new teacher is added to the database as")
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    def delete(role, person):
        opening = open('admin.json')
        data = json.load(opening)
        try:
            del data["accounts"][role][person]
            data.update()
            json.dump(data, open("admin.json", "w"), indent=3)
            print("Person is deleted")
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return
        # print(data["accounts"][role][person] + "is deleted")

    def update(role, person, new_name, surname, login, password, bachelor):
        opening = open('admin.json')
        data = json.load(opening)
        try:
            del data["accounts"][role][person]
            data.update()
            data["accounts"][role].update(
                {new_name: {"surname": surname, "bachelor": bachelor, "login": login, "password": password, "courses": []}})
            json.dump(data, open("admin.json", "w"), indent=3)
            print(f"teacher's data is changed")
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    def addCourse(name, san_student, teacher_amount):
        opening = open('admin.json')
        data = json.load(opening)
        try:
            last_id = data["courses"].keys()
            new_id = len(list(last_id)) + 1
            data['courses'].update(
                {name: {"id": new_id, "san_student": san_student, "teacher_amount": teacher_amount, "teachers": [],
                        "students": []}})
            json.dump(data, open("admin.json", "w"), indent=3)
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    def updateCourse(new_name, san_student, teacher_amount):
        opening = open('admin.json')
        data = json.load(opening)
        try:
            del data["courses"][new_name]
            data.update()
            data["courses"].update(
                {new_name: {"san_student": san_student, "teacher_amount": teacher_amount}})

            json.dump(data, open("admin.json", "w"), indent=4)
            print(f"course's data is changed")
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    def deleteCourse(name):
        opening = open('admin.json')
        data = json.load(opening)
        try:
            del data["courses"][name]
            data.update()
            json.dump(data, open("admin.json", "w"), indent=4)
            print("course is deleted")
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    def addTeacherToCourse(self):
        opening = open('admin.json')
        data = json.load(opening)
        try:
            courseName = input("Enter the course name: ")
            teacherName = input("Enter the teacher name: ")

            teacher = data['accounts']['teacher'][teacherName]

            with open("admin.json", "r+") as file:
                fileData = json.load(file)
                fileData['courses'][courseName]['teachers'].append(teacher)
                file.seek(0)
                json.dump(fileData, file, indent=4)

        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    def addStudentToCourse(courseName):
        opening = open('admin.json')
        data = json.load(opening)
        try:
            studentName = input("Enter the student name: ")

            student = data['accounts']['student'][studentName]

            with open("admin.json", "r+") as file:
                fileData = json.load(file)
                fileData['courses'][courseName]['students'].append(student)
                file.seek(0)
                json.dump(fileData, file, indent=4)
        except ValueError:
            print("There is an exception according to subject")
            return
        except TypeError:
            print("There is an exception according to subject")
            return

    # def addCourse(name, san_student):
    #     opening = open('admin.json')
    #     data = json.load(opening)
    #     last_id = data["courses"][name].keys()
    #     new_id = len(list(last_id)) + 1
    #     data["accounts"]['courses'].update(
    #         {name: {"id": new_id , "san_student": san_student, }})
    #     student_quantity = data["courses"][name]["students"].key()
    #     new_student = len(list(student_quantity)) +1
    #     if student_quantity > san_student:
    #         print("you cannot add the person since there is limited quantity of people")
    #     else: pass
    #     json.dump(data, open("admin.json", "w"), indent=3)
    #     data.close()
    #     print("new course is added")
    def Interface(aty, self=None):
        while 1:
            print("Welcome,", aty)
            print("1. adjust teacher's account (c/u/d/addtotthecourses)")
            print("2. adjust student's account (c/u/d/addtothecourses)")
            print("3. adjust courses (c/u/d)")
            print("4. exit")
            try:
                selection = int(input("Enter selection (from 1 to 4): "))
            except ValueError:
                print("You must type a number and range is between 1 to 4 ! ")
            else:
                while selection < 0 or selection > 4:
                    selection = int(input("Enter selection again: "))
            if selection == 1:
                print("there is adjustment field for teacher's account")
                print("1. add account")
                print("2. update account")
                print("3. delete account")
                print("4. add teachers to the courses")
                print("5. exit")
                try:
                    election = int(input("Enter selection (from 1 to 4): "))
                except ValueError:
                    print("You must type a number and range is between 1 to 4 ! ")
                else:
                    while election < 0 or election > 4:
                        election = int(input("Enter selection again: "))

                    if election == 1:
                        name = input("Enter the name of the teacher: ")
                        surname = (input("Enter the surname of the teacher: "))
                        bachelor = (input("Enter the bachelor of the teacher: "))
                        login = (input("create login:"))
                        password = (input("create password:"))
                        Admin.add("teacher", name, surname, bachelor, login, password)

                    elif election == 2:
                        name: str = input("Enter name:")
                        new_name: str = input("Enter new name:")
                        surname: str = input("Enter new surname:")
                        login: str = input("Enter new login:")
                        password: str = input("Enter the password:")
                        bachelor: str = input("Enter the bachelor:")
                        Admin.update("teacher", name, new_name, surname, login, password, bachelor)
                    elif election == 3:
                        name: str = input("Enter the name of the teacher to delete: ")
                        Admin.delete("teacher", name)
                    elif election == 4:
                        Admin.addTeacherToCourse(self)
                    elif election == 5:
                        starProgram()

            elif selection == 2:
                print("there is adjustment field for student's account")
                print("1. add account")
                print("2. update account")
                print("3. delete account")
                print("4. add students to the courses")
                print("5. exit")
                try:
                    election = int(input("Enter selection (from 1 to 4): "))
                except ValueError:
                    print("You must type a number and range is between 1 to 4 ! ")
                else:
                    while election < 0 or election > 4:
                        election = int(input("Enter selection again: "))
                    if election == 1:
                        name = input("Enter the name of the teacher: ")
                        surname = (input("Enter the surname of the teacher: "))
                        bachelor = (input("Enter the bachelor of the teacher: "))
                        login = (input("create login:"))
                        password = (input("create password:"))
                        Admin.add("student", name, surname, bachelor, login, password)
                    elif election == 2:
                        name: str = input("Enter name:")
                        new_name: str = input("aenter new name:")
                        surname: str = input("Enter new surname:")
                        login: str = input("Enter new login:")
                        password: str = input("Enter the password:")
                        bachelor: str = input("Enter the bachelor:")
                        Admin.update("student", name, new_name, surname, login, password, bachelor)
                    elif election == 3:
                        name: str = input("Enter the name of the teacher to delete: ")
                        Admin.delete("student", name)
                    elif election == 4:
                        opening = open('admin.json')
                        data = json.load(opening)

                        courseName = input("Enter the course name:")

                        if int(data['courses'][courseName]['san_student']) == len(
                                data['courses'][courseName]['students']):
                            print("There is maximum amount of students already !")
                        else:
                            Admin.addStudentToCourse(courseName)
                    elif election == 5:
                        starProgram()
            elif selection == 3:
                print("there is adjustment field for courses")
                print("1. add course")
                print("2. update course")
                print("3. delete course")
                print("4. attach teachers or students to the courses")
                print("5. exit")
                try:
                    election = int(input("Enter selection (from 1 to 5): "))
                except ValueError:
                    print("You must type a number and range is between 1 to 5 ! ")
                else:
                    while election < 0 or election > 5:
                        election = int(input("Enter selection again: "))
                    if election == 1:
                        name: str = input("Enter name of the course:")
                        san_student: str = input("Enter number of students:")
                        teacher_amount: str = input("Enter the number of teachers:")
                        Admin.addCourse(name, san_student, teacher_amount)
                    # Обновление курса
                    elif election == 2:
                        name: str = input("Enter name of the course:")
                        san_student: str = input("Enter number of students:")
                        teacher_amount: str = input("Enter the number of teachers:")
                        Admin.updateCourse(name, san_student, teacher_amount)
                    elif election == 3:
                        name: str = input("Enter name of the course:")
                        Admin.deleteCourse(name)

            elif selection == 4:
                exit()


def starProgram():
    choice = input("Choose a role: student(s) or admin(a) or teacher(t): ")[0]
    while choice[0] != 's' or choice[0] != 'a' or choice[0] != 't':
        if choice == 's':
            print("Approve your identity! ")
            username = input("Enter login: ")
            password = input("Enter password: ")

            student = Student(username, password)

            if student.login(username, password):
                print("you have approved your identity")
                name = input("Hello user, what's your name? ")
                student.Interface(name)
            else:
                print("You did not approve your identity...")
        elif choice == 'a':
            print("Approve your identity! ")
            username = input("Enter login: ")
            password = input("Enter password: ")
            if Admin.login(username, password):
                print("you have approved your identity")
                name = input("Hello user, what's your name? ")
                Admin.Interface(name)
            else:
                print("You did not approve your identity...")
        elif choice == 't':
            print("Approve your identity! ")
            username = input("Enter login: ")
            password = input("Enter password: ")

            teacher = Teacher()

            if teacher.login(username, password):
                print("you have approved your identity")
                name = input("Hello user, what's your name? ")
                teacher.Interface(name)
            else:
                print("You did not approve your identity...")
        choice = input("Choose a role: student(s) or admin(a) or teacher(t): ")[0]


starProgram()
