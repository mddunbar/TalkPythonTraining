import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------')
    print('     JOURNAL APP')
    print('----------------------')


def run_event_loop():

    print('What do you want to do with your journal?')
    cmd = 'Empty'
    journal_name = 'default'
    journal_data = journal.load(journal_name) # [] # list()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it:')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd !='x' and cmd:
            print("Sorry, we don't undertand '{}'".format(cmd))

    print('Goodbye')
    journal.save(journal_name, journal_data)

def list_entries(data):
    print('Your Journal Entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('[{}] {}'.format(idx + 1, entry))

def add_entries(journal_data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, journal_data)
    # data.append(text)

if __name__ == "__main__":
    main()
