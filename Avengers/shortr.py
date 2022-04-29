
def s(var):

    yes = ["Yes", "yes", "Y", "y", "Yes!", "yes!"]
    no = ["No", "no", "N", "n", "No!", "no!"]
    stop = ["Stop", "stop", "Stop!", "stop!"]
    cancel = ["Cancel", "cancel"]

    if var in yes or var in no or var in stop or var in cancel:

        for i in range(len(yes)):
            if var == yes[i]:
                var = "yes"


        for i in range(len(no)):
            if var == no[i]:
                var = "no"

        for i in range(len(stop)):
            if var == stop[i]:
                var = "stop"

    return var


#---------------------------------------------------------------------------------------------#


def sf(var):

    if s(var) == var:
        var = "error"

    return var
