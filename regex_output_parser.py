def parse_mpp_output_allg(paramlist, output=None, logfile="mpp/build/log/log"):
    '''
    :param paramlist:
    :param output:
    :return:list of list of outputvalues
    '''
    out = []
    if output is None:
        # logfile = "mpp/build/log/log"
        with open(logfile) as file:
            lines = file.readlines()
    else:
        lines = output
    for param in paramlist:
        out.append([])
        for line in lines:
            if "Step" in line and not "default" in line and not "reading" in line:
                regex = r"[+-]?[0-9]+[.]?[0-9]*[eE]?[+-]?[0-9]*"
                if param in line:
                    tmp = line.split(param)[1]
                    value = float(re.findall(regex, tmp)[0])
                    # print(value)
                else:
                    value = 0
                out[paramlist.index(param)].append(value)
    return out
