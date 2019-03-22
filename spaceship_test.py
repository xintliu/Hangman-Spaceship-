'''
CS 
HW5
XINTONG LIU
3/21/2019
'''
import spaceship
'''
test pickword()
no input
except random word
success
'''
def main():
    success=0
    '''
    test pickword()
    no input
    expectrandom word
    success
    '''
    print(spaceship.pickword())
    success += 1
    '''
    test spaceship()
    input 2
    expect a left body
    success
    '''
    
    spaceship.spaceship(2)
    success += 1
    
    '''
    test spaceship()
    input sissy
    expect a 5 blank spaces
    success
    '''
    
    spaceship.blank_spaces('sissy')
    success += 1
    
    '''
    test right_guess(i,1)
    input a,2
    expect a on the 2nd position
    success
    '''
    
    spaceship.right_guess('i',1)
    success += 1
    '''
    test wrong_guess(a,0)
    input a,0
    expect a of left side
    success
    '''
    spaceship.wrong_guess('a',0)
    success += 1

    '''
    scores(90)
    input cc(name)
    expect updated in file
    success
    '''
    spaceship.scores(90)
    success += 1
    '''
    '''
    record=spaceship.playgame(0)
    spaceship.scores(record)
    print(success)

    '''
    
main()
