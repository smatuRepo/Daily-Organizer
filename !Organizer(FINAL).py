"""
Simon Matusek
Oct. 30- Nov. 4
(FINAL VER.)
Event organizer
- calendar
- to-do list
- event list
"""

from time import strftime, sleep
import turtle


###CLASSES



class months:

    

    def __init__(self, number, year):
        """
        12 possibilities, initialize attributes
        April is weird
        """
		
        if number==1:
            self.name='January'
            self.holi_day=1  #new year's
            self.holi_name='new year\'s' #all names lowercase for sorting purposes
            self.n_days=31
            self.number=1
            self.leap=1
            self.grego=11
	    
        elif number==2:
            self.name='February'
            self.holi_day=14 #valentine's
            self.holi_name='valentine\'s day'
            if year % 4==0:
                self.n_days=29
            else:
                self.n_days=28
            self.number=2
            self.leap=1
            self.grego=12
		
        elif number==3:
            self.name='March'
            self.holi_day=17 #st patrick's day
            self.holi_name='st.patrick\'s day'
            self.n_days=31
            self.number=3
            self.grego=1
	    
        elif number==4:   
            self.name='April'
            self.holi_day=None  #easter, but no static date
            self.holi_name='easter' #1st sunday of month
            self.n_days=30
            self.number=4
            self.grego=2
	    
        elif number==5:
            self.name='May'
            self.holi_day=None
            self.holi_name='victoria day'
            self.n_days=31
            self.number=5
            self.grego=3
	    
        elif number==6:
            self.name='June'
            self.holi_day=None
            self.n_days=30
            self.number=6
            self.grego=4
	    
        elif number==7:
            self.name='July'
            self.holi_day=1  #canada day
            self.holi_name='canada day'
            self.n_days=31
            self.number=7
            self.grego=5
	    
        elif number==8:
            self.name='August'
            self.holi_day=None
            self.n_days=31
            self.number=8
            self.grego=6
	    
        elif number==9:
            self.name='September'
            self.holi_day=None #1st monday of month
            self.holi_name='labour day'
            self.n_days=30
            self.number=9
            self.grego=7
	    
        elif number==10:
            self.name='October'
            self.holi_day=31 #halloween
            self.holi_name='halloween'
            self.n_days=31
            self.number=10
            self.grego=8
	    
        elif number==11:
            self.name='November'
            self.holi_day=None
            self.n_days=30
            self.number=11
            self.grego=9
	    
        elif number==12:
            self.name='December'
            self.holi_day=25  #christmas
            self.holi_name='christmas'
            self.n_days=31
            self.number=12
            self.grego=10
			

       
		


		

class event:

    
	
    def __init__(self, year, Month, day, time, name, colour, size):
        '''
        color for place_dot on calendar
        '''
        self.year=year
        self.Month=Month
        self.day=day
        self.time=time
        self.name=name
        self.colour=colour   #for place_dot
        self.size=size       #same


        
    def __lt__(self,other):
        '''
        sort by attr's in this order:
        yr, mon, day, (colour), time, and name last
        color is so holidays always print
        UNDER user events
        '''
        return (self.year, self.Month.number, self.day, other.colour, self.time, self.name)<\
        (other.year, other.Month.number, other.day, self.colour, other.time, other.name)



    def place_dot(self, start_day, turt,dotsize): 
        """
        0-6 integer arg, where month starts
        places dot to indicate event(s)
        in that day
        """
        start_day-=1

		
        week=(self.day+start_day) // 7    # # of weeks
        d_o_w=(self.day+start_day) % 7    #whats left
		
        turt.setpos(100*d_o_w-300, 250-100*week) #(x,y)
        turt.dot(dotsize,self.colour)   
		






		
class to_do:
    

    def __init__(self, name, priority=3):
        """
        name/priority attributes
        if nothing entered to value, bottom priority
        """
        self.name=name
        self.priority=priority  #for sorting

        

    def __lt__(self,other):
        """
        sorts objects by priority first,
        then by name 
        """
        return (self.priority,self.name)<(other.priority, other.name)




class inpError(Exception):  #for valid_inp/_time
    pass

