import colorama
banner=(colorama.Fore.GREEN+'''  OooOoo                                      
      O                                       
      o                                   O   
      O                                  oOo  
      o  o   O .oOo  `OoOo. O   o .oOo.   o   
      O   OoO  O      o     o   O O   o   O   
O     o   o o  o      O     O   o o   O   o   
`OooOO'  O   O `OoO'  o     `OoOO oOoO'   `oO      Decoder
                                o O                version= 0.1
                             OoO' o'               Made by Jatin''')
print(banner)
a=input(colorama.Fore.YELLOW+colorama.Style.BRIGHT+"Enter to decode :")
string=''
for i in a:
                a=(ord(i))
                b=a+3
                d=(chr(b))
                string+=d
print(colorama.Fore.YELLOW+colorama.Style.BRIGHT+"The encoded value is -> "+colorama.Fore.BLUE+colorama.Style.BRIGHT+string)