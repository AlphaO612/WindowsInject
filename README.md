# WindowsInject
This app add in Manages scheduled tasks your task in autolaunch!
# How use it
if you wanna install(add) in schtasks, write it, but change <name> and <way>:
```sh
inject.exe -set -n name -w way
```
if you wanna delete task, write it, but change <name>:
```sh
ingect.exe -del -n name
```
 For example:
```sh
ingect.exe -set -n TestName -w C:\ProgramFiles\TestApp\example.exe
```
```sh
ingect.exe -del -n TestName
```
