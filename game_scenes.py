#--------------------------
# THESE ARE THE SCENES
#---------------------------




from sys import exit
from random import randint
import bad_guys






backpack = [] 


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass"
        print "it and implement enter()."
        exit(1)
    
    
        
        
class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "such a loser.",
        "I have a small puppy thats better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
     ### make this offer replay option
     

class FrontGate(Scene):
    
    def enter(self):
        print "\nIt's about midnight and your dog Shnookims"
        print "decides he conveniently needs to choose"
        print "this as the perfect time to go outside.\n"
        print "You're walking down the sidewalk past"
        print "Old Man Flanders' condemned, decrepid,"
        print "remnant of a house.\n" 
        print "Old Man Flanders died in 1857. During"
        print "his life however he was a strange guy."
        print "Mostly kept to himself, locked away inside"
        print "the house. Nobody really knew what he did"
        print "in there, but dark rumors were commonplace"
        print "among the townfolk.\n"
        print "The most widely accepted belief regarding"
        print "the mysterious life of Old Man Flanders,"
        print "was that of his late wife and child."
        print "You see, they suffered from a rare strain"
        print "of tuberculosis and passed away when Old"
        print "Man Flanders was merely 28 years of age.\n"
        print "They say the death of his family drove him"
        print "into psychosis, and that he would spend the"
        print "remainder of his years attempting to reach" 
        print "out to his dead wife and child. Every night" 
        print "For decades, a dim light and low voices"
        print "would echo from the small attic window.\n\n"
        print "What made the townfolk curious, though,"
        print "was that Old Man Flanders lived alone...\n\n"
        
        action = raw_input('[PRESS ENTER TO PLAY]')
        
        if action == '':
            print "\nWhile walking past the front gate,"
            print "Shnookims hears a rustling and takes" 
            print "off running into Old Man Flanders yard."
            print "\n"
            print "You chase Shnookims through the creaky"
            print "gate, and into the yard."
            print "Shnookims is nowhere in sight..."
            return 'yard' 
        else:
            print "\n\n\n"
            return 'death'
         
 
 
 
        
class Yard(Scene):
    
    def enter(self):
        print "\n\n"
        print "This is kind of a creepy old yard. You see" 
        print "what looks like an old shed to the left of"
        print "the crooked house. Near the back right of"  
        print "the property there is an over grown garden."
        print "\n\nThe front porch is rotten, but maybe"
        print "it'll hold you if you'd like to try the"
        print "door..."     
        
        while True:
            print "\nwhere would you like to go?\n"
        
            action = raw_input('> ').lower()
    
            if 'door' in action:            
                print "\nIt's locked, you'll have to"    
                print "find another way to get inside."
            elif 'shed' in action:
                return 'shed'
            elif 'garden' in action:
                return 'garden'
            else:
                print "\nNot sure that's an option..."
            
            
            

class Shed(Scene):

    
    def enter(self):

        print "\nYou walk slowly over to the shed to"
        print "see if Shnookims is hiding in there\n" 
        print "No dog, but this is interesting.\n" 
        print "A glass bottle with a cross imprinted on"
        print "on the side... could it be holy water?"
        print "\nYou should probably take that...\n"
        print "It looks like there is also some kind"
        print "of hatch on the floor.\n\n"
    
        
        while True:
            print "\nWhat now?\n"
            
            action = raw_input('> ').lower()
            
            if 'hatch' in action:
                print "\nTheres a tunnel here."
                print "see where it goes?\n"
                
                tunnel = raw_input('[YES or NO]> ').lower()
                
                if 'yes' in tunnel:
                    return 'cellar'
                else:
                    print "I don't blame you, that tunnel"
                    print "gives me the heeby jeebys.\n"
                    
            elif 'water' in action or 'bottle' in action:
                global backpack
                if 'water' in backpack:
                    print "\nYou already put the holy"
                    print "water in your backpack.\n"
                else:
                    print "\nYou put the holy water in your"
                    print "backpack. That'll come in handy."
                    backpack.append('water')
            elif 'yard' in action:
                return 'yard'
            elif 'garden' in action:
                return 'garden'
            else:
                print "\nNot sure that's an option...\n"
                
                
    
