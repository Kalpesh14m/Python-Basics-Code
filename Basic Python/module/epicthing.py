#if name == main asks whether or not the script is the "main" running script, or if that script is just being referenced by another script.
#Whenever you import other people's code, they usually have these there, so that, when you import them, their code doesn't just automatically run.

# modules are just Python scripts that are stored in your Lib or Lib/site-packages folder, or local to the script being run.


def epic():
    print("This is great!, Woowwww....")

if __name__ == '__main__':
    print('such great module!!!!')

