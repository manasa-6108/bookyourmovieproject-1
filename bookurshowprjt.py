
# write a program for bookyourmovie.com
#initilize value
#Enter the rows and seats taken from user end 
x = 10
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0
Row = int(input('Enter number of Row - \n'))
Seats = int(input('Enter number of seats in a Row - \n'))
Total_seat = Row*Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]      #using list comprehension to form  an matrix 
# create class function to define seat arrangement in a matrix form

class chart:

    @staticmethod
    def chart_maker():
        
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():
        percentage = (Booked_seat/Total_seat)*100
        return percentage
#object formed to call class name

class_call = chart
table_of_chart = class_call.chart_maker()
# using the nested loop to perform the different option

while x != 0:
    print('1 For Show the seats \n2 For Buy a Ticket \n3 For Statistics ',
          '\n4 For Show booked Tickets User Info \n0 for Exit')
    x = int(input())
    #select 1 to show the seats for rows and rows to be evaluated in the loop
    if x == 1:
        print('Cinema:')
        if Seats < 10:
            for seat in range(Seats):
                print(seat, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_chart.keys():
                print(int(num)+1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num)+1, end='  ')
                else:
                    print(int(num)+1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
                print()
        print('Available Seats = ', Total_seat - Booked_seat)
        print()
    #select 2 to choose the row number and column number and check the availability if seat is not reseved the book the ticket by giving yes
    #After selecting the seat, user detail to be entered
    elif x == 2:
        Row_number = int(input('Enter Row Number - \n'))
        Column_number = int(input('Enter Column Number - \n'))
        if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
            if table_of_chart[str(Row_number-1)][str(Column_number)] == 'S':
                if Row*Seats <= 60:
                    prize_of_ticket = 10
                elif Row_number <= int(Row/2):
                    prize_of_ticket = 10
                else:
                    prize_of_ticket = 8
                print('prize_of_ticket - ', '$', prize_of_ticket)
                conform = input('yes for booking and no for Stop booking - ')
                person_detail = {}
                if conform == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    person_detail['Ticket_prize'] = prize_of_ticket
                    table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
                    Booked_seat += 1
                    Total_Income += prize_of_ticket
                else:
                    continue
                Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat already booked by some one')
        else:
            print()
            
        print()
    #select 3 to display the statistics
    elif x == 3:
        print('Number of purchased Ticket - ', Booked_seat)
        print('Percentage - ', class_call.find_percentage())
        print('Current  Income - ', '$', prize_of_ticket)
        print('Total Income - ', '$', Total_Income)
        print()
    #select 4 to display the user detail for booked tickets
    elif x == 4:
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
            if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])
                print('Ticket Prize - ', '$', person['Ticket_prize'])
            else:
                print()
                print('---**---  Available seat  ---**---')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    else:
        print()
        print()
