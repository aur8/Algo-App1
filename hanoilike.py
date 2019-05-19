# Hanoi like for app1
    
def hanoilike(ndisks, startPeg=1, endPeg=3): #using n disks like n containers
    if ndisks:
        hanoilike(ndisks-1, startPeg, 6-startPeg-endPeg)
        print "Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg) #using sentences to describe what's happening like trace
        hanoilike(ndisks-1, 6-startPeg-endPeg, endPeg)
        
        #then test it with an integer 
