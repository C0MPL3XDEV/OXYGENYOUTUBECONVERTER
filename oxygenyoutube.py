import pytube, time
from rich.console import Console
console = Console()
def title():

    console.print('[bold red] ██████╗ ██╗  ██╗██╗   ██╗ ██████╗ ███████╗███╗   ██╗██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗')
    console.print('[bold red]██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔════╝ ██╔════╝████╗  ██║╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝')
    console.print('[bold red]██║   ██║ ╚███╔╝  ╚████╔╝ ██║  ███╗█████╗  ██╔██╗ ██║ ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗  ')
    console.print('[bold red]██║   ██║ ██╔██╗   ╚██╔╝  ██║   ██║██╔══╝  ██║╚██╗██║  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  ')
    console.print('[bold red]╚██████╔╝██╔╝ ██╗   ██║   ╚██████╔╝███████╗██║ ╚████║   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗')
    console.print('[bold red] ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝')
                                                                                                                  
title()
url = console.input('[red][ * ] ENTER URL: ')
directory = console.input('[blue][ * ] ENTER THE DIRECTORY: ')

time.sleep(0.5)
console.print('[red][ * ] I AM DOWNLOADING THE VIDEO ...')

youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download(directory)
time.sleep(0.5)
console.print('[violet][ * ] DOWNLOAD COMPLETED ;)')

def closedtitle():

    time.sleep(0.5)
    console.print('[bold red] ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██████╗     ██████╗ ██╗   ██╗     ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ██████╗ ██╗  ██╗')
    console.print('[bold red]██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ██╔════╝██╔═████╗████╗ ████║██╔══██╗██║     ╚════██╗╚██╗██╔╝')
    console.print('[bold red]██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║  ██║    ██████╔╝ ╚████╔╝     ██║     ██║██╔██║██╔████╔██║██████╔╝██║      █████╔╝ ╚███╔╝ ')
    console.print('[bold red]██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝      ██║     ████╔╝██║██║╚██╔╝██║██╔═══╝ ██║      ╚═══██╗ ██╔██╗ ')
    console.print('[bold red]╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██████╔╝    ██████╔╝   ██║       ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗██████╔╝██╔╝ ██╗')
    console.print('[bold red] ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝     ╚═════╝    ╚═╝        ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚═════╝ ╚═╝  ╚═╝')
                                                                                                                                              
closedtitle()