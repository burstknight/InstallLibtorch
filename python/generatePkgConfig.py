import argparse

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

def main(oArgs):
    print("input: %s" %(oArgs.input))
    print("output: %s" %(oArgs.output))
# End of main

if "__main__" == __name__:
    oArgs = parseArgs()
    main(oArgs)
# End of if-condition
