while True:
    an_a = int(input("Degree of angle a? "))
    print("Angle a is:", an_a)
    
    if an_a <= 180 and an_a >= 0:
        an_b = 180 - an_a
        print("So angle b is:", an_b)
        
        print("""
            EXPLANATION:
            
            It because those two angle sare supplementary
            which makes them equal to 180 degrees!
            """
            "So if angle a is", an_a, "then angle b is", an_b
            )
        break

    else:
        print("""
        ERROR:
        
        This program has been temporary been stopped,
        because of angle a's value being unrealistic.
        
        Such as angle a's value being higher than 180,
        or angle a's value being lower than 0.
        
        Please retry again.
        """)