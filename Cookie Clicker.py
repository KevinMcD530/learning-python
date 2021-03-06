"""
Cookie Clicker Simulator
"""

import simpleplot
import math
import random

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 100.0
class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_game_time = 0.0
        self._current_cps = 1.0
        self._history_list = [(0.0, None, 0.0, 0.0)]
        
        
    def __str__(self):
        """
        Return human readable state
        """
        return "TotalCookies:" + str(self._total_cookies) + "\n"\
    + "CurrentCookies:" + str(self._current_cookies) + "\n"\
    + "CurrentTime:" + str(self._current_game_time) + "\n"\
    + "CurrentCPS:" + str(self._current_cps) + "\n"
                
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_game_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        _history_copy = [] 
        _history_copy.extend(self._history_list)
        
        return _history_copy

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        else:
            _secs_to_cookie_goal = math.ceil((float(cookies - self._current_cookies)) / float(self._current_cps))
        return _secs_to_cookie_goal
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time >= 0.0:
            self._current_game_time += time
            self._current_cookies += (self._current_cps * time)
            self._total_cookies += (self._current_cps * time)
            
        return self._current_game_time, self._current_cookies, self._total_cookies
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history_list.append((float(self._current_game_time), item_name, float(cost), float(self._total_cookies)))
        else:
            pass
        return self._history_list, self._current_cookies, self._current_cps
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    
    #initialize game state class and clone of build_info
    sim_state = ClickerState()
    cloned_build = build_info.clone()
    
    #outermost loop ensuring game only runs as long given duration
    while sim_state.get_time() <= duration:
        
        #Call strategy function to determine what to buy
        strat_buy = strategy(sim_state.get_cookies(),
                             sim_state.get_cps(),sim_state.get_history(),
                             (duration - sim_state.get_time()),
                             cloned_build)
        #print "Going to buy item :",strat_buy
        if strat_buy is None:
            break
        
        #Take strat_buy and determine how much time needs to pass to buy
        else:
            cost_to_buy = cloned_build.get_cost(strat_buy)
            time_to_buy = sim_state.time_until(cost_to_buy)
            #print "time to buy the item is :", time_to_buy
            
            #check if time to buy will be after game is over
            if (time_to_buy + sim_state.get_time()) > duration:
                break
            
            
            #Check if we already have enough to buy
            elif time_to_buy == 0.0:
                sim_state.buy_item(strat_buy,cost_to_buy,
                                   cloned_build.get_cps(strat_buy))
                cloned_build.update_item(strat_buy)
            
            #Waits as needed to make the purchase
            else:
                sim_state.wait(time_to_buy)
                sim_state.buy_item(strat_buy,cost_to_buy,
                                   cloned_build.get_cps(strat_buy))
                cloned_build.update_item(strat_buy)
                 
                    
            
    
    time_left = duration - sim_state.get_time()
    sim_state.wait(time_left)
    #print sim_state.__str__()
    return sim_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    
    item_list = build_info.build_items()
    min_item = item_list[0]
    potential_cookies = cookies + (cps * time_left)
    
    #walk through item list, check cost, set it to min_item
    
    #if it is cheapest
    
    for dummy_key in item_list:
        if build_info.get_cost(dummy_key) < build_info.get_cost(min_item):
            min_item = dummy_key
    
    
     
    if build_info.get_cost(min_item) <= potential_cookies:    
        
        return str(min_item)
    else:
        return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    item_list = build_info.build_items()
    max_item = item_list[0]    
    potential_cookies = cookies + (cps * time_left)
    
    #walk through item list, check cost, set it to max_item
    
    #if it is most expensive
    
    for dummy_key in item_list:
        if build_info.get_cost(dummy_key) > build_info.get_cost(max_item) and build_info.get_cost(dummy_key) < potential_cookies:  
            max_item = dummy_key
        
    if build_info.get_cost(max_item) < potential_cookies:
        print "buying item :", max_item
        print "item cost :", build_info.get_cost(max_item)
        return str(max_item)
    else:
        return None
    

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()

#test_object = ClickerState()

#print test_object.__str__()
#print test_object.get_history()


#test_import = provided.BuildInfo()
#print test_import.build_items()[0]
#print test_import.build_items()
