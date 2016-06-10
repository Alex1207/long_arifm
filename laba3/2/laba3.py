import sys
import MathFuncsDll
print"\nEnter :\
\n<ProgramName> <FileName A> <Operation> <FileName B> <ResultFileName> [-b] \n\
Posible operations: \n\
\"+\" - addition\n\
\"-\" - subtraction\n\
\"*\" - multiplication\n\
\"/\" - division\n\
\"%\" - taking the remainder\n\
\"^\" - power by module\n"
l = len(sys.argv)
if (l > 7):
    print "\nToo many parameters...\n"
    sys.exit(1)
if ((l > 0) and (l < 6)):
    print "\nIntroduced not all parameters...\n"
    sys.exit(1)
if ((sys.argv[2][0] == "^") and (l < 7)):
    print "\nModule is not introduced...\n"
    sys.exit(1)
# (len(sys.arvg[2]) > 1):
#    print "Wrong input operation...\n"
#    sys.exit(1)
fNameA = sys.argv[1]
DoIt = sys.argv[2]
fNameB = sys.argv[3]
fNameOut = sys.argv[4]
bi=sys.argv[5]

if(bi == "-b"):
    ReadFlag = "rb"
    WriteFlag = "bw"
else:
    ReadFlag = "r"
    WriteFlag = "w"
a = MathFuncsDll.LongInt()
b = MathFuncsDll.LongInt()
c = MathFuncsDll.LongInt()
if (not a.Read(ReadFlag, fNameA)):
    sys.exit(1)
if (not b.Read(ReadFlag, fNameB)):
    sys.exit(1)
if DoIt == "+":
    c = a + b
if DoIt == "-":
    c = a - b
if DoIt == "*":
    c = a * b
if DoIt == "/":
    c=a / b
    if (c.CheckSize()):
        sys.exit(1)
if DoIt == "%":
    c = a % b
    if (c.CheckSize()):
        sys.exit(1)
if DoIt == "^":
    fNameM=sys.argv[6]
    mod = MathFuncsDll.LongInt()
    if (not mod.Read(ReadFlag, fNameM)):
        sys.exit(1)
    c=c.Pow(a, b, mod);
    if c.CheckMinus():
        sys.exit(1)
c.Print();	
if (not c.WriteFile(WriteFlag, fNameOut)):
    sys.exit(1)

    
