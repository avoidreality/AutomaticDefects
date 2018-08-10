

INPUT = ''
defects = []

while(INPUT != "STOP MOFO"):
    INPUT  = raw_input('Please enter a defect number: ')
    print 'You entered %s.' % INPUT
    

    if (INPUT != "STOP MOFO"):
        defects.append(int(INPUT))
        

    if (INPUT == "STOP MOFO"):
        print "Entering defects complete."
        

print ":) " * 5
print "Printing the sorted list of defects now."
print ":) " * 5
#sort the defects
defects.sort()

#print the sorted defects
for i in defects:
    print i

print ""

#show the number of defects
print "The number of defects is: %d " % (len(defects))

print ""
#output HPQC friendly 'or' statements to copy/paste into HPQC
defects2 = []
for i in defects:
    defects2.append(str(i))


print "*" * 10
print "Your HPQC friendly defects list is as follows."
print "*" * 10

print ' or '.join(defects2)


