import os


def clean_numerical_names():
    for i in sorted(os.listdir(os.getcwd())):
        name = os.path.splitext(i)[0]
        filetype = os.path.splitext(i)[1] if len(os.path.splitext(i)[1]) > 0 else "0"
        if name.isdigit() and filetype != "0" :
            os.rename(i, "zzzz" + i)


def main():
    clean_numerical_names()
    counter = 1
    for i in sorted(os.listdir(os.getcwd())):
        name = os.path.splitext(i)[0]
        filetype = os.path.splitext(i)[1]
        if filetype == ".mp3":
            os.rename(i, str(counter) + filetype)
            counter += 1


main()
