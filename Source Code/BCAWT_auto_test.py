def auto_test():
    '''
    Run a demo test demo.

    Returns:
        creates a folder named "test_demo" with 23 results ( see the documentation for more details about the expected output )
    '''
    from BCAWT import BCAWT
    BCAWT.BCAW('Ecoli','test_demo',fasta=True,Auto=True)



print ("===============================")

def auto_check_files():
    '''
    Run a demo test demo.

    Returns:
        check the expected outputs
    '''
    import glob
    text = [ i for i in glob.glob("Result\\test_demo\\*.txt")]
    csv = [ i for i in glob.glob("Result\\test_demo\\*.csv")]
    png = [i for i in glob.glob("Result\\test_demo\\*.png")]

    if len(text) == 4 and len(csv) == 8 and len(png) == 11:
        print ("test is completed 'successfully'")
    else:
        print ("Something going wrong please, see the documentation or contact the developer")
