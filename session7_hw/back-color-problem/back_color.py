from random import randint,choice

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100] 
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():

    text = choice(['BLUE','RED','YELLOW','GREEN'])
    color = choice(['#3F51B5','#C62828','#FFD600','#4CAF50'])
    quiz_type = randint(0,1)
    print(quiz_type)  

    return [text,color,quiz_type]

# 0 if users must select one the rectangles by the Meaning of the text as the answer 
# 1 if users must select one the rectangles by the Color of the text as the answer

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        if text == 'BLUE':
            return 20<=x<=120 and 60<=y<=160
        elif text == 'RED':
            return 140<=x<=240 and 60<=y<=160
        elif text == 'YELLOW':
            return 20<=x<=120 and 180<=y<=280
        elif text == 'GREEN':
            return 140<=x<=240 and 180<=y<=280

    elif quiz_type == 1:
        if color == '#3F51B5':
            return 20<=x<=120 and 60<=y<=160
        elif color == '#C62828':
            return 140<=x<=240 and 60<=y<=160
        elif color == '#FFD600':
            return 20<=x<=120 and 180<=y<=280
        elif color == '#4CAF50':
            return 140<=x<=240 and 180<=y<=280

        

            

        


    

    
    
            






 

 


        
            

   










      
