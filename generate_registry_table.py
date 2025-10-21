import argparse
import csv
import pandas as pd
import regex as re

#####################
# Functions
#####################


def matchNameToAddress(name, dataFrame):
    for index, row in dataFrame.iterrows():
        if name in row[0]:
            return row[1]
    return "not found"


def matchNameToType(name, dataFrame):
    for index, row in dataFrame.iterrows():
        if name in row[1]:
            return row[0]
    return "not found"


def checkIfPresent(name, dataFrame):
    for index, row in dataFrame.iterrows():
        if name in row[1]:
            return True
    return False


def ReadStructReversed(key, sourceFile):
    sourceFile.seek(0)
    begin_struct = False
    csv_buffer = ""
    for line in reversed(list(sourceFile)):
        if key in line:
            begin_struct = True
            continue
        if begin_struct:
            if "{" in line:
                break
            elif "}" in line:
                continue
            # char arrays are not included because they don't work with pybind
            elif "char" in line and "[" in line:
                continue
            elif line == "\n":
                csv_buffer += "break here\n"
            else:
                for char in line:
                    if char == " ":
                        continue
                    else:
                        break
                csv_buffer += line.replace("\n", "").replace("\t", "").replace(
                    ",", "").replace("\r", "").replace(";", "") + "\n"
    csv_array = csv.reader(csv_buffer.splitlines(), delimiter=' ')
    csv_array = list(csv_array)
    csv_array.reverse()
    return csv_array


def ReadEnumReversed(key, sourceFile):
    sourceFile.seek(0)
    begin_enum = False
    csv_buffer = ""
    for line in reversed(list(sourceFile)):
        if key in line:
            begin_enum = True
            continue
        if begin_enum:
            if "{" in line:
                break
            elif line == "\n":
                csv_buffer += "break=here\n"
            else:
                csv_buffer += line.replace("\n", "").replace(" ", "").replace(
                    "\t", "").replace(",", "").replace("\r", "") + "\n"
    # invert the order of the lines
    csv_buffer = csv_buffer.splitlines()
    csv_buffer.reverse()
    csv_buffer = "\n".join(csv_buffer)
    csv_array = csv.reader(csv_buffer.splitlines(), delimiter='=')
    return csv_array

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


#####################
# Main
#####################

def main(args):
    parser = argparse.ArgumentParser(description='Generate registry table')

    parser.add_argument('-i', '--input', required=True,
                        help='Input header file to read registries from')
    parser.add_argument('-o', '--output', default="registry_table.html",
                        help='Output file to write to')

    args = parser.parse_args()

    readPath = args.input
    writePath = args.output

    sourceFile = open(readPath, "r")
    destination = open(writePath, "w+")

    # read the file and write the output
    csvArrayRW = ReadStructReversed("} regRW_st;", sourceFile)
    csvArrayRO = ReadStructReversed("} regRO_st;", sourceFile)
    csvArrayAddress = ReadEnumReversed("} Md80Reg_E;", sourceFile)

    sourceFile.close()

    dataFrameRW = pd.DataFrame(csvArrayRW)
    dataFrameRO = pd.DataFrame(csvArrayRO)
    dataFrameAddress = pd.DataFrame(csvArrayAddress)

    dataFrameCombinedRWO = pd.concat(
        [dataFrameRW, dataFrameRO], ignore_index=True)

    dataFrameTable = pd.DataFrame(
        columns=["reg name", "address", "read/write", "size", "limits", "description"])

    for name in dataFrameAddress[0]:
        dataFrameToConcat = pd.DataFrame(
            columns=["reg name", "address", "read/write", "size", "limits", "description"])
        if name != "break":
            dataFrameToConcat["reg name"] = [name]
            if checkIfPresent(name, dataFrameRW):
                dataFrameToConcat["read/write"] = "R/W"
                dataFrameToConcat["size"] = [matchNameToType(name, dataFrameRW)]
            elif checkIfPresent(name, dataFrameRO):
                dataFrameToConcat["read/write"] = "R/O"
                dataFrameToConcat["size"] = [matchNameToType(name, dataFrameRO)]
            else:
                dataFrameToConcat["read/write"] = "not found"
                dataFrameToConcat["size"] = "not found"
            dataFrameToConcat["address"] = [
                matchNameToAddress(name, dataFrameAddress)]
            dataFrameToConcat["limits"] = "-"
            dataFrameToConcat["description"] = "-"
            
        else:
            dataFrameToConcat["reg name"] = [""]
            dataFrameToConcat["address"] = [""]
            dataFrameToConcat["read/write"] = [""]
            dataFrameToConcat["size"] = [""]
            dataFrameToConcat["limits"] = [""]
            dataFrameToConcat["description"] = [""]
        dataFrameTable = pd.concat([dataFrameTable, dataFrameToConcat],ignore_index=True)

    with open(writePath, "a") as destination:
        html = dataFrameTable.to_html(classes="table",index=False,justify="center")
        print(dataFrameTable.to_markdown(index=False))
        html = re.sub(
            r'<table([^>]*)>',
            r'<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">',
            html
        )
        destination.write(html)

    print(bordered("\n  HTML table written to " + writePath + "     \n\n"))


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
