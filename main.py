from util.plugins.update import search_for_updates
from util.plugins.setup import setup
from util.plugins.utils import *

def main():
    setup()


if __name__ == "__main__":
    main()
    # import sys
    # setTitle("@TIO Premium Loading...")
    
    # System.Size(120, 30)
    # Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, time=1)
    # if not os.path.exists("output"):
    #     os.makedirs("output", exist_ok=True)
    # if os.path.exists("output/QR-Code"):
    #     shutil.rmtree(f"output/QR-Code")
    # os.system("""if not exist "util/chromedriver.exe" echo [#] Downloading chromedriver: """)
    # os.system("""if not exist "util/chromedriver.exe" curl -#fkLo "util/chromedriver.exe" "https://github.com/AstraaDev/complement/raw/main/chromedriver.exe" """)
    # if os.path.basename(sys.argv[0]).endswith("exe"):
    #     search_for_updates()
    #     if not os.path.exists(getTempDir()+"\\atio_proxies"):
    #         proxy_scrape()
    #     clear()
    #     main()
    # try:
    #     assert sys.version_info >= (3,9)
    # except AssertionError:
    #     input(f"{y}[{Fore.RED}#{y}]{w} Sorry but, your python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with @TIO, please download python 3.9 or higher.")
    #     sys.exit()
    # else:
    #     search_for_updates()
    #     if not os.path.exists(getTempDir()+"\\atio_proxies"):
    #         proxy_scrape()
    #     clear()
    #     main()