class Garden(Scene):
    global backpack
    
    demon_name = 'SALAZAR'
    caller = 'garden'
    this_bad = 0    
    def enter(self):
        
        if 'demon_gard' in bad_guys.demon_x:
            print "As you creep over to the garden," 
            print "you notice something move behind the"
            print "rusty fence. It looked a bit big to be" 
            print "Shnookims. Maybe the wind moved the tall"
            print "over grown weeds.\n"
            print "What's that noise?"
            print "It sounds like a whisper...\n"
            print "Are you sure you want to enter the"
            print "garden?\n"
            
            garden = raw_input('[YES or NO]> ').lower()
        
            if garden == 'yes':  
                return bad_guys.demon(self)
                                        
            else:
                print "\nWay to scary!"
                print "get out of there!!" 
                return 'yard'
            
        else:        
            print "\nThe garden is just as creepy as usual."
            print "Good thing we killed that demon. Look"
            print "at these crumbling headstones. Poor"
            print "family... I wonder what this brick"
            print "patter on the ground is..."
            print "Looks like some kind of portal.\n"
            print "Keep looking for that damn mut?\n"
            
            looking = raw_input('[YES or NO]> ').lower()
            
            if 'yes' in looking:
                return 'yard'
            else:
                return 'garden'
            

            
          
flanders_ghostw = ['yes']
class BedOne(Scene):
    global flanders_ghostw
    def enter(self):
        
        if 'yes' in flanders_ghostw:
            print "\nThere's someone standing in the corner"
            print "of the room... ITS A GHOST!!!\n"
            print "The ghost of Flanders wife turns to look"
            print "at you. Her eyes filled with sorrow, and"
            print "fear.\n"
            print "She disappears.\n"
            flanders_ghostw.pop()
            return 'bed_1'
        else:
            print "\nThis room is a tid bit spooky I'd say."
            print "Peeling green flower wall paper."
            print "Tall victorian window, boarded shut.\n" 
            print "There are 2 doors, a blue door and a"
            print "big wooden door.\n"
            while True:
                print "What now?\n"
                
                action = raw_input('> ').lower()
                
                if 'wooden' in action or 'big' in action:
                    return 'hall'
                elif 'blue' in action:
                    return 'bed_2'
                elif 'chute' in action or 'coal' in action:
                    print "\nThis is a tight fit, but I" 
                    print "think it'll hold.\n"
                    return 'cellar'
                else:
                    print "\nNot sure that's an option.\n"
                 
     
class Hall(Scene):
    
    def enter(self):
        print "\nYou're standing in a long hallway with 2"
        print "doors. You can either walk down the the"
        print "hall, go through the big wooden door, or go"
        print "through the small door.\n"
        
        while True:
            print "Which way?\n"
            
            action = raw_input('> ')
            
            if 'big' in action or 'wooden' in action:
                return 'bed_1'
            elif 'small' in action:
                return 'bed_2'
            elif 'hall' in action:
                return 'living_room'
            else:
                print "Not sure that's an option."  


class BedTwo(Scene):
    
    caller = 'bed_2'
    this_bad = 2
    
    def enter(self):
        
        if 'ghost_2' in bad_guys.demon_x:
            return bad_guys.ghost(self)
        else:
            print "\nThis room is dark... You dont like it"
            print "at all..."
            
            while True:    
                print "\nDo you want to go back through"
                print "the blue door, or through the small"
                print "door in front of you?\n"
                
                action = raw_input('> ').lower()
                
                if 'blue' in action:
                    return 'bed_1'
                elif 'small' in action:
                    return 'hall'
                else:
                    print "\nNot sure that's an option."
                    
    
        
