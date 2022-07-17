import argparse
import os

def parseArgs():
    """
    Description:
    =====================================================
    Parse the arguments from command line.

    Args:
    =====================================================
    - no args

    Returns:
    =====================================================
    - rtype: Namespace, the parsed arguments
    """
    oParser = argparse.ArgumentParser(prog="generatePkgConfig.py", description="Generate \".pc\" file of libtorch for pkg-config.")

    oParser.add_argument("--output", "-o", type=str, required=True, help="Set the output file path.")
    oParser.add_argument("--input", "-i", type=str, required=True, help="Set the path where libtorch locates in.")

    return oParser.parse_args()
# End of parseArgs

def lsItems(strRootDir:str, isMode:bool) -> list:
    """
    Description:
    =====================================================
    List the items in the given directory

    Args:
    =====================================================
    - strRootDir: ptype: str, the root directory of libtorch
    - isMode: ptype: bool, find all directories in the given path if this flag is True, otherwise find all files

    Returns:
    =====================================================
    - rtype: list, the list of the directories or files that have all header file for libtorch
    """
    vstrItems = os.listdir(strRootDir)

    vstrFoundItems = []
    for strRoot, vstrSubDirs, vstrSubFiles in os.walk(strRootDir):
        if True == isMode:
            for strSubDirs in vstrSubDirs:
                strPath = os.path.join(strRoot, strSubDirs)
                vstrFoundItems.append(strPath)
            # End of for-loop
        else:
            for strFile in vstrSubFiles:
                strPath = os.path.join(strRoot, strFile)
                vstrFoundItems.append(strPath)
            # End of for-loop
        # End of if-condition
    # End  of for-loop

    return vstrFoundItems
# End of lsItems

def main(oArgs):
    print("input: %s" %(oArgs.input))
    print("output: %s" %(oArgs.output))
    
    print("Sub directories:\n" + str(lsItems(oArgs.input, True)))
    print("\nSub files:\n" + str(lsItems(oArgs.input, False)))
# End of main

if "__main__" == __name__:
    oArgs = parseArgs()
    main(oArgs)
# End of if-condition
