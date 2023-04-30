while(True):
    import random
    print("****Guess The Number****")
    name=input("Enter Your Good Name: ")
    print(f'welcome {name}')
    l=input("Select Your Level: ")
    if l=='easy':
        rd= random.randrange(1,100)
                                                                               
        while(True):
            
            n=int(input("Enter your Guess Number: "))
            if rd>n:
                print("Too Small")
            elif rd<n:
                print("Too Large")
            elif rd==n:
                print("Hurrah! You Won The Game")
                break
    print(" ")
                                                                                
    print("Do You Want To Play It Again")
    choice=input("Enter Your Choice: ")
    if choice=='no':
        print(f'Thank You {name}!')
        break
                                                                                        
                                                                                          
                                                                    
                                                                
                                                                

              
              
              

