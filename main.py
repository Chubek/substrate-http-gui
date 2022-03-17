import gui
import cli
import sys



if __name__ == "__main__":
    if sys.argv[1].lower() == "gui":
        print("GUI Initiated...")
        gui.render_gui()