# Module Imports
from sys import platform as sys_platform, exit as sys_exit
from os import system as os_system, getcwd as os_getcwd
from configparser import ConfigParser
from screeninfo import get_monitors as screeninfo_get_monitors


# Classes
_c = ConfigParser()
class config:
   class screen:
      def _res():
         res = []
         for monitor in screeninfo_get_monitors():
            res.append(min(monitor.width,monitor.height))
         return min(res)
      res = _res()

   path = os_getcwd()
   _c.read(f'{path}\\config.ini')

   class button:
      close = _c['CONFIG']['close_program']

   class wireless:
      ip = _c['CONFIG']['DEVICE_IP']
      port = _c['CONFIG']['PORT']

   class version:
      scrcpy = _c['CONFIG']['SCRCPY_VERSION']
      adb = _c['CONFIG']['ADB_VERSION']

   if sys_platform.lower() == 'win32': _clear = 'cls'
   elif sys_platform.lower() == 'cygwin': _clear = 'echo -e "\033c"' # I'm using google to find the clear commands for these platforms, and it seems cygwin doesn't have a clear command unless you install "ncurses", but it seems like this works for people.
   #elif sys_platform.lower() in ['linux','linux2','darwin','msys','freebsd7','freebsd8','freebsdn']: _clear = 'clear'
   else: _clear = 'clear'


class cmds:
   def fullscreen(): return ' --f',
   def borderless(): return ' --window-borderless'
   def stay_awake(): return ' -w'
   def max_size(value:int=config.screen.res): return f'-m {value}'



# Functions
def _clear(fail:bool=False):
   os_system(config._clear)
   if fail == True: print('That input was not recognized, please try again. ')
   return


def close():
   sys_exit()


def main():
   fullscreen = ''
   borderless = ''
   stay_awake = ''
   max_size = 800

   _clear()
   while True:
      i = input('Fullscreen Window [Y/N] (N): ')
      if len(i) == 0 or i == 'n': break
      elif i.lower() == 'y':
         fullscreen = cmds.fullscreen()
         break
      else: _clear(True)

   _clear()
   while True:
      i = input('Borderless Window [Y/N] (N): ')
      if i.lower() == 'y':
         borderless = cmds.borderless()
         break
      elif (len(i) == 0) or (i == 'n'): break
      _clear(True)

   _clear()
   while True:
      i = input('Keep Phone Screen On [Y/N] (N): ')
      if i.lower() == 'y':
         stay_awake = cmds.stay_awake()
         break
      elif (len(i) == 0) or (i == 'n'): break
      _clear(True)

   _clear()
   while True:
      i = input(f'Max Resolution ({config.screen.res}): ')
      if i.isnumeric() == True: max_size = cmds.max_size(i)
      elif len(i) == 0: max_size = cmds.max_size()
      else:
         _clear(True);
         continue
      break
   _clear()


   try: os_system(f'"{config.path}\\include\\{config.version.adb}\\adb.exe" tcpip {config.wireless.port}')
   except: pass

   try: os_system(f'"{config.path}\\include\\{config.version.adb}\\adb.exe" connect {config.wireless.ip}:{config.wireless.port}')
   except: pass

   try: os_system(f'"{config.path}\\include\\{config.version.scrcpy}\\scrcpy.exe" {max_size}{fullscreen}{borderless}{stay_awake}')
   except Exception as error: print(error)



#-
main()

