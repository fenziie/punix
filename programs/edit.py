
import os
import curses

def executeEdit(args):
    if len(args) == 2:
        # Build the full file path within the "filesystem" directory
        file_path = os.path.join('filesystem', args[1])
        edit(file_path)
    else:
        print(f"err: too little or too many args. expected 1, got {len(args)}")

def edit(file_path):
    if not os.path.exists(file_path):
        print("err: file doesn't exist")
        return  # Exit from the edit function and return to the main program

    def start_editing(stdscr):
        # Initialize curses and enable color support
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green text on black background
        stdscr.attron(curses.color_pair(1))  # Apply the green color pair
        
        # Clear screen
        stdscr.clear()

        # Read the content of the file, removing any \r (carriage return) characters
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            lines = [line.replace('\r', '') for line in f.readlines()]

        # If the file is empty, initialize it with one empty line
        if not lines:
            lines.append("")  # Add one empty line if the file is empty

        # Initialize cursor position at the end of the last line
        current_line = len(lines) - 1  # Start at the last line
        current_pos = len(lines[current_line]) if lines else 0  # Position at the end of the last line, or at the start if no lines

        # Display lines with line number for reference
        def display_lines():
            stdscr.clear()
            for i, line in enumerate(lines):
                stdscr.addstr(i, 0, line)
            stdscr.move(current_line, current_pos)

        # Display initial lines
        display_lines()

        while True:
            key = stdscr.getch()

            if key == 27:  # ESC key to finish editing
                stdscr.clear()
                stdscr.addstr(0, 0, "1. Save\n2. Discard\n3. Restart\nChoose option: ")
                stdscr.refresh()
                option = stdscr.getch()
                if option == ord('1'):  # Save
                    with open(file_path, 'w', newline='', encoding='utf-8') as f:
                        for line in lines:
                            f.write(line + '\n')  # Ensure Unix-style newlines
                    break
                elif option == ord('2'):  # Discard
                    break
                elif option == ord('3'):  # Restart
                    start_editing(stdscr)  # Recursively restart editing
                    break
                else:
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Invalid option. Press ESC to quit editing.")
                    stdscr.refresh()

            elif key == curses.KEY_BACKSPACE or key == 127:  # Backspace
                if current_pos > 0:
                    # Delete character before the cursor in the current line
                    lines[current_line] = lines[current_line][:current_pos - 1] + lines[current_line][current_pos:]
                    current_pos -= 1
                elif current_line > 0:
                    # If we're at the start of a line, merge with the previous line
                    lines[current_line - 1] += lines[current_line]
                    del lines[current_line]
                    current_line -= 1
                    current_pos = len(lines[current_line])
                elif current_line == len(lines) and len(lines) > 0:  # Handle empty lines correctly at the end
                    # When there's no content, prevent index error by ensuring valid lines
                    lines.append("")  # Add a new empty line if none exists at the end
                    current_pos = 0  # Move the cursor to the start of the new line
                display_lines()

            elif key == curses.KEY_UP:  # Arrow Up
                if current_line > 0:
                    current_line -= 1
                    current_pos = len(lines[current_line])  # move to the end of the previous line
                display_lines()

            elif key == curses.KEY_DOWN:  # Arrow Down
                if current_line < len(lines) - 1:
                    current_line += 1
                    current_pos = len(lines[current_line])  # move to the end of the next line
                display_lines()

            elif key == curses.KEY_LEFT:  # Arrow Left
                if current_pos > 0:
                    current_pos -= 1
                display_lines()

            elif key == curses.KEY_RIGHT:  # Arrow Right
                if current_pos < len(lines[current_line]):
                    current_pos += 1
                display_lines()

            elif key == 10:  # Enter key (Newline)
                # If the current line is empty, create a new one at the current line position
                if current_line == len(lines):
                    lines.append("")
                # Split the line at the current position
                lines.insert(current_line + 1, lines[current_line][current_pos:])
                lines[current_line] = lines[current_line][:current_pos]
                current_line += 1
                current_pos = 0
                display_lines()

            elif key == 9:  # Tab key (Indentation, optional)
                lines[current_line] = lines[current_line][:current_pos] + '    ' + lines[current_line][current_pos:]
                current_pos += 4  # Move cursor forward by 4 spaces
                display_lines()

            elif key >= 32 and key <= 126:  # Any printable character
                if current_line == len(lines):
                    lines.append("")  # Add a new line if we're at the end
                lines[current_line] = lines[current_line][:current_pos] + chr(key) + lines[current_line][current_pos:]
                current_pos += 1
                display_lines()

        # Turn off the green color at the end of editing
        stdscr.attroff(curses.color_pair(1))

    # Initialize curses screen and start editing
    curses.wrapper(start_editing)
