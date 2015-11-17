import game_scenes


demon_x = ['demon_gard', 
           'demon_cell', 
           'ghost_2', 
           'ghost_3',
           'demon_roof',
           'final'
           ]


def demon(self):
    global demon_x
    
    print "\nA cloud of smoke appears out of nowhere" 
    print "and the stench of sulfur overcomes you."
    print "\nA man in a black suit walks out of the"
    print "shadows. His eyes are solid black. his"
    print "mouth isn't moving but you can hear his"
    print "voice in your head....\n\n"
    print "'I AM %s, THE HELL DEMON" % self.demon_name
    print "OF THE 666th COLONY. YOUR SOUL"
    print "BELONGS TO ME!!'\n\n"
    print "The demon moves from in front of you to"
    print "behind you in a split second."
    print "What is this black magic?"
    print "\nYou'd better think quickly about your"
    print "next move or it could be your last."

    
    
    while True:
        print "\nDo you want to fight the demon?"
        print "Or would you prefer to run away?...\n"
        
        action = raw_input('> ').lower()
        
        if 'fight' in action:
            if 'water' in game_scenes.backpack:
                print "\nYou side-step and turn, pulling" 
                print "the holy water out of your back" 
                print "pack and splashing it on the" 
                print "demon.\n"
                print "That evil twat lights up like" 
                print "the fourth of july and turns to" 
                print "dust in a fit of howling rage.\n"
                
                demon_x.pop(self.this_bad)
                
                # how do i set demon_cell to a variable
                #so i can use this 1 function for all demons
                return self.caller
            else:
                print "\nYou side-step and turn to"
                print "punch the demon in the face."
                print "Before you make contact, the"
                print "demon puts his hand on your"
                print "forhead and sucks the soul"
                print "out of you eyes, in a fiery"
                print "torturous rage that seems like"
                print "an eternity..."
                return 'death'
        elif 'run' in action:
            print "\nYou side-step and turn to"
            print "make a run for your life."
            print "Before you make it out, the"
            print "demon puts his hand on your"
            print "forhead and sucks the soul"
            print "out of your eyes in a fiery,"
            print "torturous rage that seems like"
            print "an eternity..."
            return 'death'
        else:
            print "\nNot sure that's the best option"
            print "given your current situation."


def ghost(self):
    global demon_x
    
    print "\nA chill goes up your spine. It feels like"
    print "the temperature dropped 15 degrees.\n"
    print "A man is standing in front of you. At least"
    print "you think so... His body is flickering as if"
    print "nobody may be there at all.\n"
    print "It's a ghost..."
    print "His face looks ruined, rotten, hateful."
    
    while True:
        print "\nDo you want to fight the ghost?"
        print "or do you want to run?\n"
        
        action = raw_input('> ').lower()
        
        if 'fight' in action:
            if 'iron' in game_scenes.backpack:
                print "\nGood thing you picked up that"
                print "iron poker. You pull it out and"
                print "swing straight through that evil"
                print "specter.\n"
                print "The ghost seems to blow away, like"
                print "a cloud of smoke.\n"  
                
                demon_x.pop(self.this_bad)
                return self.caller
            else:
                print "\nYou turn to swing a punch at the"
                print "ghosts face, only to realize you"
                print "can't touch him. Your fist goes"
                print "right through the bastard as if"
                print "he was made of candle smoke.\n"
                print "He grabs you and immediately you see"
                print "that you aren't in Old Man Flanders"
                print "house anymore. Your falling through"
                print "horrible memories of the ghosts"
                print "past life...\n"
                print "You're soul is doomed to haunt the"
                print "Old Mans house of horrors forever."  
                
                return 'death'
        elif 'run' in action:
            print "\nYou turn to run for your life." 
            print "He grabs you and immediately you see"
            print "that you aren't in Old Man Flanders"
            print "house anymore. Your falling through"
            print "horrible memories of the ghosts"
            print "past life...\n"
            print "You're soul is doomed to haunt the"
            print "Old Mans house of horrors forever."  
            
            return 'death'
        else:
            print "\nNot sure that's the best option"
            print "given your current situation."
            
     
    
    
    
def finalb(self):
    global demon_x
    
    print "\nHoly moly Flanders wife appears in front of you"
    print "She is about as scary as it gets. Dark evil eyes,"
    print "bloody hands. She lets out a demented scream."
    
    while True:
         print "\nDo you want to fight, or run?\n"
         
         x = raw_input('> ').lower()
         
         if 'fight' in x: 
             if 'diary' in game_scenes.backpack:
                 print "\nYou pull the diary out of your"
                 print "backpack and read the spell under the"
                 print "front cover.\n"
                 print "'OOGA BOOGA HOCUS POCUS MALOCUS'"
                 print "\nShe lets out a blood curdling shriek."
                 print "and disappears...\n"
                 print "The curse is over... She's gone..."
                 print "The Old Man and his daughter can"
                 print "finally be at piece.\n"
                 
                 demon_x.pop(self.this_bad)
                 return 'finished'
             else:
                 print "\nShe does some evil witchery and"
                 print "locks you away in a box that keeps"
                 print "shrinking forever.\n" 
                 return 'death'
         elif 'run' in x:
             print "\nYou try to run away... not so much."
             print "She does some evil witchery and"
             print "locks you away in a box that keeps"
             print "shrinking forever.\n" 
         
             return 'death'
         else:
            print "\nNot sure that's an option."
        
            
      
    
    
    
    
    
    
    
    
    
    
    