class tooLarge(Exception):  #for valid_time
    pass

class noZero(Exception):    #same as above
    pass











###DEFINITIONS:





def valid_inp(valid, prompt, error): 
    """
    valid=list, prompt=string,error=string
    list of valid inputs
    validates any string input
    returns input (string)
    """
    inp=''   #assign before referencing
    
    
    while True: 
        
        print(prompt,end=' ')
        
        try:
            inp=input() #check for input in list
            
            if not(inp in valid): raise inpError
            
            

            return inp # exit when input is an item from the list arg

        

        except inpError:   #custom error+message
            print(error)  







def valid_time():
    '''
    checks string input for
    proper format for time
    returns time (string)
    '''
    
    valid_hrs= range(0,24)
    valid_mins= range(0,60)  #what values are acceptable
    
	
    while True:
        

        try:
            time=input('What is the time? (24-hr time): ')
            
            if time[2] != ':': raise inpError
            #most helpful err. message IMO

            elif int(time[3:5])<10 and time[3] != '0': raise noZero
            #also should be checked first
            
            elif int(time[0:2])<10 and time[0] != '0': raise noZero
            #same as prev, but more likely to raise catch-all error
            
            elif not(int(time[0:2]) in valid_hrs): raise tooLarge
            #helpful, but more common knowledge
            
            elif not(int(time[3:5]) in valid_mins): raise tooLarge
            #same as prev.
            
            elif len(time) != 5: raise ValueError
            #catch-all for rest
            

	    
            return time #exit when evenrything is all right
        
        

        except ValueError:  #catch-all
            print('Please write time in the proper format, like \'01:03\'.')
            
        except tooLarge:
            print('One of the numbers is too large.')
            
        except noZero:
            print('Numbers less than 10 must be preceded by a \'0\'.')
            
        except inpError:    #for incorrect ':' placement
            print('The 3rd character must be a \':\'.')
            
        except IndexError:    #if not enough entered
            print(f'String is {5-len(time)} characters too short.')










def str_list(list_range):
    '''
    casts all values in a range to string
    returns modified argument
    '''
    
    list_range=list(list_range)   #range =/= list, must cast

	
    for i in range(len(list_range)):  #cant do just str(list_range)
        list_range[i]=str(list_range[i])
        

	
    return list_range
	











def todo_input(total):
    '''
    adds items to to-do list indefinitely
    total to-do list as arg
    returns modified argument (list)
    '''
    
    print('/MAIN/TO-DO/INPUT/') #menu location
    
    
    print('\t(Type \'0\' to stop entering.)')
    new_item=input('Input an item you need to do: ')  #anything input

    prio=str_list([1,2,3])  #for valid_inp
    

    while new_item != '0':
		
        item_prio=int(valid_inp(prio, 'How important is it? \n(1-3, 1 \
is most important.)', 'Not an integer between 1 and 3.'))
        

        todoitem=to_do(new_item, item_prio)  #__init__ instance
        
        total.append(todoitem) #initialize+add to_do instance to list
        print(f'Done! \'{todoitem.name}\' has been added.')
        new_item=input('Input an item you need to do: ')


        



    return total   #return modified list










def todo_delete(total):	
    '''
    user inputs item name,
    try to find name in list,
    delete (only) first instance in list
    total to-do list as arg
    returns modified argument (list)
    '''
    
    print('/MAIN/TO-DO/DELETE/')  #menu location
    
    if len(total)>0:  #if anything input
	
        target_item=input('\t(Type \'0\' to stop entering.)\nInput an item you need to delete: ')


        while target_item != '0':
            
            #target_item.lower()
            
            for i in total:
                
                if i.name.lower()==target_item.lower():
                    
                    print(f'Done! \'{i.name}\' has been deleted.')  #confirmation
                    total.remove(i)
                    
                    break
            
            else:
                print('That is not an item in the list.\nYou may \
have spelled it incorrectly.')

            if len(total)==0:
                print('There is nothing left to delete.')
                break

            target_item=input('Input an item you need to delete: ')


        
    else:
        print("There are no items to delete.")


        

    return total   #return modified list