class BedThree(Scene):

    caller = 'bed_3'
    this_bad = 3
    
    def enter(self):
        
        if 'ghost_3' in bad_guys.demon_x:
            return bad_guys.ghost(self)
        else:
            print "\nThere's nothing in this room but more"
            print "boarded windows, the door, and a closet."
            
            while True:
                print "\nWhich way boss?\n"
                
                action = raw_input('> ').lower()
                
                if 'door' in action:
                    return 'living_room'
                elif 'closet' in action:
                    return self.closet_d()
                else:
                    print "Not sure that's an option." 

    def closet_d(self):
        
        print "\nThis closet is a little cramped, but"
        print "the back wall looks funny...\n"
        print "It's a secret door. Do you want to go"
        print "through it?\n"
        
        action = raw_input('[YES or NO]> ').lower()
        
        if 'yes' in action:
            return 'bed_4'
        else:
            print "\nI don't blame you. thats pretty"
            print "spooky."
            return 'bed_3'
    
    
flanders_kid = ['yes']
class BedFour(Scene):
    global flanders_kid
    def enter(self):
        
        if 'yes' in flanders_kid:
            print "\nThere's a small child standing in the"
            print "room... it's the ghost of Old Man"
            print "Flanders' daughter... She looks so"
            print "innocent.\n"
            print "She walks up to you slowly, and hands"
            print "you a diary... I think she wants you to"
            print "read it...\n"
            print "This diary is intense... Written by the"
            print "Old Mans daughter. It tells the truth"
            print "about the family... and the tragic death"
            print "of the Old Mans wife and daughter.\n"
            print "You see, his wife was a witch... always"
            print "working secretly in the attic."
            print "The Old Man didn't know about her evil"
            print "witchcraft, animal sacrifices, or"
            print "satanic spells... That is until her"
            print "witchery turned to their daughter."
            print "The last part says there is only one way"
            print "to the attic... something about the"
            print "living room.\n"
            print "The rest of the diary is waterlogged"
            print "from the century of rot this house has"
            print "had to endure... Poor kid.\n"
            print "You put the diary in your backpack."
            
            backpack.append('diary')   
            flanders_kid.pop()
            return 'bed_4'
        else:
            print "\nThis isnt't much of a room at all"
            print "more of a crawl space. Must be where the"
            print "Old Mans daughter would hide from her"
            print "evil mother."
            while True:
                
                print "\nSeems to be only one way to go."
                print "The door we came in."
                print "\nWhat now?\n"
                
                action = raw_input('> ').lower()
                
                if 'door' in action:
                    return 'bed_3'
                else:
                    print "Not sure that's an option."
                
                
                
class LivingRoom(Scene):
    global backpack
    global scoop
    def enter(self):
        
        print "\n"
        print "This living room looks like a horror show." 
        print "Cob webs eveywhere, stained white curtains" 
        print "over the furniture, and animal bones.\n"
        print "The chimney is obviously open to the roof,"
        print "there's a freezing draft coming down it."
        print "The iron fire pokers are thrown on the"
        print "floor. It would be a good idea to grab one."
        print "There is a door on the opposite end of the"
        print "room. I wonder what's in there."
        print "\n There seems to be 2 ways you can go:"
        print "Back down the hall or through the door."
         
        return self.while_loop()
        
    def while_loop(self):
        while True:
            print "\nWhat now?\n"
            
            action = raw_input('> ').lower()
            
            if 'door' in action:
                return 'bed_3'
            elif 'hall' in action:
                return 'hall'
            elif 'poker' in action or 'iron' in action:
                self.pokey_iron()
            elif 'chimney' in action:
                return self.chimney_climb()                
            else:
                print "Not sure that's an option."
          

    def pokey_iron(self):
        if 'iron' in backpack:
            print "\nYou already have an iron poker."
        else:
            print "\nYou put an iron poker in your"
            print "backpack. That'll come in handy."
            print "\n"
            backpack.append('iron')
            # put ghost function here
            
    def chimney_climb(self):
        
        print "\nIt looks like there are some metal"
        print "pegs all the way up the chimney.\n"
        print "Do you want to climb?\n"
        
        resp = raw_input('[YES or NO]> ').lower()
        
        if 'yes' in resp:
            print "\nIts pretty dusty but you can"
            print "handle it.\n"
            
            return 'roof'
        else:
            print "\nI don't blame you, its probably"
            print "going to collapse anyway."
            return 'living_room'
    # shimmy to the roof - secret - kind of hint
    
    
  

