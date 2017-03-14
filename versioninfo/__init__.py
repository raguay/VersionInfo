import sys, fman

class VersionInfo(fman.DirectoryPaneCommand):
    def __call__(self):
        fmanVer = "unknown"
        try:
            fmanVer = fman.FMAN_VERSION
        except:
            fmanVer = "unknown"
        apiVer = "unknown"
        try:
            apiVer = fman.API_VERSION
        except:
            apiVer = "unknown"
        outStr = "fman Version:\t{0}\n".format(fmanVer)
        outStr += "fman Api Version:\t{0}\n".format(apiVer)
        outStr += "Python Version:\t{0}.{1}.{2}\n".format(sys.version_info[0], sys.version_info[1], sys.version_info[2])
        fman.show_alert(outStr)