def todo_output(total):
    """
    prints to do list
    in order of priority
    total to-do list as arg
    returns none
    """
    
    print('/MAIN/TO-DO/OUTPUT/')  #menu location
    
    if len(total)>0:
        
        total.sort()

        print('To-do list:')
        
        for i in total:  #all objects w/ indent
            try:
                char1=i.name[0].upper()  #to print with proper capitalization
                char_after=i.name[1:].lower()
            except IndexError: #for blank line name 
                char1=''
                char_after=''
            print(f'\t{total.index(i)+1}. {char1}{char_after}, level {i.priority} priority')
        
    else:
        print('There is nothing in the list.')







def todo_menu(total_todo):
    '''
    takes inputs,
    calls different procedures accordingly
    total to-do list as argument
    returns modified argument (list)
    '''
    
    print('/MAIN/TO-DO/')   #menu location
    
    decision=valid_inp(['B', 'D', 'I', 'O', 'b', 'd', 'i', 'o'], \
    'What would you like to do? \n(INPUT(i), DELETE(d), OUTPUT(o), BACK(b))'\
    , 'Please select a valid option.')


    while decision.lower() !='b':  #what def to call
	
        if decision.lower() =='i': 
            total_todo=todo_input(total_todo)
            total_todo=total_todo
            
        elif decision.lower() == 'd':
            total_todo=todo_delete(total_todo)
            total_todo=total_todo
            
        elif decision.lower() == 'o':  
            todo_output(total_todo)
            
            
        print('/MAIN/TO-DO/')
        
        decision=valid_inp(['B', 'D', 'I', 'O', 'b', 'd', 'i', 'o'],\
        'What would you like to do? \n(INPUT(i), DELETE(d), OUTPUT(o), BACK(b))'\
        , 'Please select a valid option.')


        


    return total_todo   #return modified list










def event_input(total):
    '''
    ask user for name/year/month/day/time of event
    add event objects to total list
    returns modified argument (list)
    '''
    
    print('/MAIN/EVENT/INPUT/')  #menu location
    
    
    valid_years=str_list(range(1970,2025)) 
    valid_months=str_list(range(1,13))  #for valid_inp
    	

    ev_name=input('\t(Type \'0\' to stop entering.)\nWhat is the event? ') #anything input
    

    
    while ev_name != '0':

        year= int(valid_inp(valid_years, 'What is the Year?',\
'That is not a year between 1970-2024.'))
        
        
        month=months(int(valid_inp(valid_months, 'What is the Month? \
(1(Jan)-12(Dec))', 'That is not a real month.')),year)
        
        

        valid_days=str_list(range(1,month.n_days+1)) #valid inputs for valid_inp,
                                                     #can only be declared after month
        

        days= f'What is the Day? (1-{month.n_days})'   #prompt for valid_inp
	
        ev_day=int(valid_inp(valid_days, days, 'Out of this month\'s range.'))
        
        
        time = valid_time()  #valid time string
        
	
        new_ev=event(year,month,ev_day,time,ev_name,'black',20) #__init__ event instance
        
        total.append(new_ev) #add to total events
        

        print(f'Done! {new_ev.name} at {new_ev.Month.name} {new_ev.day}, {new_ev.year} has been added.') 
	#confirmation of input
        
        
        ev_name=input('What is the event? ')


        
        


    return total  #return modified list


		

	
	
def event_delete(total):
    '''
    checks if any items in list,
    user inputs which item(title) to delete
    removes it
    returns modified argument (list)
    '''
    
    print('/MAIN/EVENT/DELETE/')

    
    if len(total)>0:

        print('(Type \'0\' to quit.)')
        del_inp=input('Input an item you need to delete: ')
    
        del_inp.lower()
	
        while del_inp != '0':
            
            for i in total:
                
                if i.name.lower()==del_inp:
                    print(f'Done! Event \'{i.name}\' at\
 {i.Month.name} {i.day}, {i.year} has been deleted.')
                    
                    total.remove(i)
                    
                    break
            else:
                print('That is not an event in the list.\nYou may \
have spelled it incorrectly.')

                
	
            if len(total)==0:  #other exit condition
                print('There is nothing left to delete.')
                break
            
            
            del_inp=input('Input an item you need to delete: ')

            
    else:
        print('There are no events to delete.')


        

    return total   #return modified list









