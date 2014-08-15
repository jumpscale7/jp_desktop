def main(j,jp):
   
    #prepare the platform before copying the files

    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    do=j.system.installtools

    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step

    cmd1="dpkg --add-architecture i386"
    do.execute(cmd1)

    # cmd2="apt-get update"
    # do.execute(cmd2)

    cmd3="apt-get install libx11-6:i386 libxmu6:i386 libxext6:i386 libxrender1:i386 libstdc++6:i386 libc6:i386 -y"
    do.execute(cmd3)
    