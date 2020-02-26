import sys, os

def mk_dir():
    for i in range(1, 10):
        print(i)
        os.mkdir(os.path.join(os.getcwd(), '{}_{}'.format('dir', i)))


def rem_dir():
    for i in range(1, 10):
        print(i)
        os.rmdir(os.path.join(os.getcwd(), '{}_{}'.format('dir', i)))

    if __name__ == '__main__':
        mk_dir()
        rem_dir()