class Cellar(Scene):
    global backpack
           
    demon_name = 'BALTHAZAR'
    caller = 'cellar'
    this_bad = 1   

    def enter(self):
        
        if 'demon_cell' in bad_guys.demon_x:
            
            return bad_guys.demon(self)
    
        else:
            print "\nThis cellar is dark and spooky."
            print "Jars on shelves, spider webs."
            print "The foundation of the house looks like"
            print "it's crumbling apart.\n"
            print "The stair case fell apart after all of"
            print "these years. It looks like the only"
            print "two directions for you to go are back" 
            print "out the tunnel to the shed, or up this" 
            print "old coal chute."
            
            while True:
                print "\nWhich way would you like to go?\n"
                
                action = raw_input('> ').lower()
                
                if 'chute' in action or 'coal' in action:
                    print "\nThis is a tight fit, but I" 
                    print "think it'll hold.\n"
                    return 'bed_1'  
                elif 'tunnel' in action or 'shed' in action:
                    return 'shed'
                else:
                    print "Not sure that's the best idea."
           
                 
    # Tunnel from shed 


class Roof(Scene):
    
    demon_name = 'FLUFFOGUS'
    caller = 'roof'
    this_bad = 4   
    
    
    def enter(self):
        
        if 'demon_roof' in bad_guys.demon_x:
            return bad_guys.demon(self)
        else:
            print "\nThe moon is full and shining on you."
            print "From the top of the house you can see"
            print "the whole yard. The shed, the garden,"
            print "the front gate. There is a door to the"
            print "attic about 20 feet away.\n"
            print "This roof top feels like it is going to"
            print "collapse. you'd better move quickly.\n"
            
            while True:
                print "You can either climb back down the"
                print "chimney, or check out the attic"
                print "door.\n\nWhat now?\n"
                
                action = raw_input('> ').lower()
                
                if 'attic' in action or 'door' in action:
                    return 'atticd'
                elif 'chimney' in action:
                    return 'living_room'
                
                 
                
 
            
    
    
class Attic(Scene):
    
    this_bad = -1
    
    def enter(self):
        if 'final' in bad_guys.demon_x:
            print "\nThis attic is about as scary as it gets."
            print "The walls are covered in old articles and"
            print "satanic symbols...\n"
            print "Theres a journal on the table.\n"
            print "It was Old Man Flanders'. It says that he"
            print "spent all those years, after his families"
            print "death, trying to lock his wife away from"
            print "this world forever... the last thing he"
            print "needed was the spell in the cover of his"
            print "daughters diary... She put it in the crawl"
            print "space and he wasnt able to find it before"
            print "his death... He tried everything..."
            print "The best he could do is keep her trapped in"
            print "the attic... that is as long as nobody"
            print "opened the door...\n"
            
            while True:
                action = raw_input('[PRESS ENTER]')
                
                if action == '':                
                    return bad_guys.finalb(self)
                else:
                    print '\nCome on wimp.\n'
        else:
            print "\nWOW this is some kind of portal!\n"
            return 'garden'
            
                
          
    # turns out flanders spent the remainder of his years
    # keeping that bitch on lock down ---
    
    
    
    # Final Boss (flanders wife - twist - witch)
    # appears after you find Shnookims and read about  
    # how to kill her 

class Finished(Scene):
    
    def enter(self):
        print "\nYou found Shnookims up in the attic!!!"
        print "What the heck was this damn mut doing up"
        print "here anyways... Let's hope this type"
        print "of haunted escapade never happens again.\n"
        print "CONGRATULATIONS!! YOU WIN!!!\n"
        print "Now get your dog a leash.\n"
         
    
    
    
    # Shnookims
    
    
    
    
    
   
    
    
    
    
    
