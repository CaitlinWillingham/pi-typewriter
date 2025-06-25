# main.py
import curses
import plugins

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    plugin_list = plugins.load_plugins()

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "TYPEWRITER - Choose an app:\n")
        for i, plugin in enumerate(plugin_list):
            stdscr.addstr(i + 1, 0, f"{i+1}. {plugin.name}")
        stdscr.addstr(len(plugin_list) + 2, 0, "Q. Quit")

        stdscr.refresh()
        key = stdscr.getkey()

        if key.lower() == 'q':
            break
        if key.isdigit():
            idx = int(key) - 1
            if 0 <= idx < len(plugin_list):
                stdscr.clear()
                plugin_list[idx].run(stdscr)
                stdscr.addstr("\nPress any key to return...")
                stdscr.getkey()

if __name__ == '__main__':
    curses.wrapper(main)
