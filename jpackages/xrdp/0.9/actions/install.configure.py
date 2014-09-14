def main(j,jp):
   
    #configure the package 

    ini=j.tools.inifile.open("/etc/xrdp/xrdp.ini")
    ini.setParam("xrdp1","password",j.application.config.get("system.superadmin.passwd"))
    ini.setParam("xrdp1","username","root")

    pass
    
