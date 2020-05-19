def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon' #this is a local

def ham():
    print(eggs) #this is global 
    
eggs = 42 #this is the global
spam()  
print(eggs)