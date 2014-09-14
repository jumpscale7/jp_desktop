def main(j,jp):
   
    #prepare the platform before copying the files

    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools

    
    execute=j.system.process.executeWithoutPipe
    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step

    print "enable system for 32 bit"
    cmd1="dpkg --add-architecture i386"
    execute(cmd1)

    print "update apt"
    cmd2="apt-get update"
    execute(cmd2)    

    print "install ia32 libs"
    cmd3="apt-get install libglib2.0-0:i386 libpng12-0:i386 libfontconfig1:i386 libfreetype6:i386 libglu1-mesa:i386 libcups2:i386 libx11-6:i386 libxmu6:i386 libxext6:i386 libxrender1:i386 libstdc++6:i386 libc6:i386 -y"
    execute(cmd3)

    print "install truetype fonts"
    cmd3="apt-get install ttf-mscorefonts-installer:i386 -y"
    execute(cmd3)

    print "should now be 32 bit"
    