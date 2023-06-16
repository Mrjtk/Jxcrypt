import colorama
colorama.init(autoreset=True)
banner=(colorama.Fore.GREEN+'''  OooOoo                                      
      O                                       
      o                                   O   
      O                                  oOo  
      o  o   O .oOo  `OoOo. O   o .oOo.   o   
      O   OoO  O      o     o   O O   o   O   
O     o   o o  o      O     O   o o   O   o   
`OooOO'  O   O `OoO'  o     `OoOO oOoO'   `oO 
                                o O                version= 0.1
                             OoO' o'               Made by Jatin
                                                   ''')
print(banner)

name=input(colorama.Fore.YELLOW+colorama.Style.BRIGHT+"[=] Enter the string :")

string=''
for i in name:
                a=(ord(i))
                b=a+2
                c=b-5
                d=(chr(c))
                string+=d
print(colorama.Fore.YELLOW+"[+] The hashed value is :-> "+colorama.Style.BRIGHT+colorama.Fore.RED+string)
          
                
