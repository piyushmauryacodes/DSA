def wipe_out():
    filename=f"02_Highscore.txt"
    with  open(filename,"w") as f:
        f.write("")
        print(f"{filename} is successfully Wiped Out!")


wipe_out()