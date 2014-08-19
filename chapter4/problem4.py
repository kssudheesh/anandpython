#What will be the output of the following program?ans:a,d
def f():
    try:
        print "a"
        return
    except:
        print "b"
    else:
        print "c"
    finally:
        print "d"
f()
