def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration, activity_duration

    global last_finished # Tracks the timestamp (in minutes) of when the last activity was finished.
    global last_finished2
    global bored_with_stars

    global cur_state
    global cur_star
    global cur_star_activity
    global take_star

    cur_hedons = 0
    cur_health = 0

    cur_state = "not tired"
    last_active_time = 0

    cur_star = None
    cur_star_activity = None
    take_star = False

    global star1_time, star_counter

    star1_time = 0
    star_counter = 0

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0
    activity_duration = 0

    cur_time = 0

    last_finished = -1000
    last_finished2 = -10000

def perform_activity(activity, duration):
    global cur_health
    global cur_hedons
    global last_activity, last_activity_duration, activity_duration
    global last_finished, last_finished2
    global bored_with_stars
    global cur_state
    global cur_time
    global cur_star, cur_star_activity
    global star1_time

    activity_duration = duration

    cur_time = cur_time + duration

    get_cur_state()

    star_can_be_taken(activity)

  # running:

    if last_activity == activity:
        total_duration = duration + last_activity_duration
    else:
        total_duration = duration

    if activity == "running":
        #print('cur_state:', cur_state)
        #print('take_star:', take_star)

      # health points, running:
        if total_duration <= 180:   # less than 3 hours
            cur_health = cur_health + (3 * duration)
        elif duration > 180:
            cur_health = cur_health + (180 * 3) + (1 * (duration - 180))
        elif total_duration > 180:
            if total_duration - duration <= 180:
                cur_health = cur_health + ((180 - last_activity_duration) * 3)
                cur_health = cur_health + ((total_duration - 180) * 1)
            if total_duration - duration > 180:
                cur_health = cur_health + (1 * duration)
      # hedons, running:
        if cur_state == "not tired":
            if duration <= 10:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (2 * duration) + (3 * duration)
                    elif bored_with_stars == True:
                        cur_hedons = cur_hedons + (2 * duration)
                if take_star == False:
                    cur_hedons = cur_hedons + (2 * duration)
            elif duration > 10:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (2 * 10) + (3 * 10) + (-2 * (duration - 10))
                    elif bored_with_stars == True:
                        cur_hedons = cur_hedons + (2 * 10) + (-2 * (duration - 10))
                if take_star == False:
                    cur_hedons = cur_hedons + (2 * 10) + (-2 * (duration - 10))

        elif cur_state == "tired":

            #print('duration:', duration)
            if duration <= 10:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (-2 * duration) + (3 * duration)
                    elif bored_with_stars == True:
                        cur_hedons = cur_hedons + (-2 * duration)
                if take_star == False:
                    cur_hedons = cur_hedons + (-2 * duration)
            elif duration > 10:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (-2 * duration) + (3 * 10)
                    elif bored_with_stars == True:
                        cur_hedons = cur_hedons + (-2 * duration)
                if take_star == False:
                    #print('duration:', duration)
                    #print('2 * duration:', 2 * duration)
                    #print('cur_hedons before:', cur_hedons)
                    cur_hedons = cur_hedons - (2 * duration)
                    #print('cur_hedons after:', cur_hedons)
    #__________________________________________________________________________________________________________________________
    # carrying textbooks

    if activity == "textbooks":
        #health points , textbooks
        cur_health = cur_health + (2 * duration)

        #hedons , textbooks
        if cur_state == "not tired":
            if duration <= 10:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (1 * duration) + (3 * duration)
                    if bored_with_stars == True:
                        cur_hedons = cur_hedons + (1 * duration)
                elif take_star == False:
                    cur_hedons = cur_hedons + (1 * duration)
            if  10 < duration <= 20:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (1 * duration) + (3 * 10)
                    elif bored_with_stars == True:
                        cur_hedons = cur_hedons + (1 * duration)
                elif take_star == False:
                    cur_hedons = cur_hedons + (1 * duration)
            if duration > 20:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (1 * 20) + (-1 * (duration- 20)) + (3 * 10)
                    elif bored_with_stars == True:
                        cur_hedons = cur_hedons + (1 * 20) + (-1 * (duration - 20))
                elif take_star == False:
                    cur_hedons = cur_hedons + (1 * 20) + (-1 * (duration - 20))

        elif cur_state == "tired":
            if duration <= 10:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (-2 * duration) + (3 * duration)
                    elif bored_with_stars == True:
                        cur_hedons = cur_hedons + (-2 * duration)
                elif take_star == False:
                    cur_hedons = cur_hedons + (-2 * duration)
            if  10 < duration <= 20:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (-2 * duration) + (3 * 10)
                    elif bored_with_stars == True:
                        cur_hedons = cur_hedons + (-2 * duration)
                elif take_star == False:
                    cur_hedons = cur_hedons + (-2 * duration)
            if duration > 20:
                if take_star == True:
                    if bored_with_stars == False:
                        cur_hedons = cur_hedons + (-2 * duration) + (3 * 10)
                    if bored_with_stars == True:
                        cur_hedons = cur_hedons + (-2 * duration)
                elif take_star == False:
                    cur_hedons = cur_hedons + (-2 * duration)

    #________________________________________________________________________________________________________________
    # resting:

    if activity == "resting":
        cur_health = cur_health + (0 * duration)
        cur_hedons = cur_hedons + (0 * duration)

    #_____________________________________________________________________________________________________________
    last_activity = activity

    last_activity_duration = total_duration

    last_finished2 = last_finished

    last_finished = cur_time

