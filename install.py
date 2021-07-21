import os


def BuildTools():
    os.system('curl -z BuildTools.jar -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar')
    os.system('set /p Data=Enter the version (1.16.5, 1.17.1, etc) : || set Data=latest')
    os.system('java -jar BuildTools.jar --rev %Data%')

BuildTools()