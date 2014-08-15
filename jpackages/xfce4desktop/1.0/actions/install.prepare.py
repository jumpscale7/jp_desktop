def main(j,jp):
   
    #prepare the platform before copying the files
    j.system.platform.ubuntu.install("aptitude")

    # # #remove gnome first
    # do=j.system.installtools
    # do.execute("aptitude purge `dpkg --get-selections | grep gnome | cut -f 1` -y")
    # do.execute("aptitude -f install -y")
    # do.execute("aptitude purge `dpkg --get-selections | grep deinstall | cut -f 1` -y")
    # do.execute("aptitude -f install -y")

    # can happen by e.g. installing a debian package e.g. by
    names=["xfce4","xfce4-terminal","scribus","firefox","gimp","tuxcmd","pidgin","evince","gnucash","inkscape","evolution"]
    for packagename in names:
        j.system.platform.ubuntu.install(packagename)


    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step
    
    pass


