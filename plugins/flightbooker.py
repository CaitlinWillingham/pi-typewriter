import curses

name = "Flight Booker"

def run(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "✈ Welcome to Pretend Airlines!\n")
    stdscr.addstr(1, 0, "Where would you like to go? ")
    stdscr.refresh()
    curses.echo()
    dest = stdscr.getstr(2, 0, 20).decode('utf-8')

    stdscr.addstr(4, 0, f"Booking your flight to {dest}... ✈ Done!\n")
    stdscr.refresh()
    curses.noecho()