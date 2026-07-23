from parser import Parser
import sys
import schedule
import subprocess

def main():




    p = Parser('db', 'https://www.worldometers.info/world-population/russia-population/')

    p.setup()
    front = subprocess.Popen([sys.executable, 'front.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             encoding="utf-8")

    schedule.every().day.at("12:00").do(p.parse)
    while True:
        line = front.stdout.readline()
        if "parse" in line:
            p.parse()
        schedule.run_pending()

        if front.poll()!=None:
            sys.exit(0)


if __name__ == "__main__":
    main()