def get_cur_hedons():
    return cur_hedons

def get_cur_health():
    return cur_health

def offer_star(activity):
    global cur_health
    global cur_hedons
    global last_activity, last_activity_duration, last_activity_duration
    global last_finished
    global bored_with_stars
    global cur_state
    global cur_time
    global cur_star, cur_star_activity
    global star1_time, star_counter

    cur_star = True
    cur_star_activity = activity

    star1_time = cur_time - activity_duration

    if cur_time - star1_time > 120:
        star_counter = 0

    if cur_time - star1_time < 120:
        star_counter += 1

    else:
        bored_with_stars = False

    if star_counter > 2:
        bored_with_stars = True

def star_can_be_taken(activity):
    global cur_star, cur_star_activity, take_star

    if cur_star_activity != activity:
        cur_star_activity = 'placeholder'
    if cur_star == True and cur_star_activity == activity:
        take_star = True
        cur_star = False
    elif cur_star == False or activity != cur_star_activity:
        take_star = False

def most_fun_activity_minute():

    '''
    call the function offer_star to obtain the star status, and return the most fun activity based on this
        informtion
    str, str --> str
    '''
    global cur_health
    global cur_hedons
    global last_activity, last_activity_duration
    global last_finished
    global bored_with_stars
    global cur_state
    global cur_time
    global cur_star, cur_star_activity, take_star, bored_with_stars
    global star1_time

    star_can_be_taken(cur_star_activity)

    get_cur_state()

    if cur_state == 'not tired':
        if take_star == True:
            if bored_with_stars == False:
                most_fun_activity = 'running'

        elif take_star == True:
            if bored_with_stars == False:
                most_fun_activity = 'textbooks'

        elif take_star == True:
            if bored_with_stars == False:
                most_fun_activity = 'resting'

        elif take_star == False:
            most_fun_activity = 'running'

        elif take_star == False:
            most_fun_activity = 'running'

    elif cur_state == 'tired':
        if take_star == True:
            if bored_with_stars == False:
                most_fun_activity = 'resting'

        if take_star == True:
            if bored_with_stars == False:
                most_fun_activity = 'running'

        elif take_star == True:
            if bored_with_stars == False:
                most_fun_activity = 'textbooks'

        elif take_star == False:
            most_fun_activity = 'resting'


    return most_fun_activity

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_cur_state():
    global last_activity, last_activity_duration
    global last_finished, last_finished2
    global cur_state

    if last_finished - last_finished2 >= 120 and last_activity != ('running' or 'textbooks'):
            cur_state = "not tired"
    else:
            cur_state = "tired"

    return cur_state

###############################################################################

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10