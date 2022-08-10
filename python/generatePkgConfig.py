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

def main(oArgs):
    if False == os.path.isdir(oArgs.input):
        print("\x1b[31mError: The value of the argument \"--input\" must be a directory!\1xb[0m")
        return
    # End of if-condition

    if False == os.path.isdir(oArgs.output):
        print("\x1b[31mError: The value of the argument \"--output\" must be a directory!\1xb[0m")
        return
    # End of if-condition

    if not "libtorch" in os.listdir(oArgs.input):
        print("\x1b[31mError: The directory \"libtorch\" is found in \x1b[34m%s\x1b[0m" %(oArgs.input))
        return
    # End of if-condition

    strPath = os.path.join(oArgs.output, "libtorch.pc")
    with open(strPath, "wt", encoding="utf-8") as oWriter:
        print("Writing prefix...", end="")
        oWriter.write("lib_name=libtorch\n");
        oWriter.write("prefix=/opt/${lib_name}\n");
        oWriter.write("include_dir=${prefix}/include\n");
        oWriter.write("lib_dir=${prefix}/lib\n\n");
        oWriter.write("Name: ${lib_name}\n");
        oWriter.write("Description: C++ version torch library for deep learning\n")

        strPath = os.path.join(oArgs.input, "libtorch/build-version")
        with open(strPath, "r", encoding="utf-8") as oReader:
            strVersion = oReader.read().strip()
            oWriter.write("Version: %s\n" %(strVersion))
        # End of with-block

        print(" Done!\nWriting libs...", end="")

        oWriter.write("Libs: -Wl,-no-undefined -Wl,--no-as-needed")
        vstrLibFiles = ["torch", "torch_cpu", "c10"]
        for strLibFile in vstrLibFiles:
            oWriter.write(" -L${lib_dir} -l%s" %(strLibFile))
        # End of for-loop

        print(" Done!\nWriting includes...", end="")

        oWriter.write("\nCflags: -I${include_dir}")
        oWriter.write(" -I${include_dir}/torch/csrc/api/include")
        oWriter.write(" -D_GLIBCXX_USE_CXX11_ABI=1 -std=gnu++14")


        oWriter.write("\n")
        print(" Done!")
    # End of with-block

    print("Finished!")
# End of main

if "__main__" == __name__:
    oArgs = parseArgs()
    main(oArgs)
# End of if-condition
