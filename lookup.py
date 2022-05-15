# issuegenerator
#
# This script opens the Reference of an opcode, gen-routine etc. (item) in the
# Csound Reference Manual (http://www.csounds.com/manual/html/)
#
# ##################################################
#
# Arguments: item
#
# ##################################################
#
#

import sys
import webbrowser

# csound manual url
manualurl = 'http://www.csounds.com/manual/html/'

# check if required arguments are given

if len(sys.argv) < 2:
    print("Error: Please anter an item to look up in the Csound manual")
    sys.exit(0)

else:
    # check if a gen routine is being looked-up (then convert input to uppercase)
    if sys.argv[1][0:3].lower() == "gen":
        theitem = sys.argv[1].upper()
    else:
        theitem = sys.argv[1].lower()

    # open reference manual page
    webbrowser.open(manualurl+theitem+".html")
