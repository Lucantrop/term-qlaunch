import sys, getopt
import csv, subprocess

def launch(launch_list):
    for i in range(1, len(launch_list)):
        print('%d. %s\n' % (i, ' '.join(launch_list[i])))
        subprocess.call(' '.join(launch_list[i]).lstrip(' ').rstrip(' ').split(' '))

def parse(infile):
    reader = csv.reader(infile)

    for program, root, options in reader:
        yield [('sudo' if root=='1' else ''), program, options]

def main(argv):
    inputfile= ''
    try:
        opts, args = getopt.getopt(argv, "i:h", ["input-file="])
    except getopt.GetoptError:
        print('qlaunch.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('qlaunch.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--input-file"):
            inputfile = arg

    print(inputfile)
    with open(inputfile, "r") as infile:
        launch_list = list(parse(infile))

    launch(launch_list)

if __name__ == '__main__':
    main(sys.argv[1:])
