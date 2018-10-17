class Synthesize(object):
    def __init__(self):
        super(Synthesize).__init__()
    def convert(self, number):
        count = 0
        for i in number:
            if count == 0:
                if number[0] == "0":
                    pass
                else:
                    place = "thousands"
                    print(number[0] + " " + place)
            if count == 1:
                if number[1] == "0":
                    pass
                else:
                    if number[0] != "0":        
                        place = "hundreds"
                        print(number[1] + " " + place)
                    else:
                        place = "hundreds"
                        print(number[1] + " " + place)
            if count == 2:
                if number[2] == "0":
                    pass
                else:
                    if number[0] != "0":
                        place = "tens"
                        print(number[2] + " " + place)
                    else:
                        place = "tens"
                        print(number[2] + " " + place)
            if count == 3:
                if number[3] == "0":
                    pass
                else:
                    if number[0] != "0":
                        place = "ones"
                        print(number[3] + " " + place)
                    else:
                        place = "ones"
                        print(number[3] + " " + place)
                    
            count = count + 1
        


    
    