def event_output(total):
    '''
    ask for month/yr to output
    sort list
    print events in month
    draw calendar
    put dots on calendar to show events
    returns none
    '''
    
    print('/MAIN/EVENT/OUTPUT/') #for menu

    
    
    if len(total) >0:
        
        total.sort() #for efficiency while checking

        valid_years=str_list(range(1970,2025)) #for valid_inp
        valid_months=str_list(range(1,13))
	
        events_year=[]  #declare before referencing
        events_month=[]
        
        weekdays=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
        #for calendar

        font1=('Courier', 15, 'italic')       #declare for .write - weekdays
        font2=('Comic Sans MS', 18, 'bold') #declare for .write - numbers
        font3=('Comic Sans MS', 40)         #declare for .write - title

        
            #finding events_month:
        while len(events_year) == 0: #only exit if events added
            
            
            year=int(valid_inp(valid_years,'In what year?', \
            'That’s not a year between 1970-2024.'))

		
            for i in total:
                
                if i.year==year:
                    events_year.append(i) #add events from yr in question
                    
                     
            if len(events_year)==0: #error message
                print('There are no events in that year.')
                
		

	
        while len(events_month) == 0: #exit if events added
            
            
            now_month=months(int(valid_inp(valid_months, 'What \
month? (1-12)', 'That is not a real month.')),year)
            

            for i in events_year: #check 1 attribute in list
                
                if i.Month.number==now_month.number:
                    events_month.append(i) #only add if in correct month+yr
                    

            if len(events_month) == 0: #error message
                print('There are no events in that month.')           
        


            #finding start_day:
        try:                        #same as if..else but 
            if now_month.leap==1:   #not all months have .leap attr
                yrexep=1    
        except AttributeError:  #else
            yrexep=0
            


            
        ###What Day of Week Month Starts In:
            
        gregyr = int(str(year)[2:])-yrexep  #gregorian year
        century = int(str(year)[0:2])
        
        #D.O.W. Formula:
        start_day = int(1+(2.6*now_month.grego-0.2)//1 - 2*century + gregyr+ \
        gregyr//4+century//4) %7 

        


        


        weeks = (now_month.n_days+start_day+1) // 7 +1 #for respective month


        
        #adding holiday event to list
        if now_month.holi_day != None:
            
            month_holi=event(year, now_month, now_month.holi_day, \
            '00:00', now_month.holi_name,'lime green',35) #time is so so green @ top
            
            events_month.append(month_holi)
            #print(month_holi.name)  #debugging
            
        elif now_month.number==4:  #april has event on 1st sunday
            
            month_holi=event(year, now_month, ((start_day+6)//7)*7-start_day+1,\
            '00:00', now_month.holi_name,'lime green',35) #time is so so green @ top
            
            events_month.append(month_holi)

        elif now_month.number==5: #may - event no mon. before 25th.
            month_holi=event(year, now_month, ((start_day+22)//7)*7-start_day+2,\
            '00:00', now_month.holi_name,'lime green',35) #time is so so green @ top
            
            events_month.append(month_holi)

        elif now_month.number==9: #sept. - event 1st mon.
            month_holi=event(year, now_month, ((start_day+6)//7)*7-start_day+2,\
            '00:00', now_month.holi_name,'lime green',35) #time is so so green @ top
            
            events_month.append(month_holi)


        #nothing to to with else statement

        events_month.sort()


        

            #TURTLE/CALENDAR START - declare screen to draw calendar
        window=turtle.Screen()  
        window.screensize(700,800)
        window.clear()

        dotter=turtle.RawTurtle(window)
	    
        dotter.pu() #set turtle attibutes
        dotter.speed(0)
        dotter.ht()
        
        grid=turtle.RawTurtle(window)  #turtle to draw grid
        grid.pensize(4)
        grid.pu() #same as penup()
        grid.ht() #same as hideturtle()
        grid.speed(0)

        label=turtle.RawTurtle(window) 
        label.speed=0  #set turtle + attr's
        label.ht()
        label.pu()
        
        
        label.color('medium blue') #color for weekdays

        
        
        

        for i in range(-350,351,100): #draw grid (horiz. lines) 7x6 grid
            grid.penup()
            grid.setpos(i,-300)
            grid.pendown()
            grid.setpos(i,300)
            
        for i in range(-300,301,100): #vert. lines
            grid.penup()
            grid.setpos(-350,i)
            grid.pendown()
            grid.setpos(350,i)






        for i in weekdays:
            label.setpos(weekdays.index(i)*100-300, 310)   #place+write days of week
            label.write(i, False, 'center', font1)
            

            

        label.color('crimson') #for title/date numbers
        label.setpos(0, 350)   #place+write title

        #title
        label.write(f'{now_month.name} {year}', False, 'center', font3)




        
            #Drawing calendar numbers
        for y in range(weeks):
            
            for x in range(7):
                date=y*7+x-start_day+1  #can be negative
                
                if date > 0 and date <= now_month.n_days:  #only if in range
                    
                    label.setpos(x*100-300, y*-100+270)   #put in place+write numbers
                    label.write(date,False,'center',font2)






            #printing list and placing dots:
        print(f'Events this {now_month.name}:')  #In Shell:
        
        
        for i in events_month:
            
            try:
                char1=i.name[0].upper() #so proper capitalization
                char_after=i.name[1:].lower()
                
            except IndexError: #for blank line name 
                char1,char_after='',''
                
            print(f'\t{i.Month.name} {i.day:02d} at{i.time:>6s}: {char1}{char_after}')
            
            i.place_dot(start_day,dotter,i.size)  #place all events on calendar (screen)
            

        sleep(2)    #give some time to read
                    #also, user may think it is broken b/c
                    #turtle window doesn't respond after
        
		
    else: #if no items in list
        print('there is nothing in the list')









def event_menu(total_event):
    '''
    takes inputs,
    calls different procedures accordingly
    total to-do list as arg
    returns modified argument (list)
    '''

    print('/MAIN/EVENT/')
    decision=valid_inp(['B','D','I','O','b','d','i','o'], 'What would you like to do?\
\n(INPUT(i), DELETE(d), OUTPUT(o), BACK(b))', 'Please select a valid option.')
    
    while decision.lower() !='b':
        
        
        if decision.lower() =='i':  
            total_event = event_input(total_event)
            total_event = total_event  #assign to itself so doesn't return NonType
            
        elif decision.lower() == 'd':
            total_event = event_delete(total_event)
            total_event = total_event
            
        elif decision.lower() == 'o':
            event_output(total_event)
            
            
        print('/MAIN/EVENT/')
        
        decision=valid_inp(['B','D','I','O','b','d','i','o'], 'What would you like to do?\
\n(INPUT(i), DELETE(d), OUTPUT(o), BACK(b))', 'Please select a valid option.')


        
	
    return total_event   #return modified list










###MAIN CODE


all_events=[] #must declare before referencing
all_todos=[]


#test=event(2000, months(4,2000), 21, '00:00', 'TEST', 'black',20)
#all_events.append(test)    #test case for easter



print('hello! Get organized today!',strftime("\nToday is \
%A, %B %d, %Y, %I:%M%p"))#today’s year, month, day of week, date, time


print('/MAIN/') #menu location


decision=valid_inp(['E','T','Q','e','t','q'], 'Where would you like to go? \n\
(TO-DO(t), EVENT(e), QUIT(q))', 'Please select a valid option.')


while decision.lower() !='q':
    
    
    if decision.lower() =='t': #to-do
        all_todos=todo_menu(all_todos)
        
    elif decision.lower() == 'e': #events
        all_events=event_menu(all_events)
        
        
    print('/MAIN/') #menu location
    
    decision=valid_inp(['E','T','Q','e','t','q'], 'Where would you like to go? \n(TO-DO(t), \
EVENT(e), QUIT(q))', 'Please select a valid option.')

turtle.bye()  #close turtle screen window automatically
print("--END--")
#EOF#
