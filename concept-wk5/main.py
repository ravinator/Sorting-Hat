# -----------------------------
# Imported modules & libraries
# -----------------------------


import textwrap;


# -----------------------------
# Defining functions
# -----------------------------


def retrieve():
    file = open("q_and_a.txt", "r");
    lines = file.readline();
    line_count = 0;
    q_and_a = {};

    while lines:
        q_and_a[line_count] = [x.strip() for x in lines.split(',')];
        lines = file.readline();
        line_count += 1;

    file.close();
    return(q_and_a);


def question_and_answer(dict):
    usr_answers = open("usr_answers.txt", "w");

    for x in dict:
        print(textwrap.dedent(f"""
        --------
        Question {dict[x][0]}
        --------
        a) {dict[x][1]}
        b) {dict[x][2]}
        c) {dict[x][3]}
        d) {dict[x][4]}
        """));

        usr_input = input("Your answer: ");
        usr_answers.write(f"{x}: {usr_input}\n");

    usr_answers.close();
    print("\n!!! This was the end of the questionnaire !!!");


def main():
    while True:
        print(textwrap.dedent("""
        ------
        Options
        ------
        1: Begin the questionnaire
        2: Answers of last test
        q: Quit the program
        """));

        usr_input = input(str("Kies uw optie: "))
        if usr_input == 'q':
            quit();
        elif usr_input == '1':
            question_and_answer(retrieve());
        elif usr_input == '2':
            usr_answers = open("usr_answers.txt", "r");
            for x in usr_answers:
                print(x, end='');
            usr_answers.close();
        else:
            print("You made an invalid selection. Please try again!");


# -----------------------------
# Calling defined function(s)
# -----------------------------


main();
