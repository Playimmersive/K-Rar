/*****************************
 * BENUTZER EIN UND AUSGABEN *
 *****************************/

struct {
    char* cmd;
    char* text;
    int room;
} user_options[_USER_OPTIONS] = {0};



void clear() {
    system(_CLEAR);
}

void slow_print(char* text) {
    int usec = 0.5 * 1000000 / typing_speed;
    char c;
    while (c = *text++) {
        printf("%c", c);
        fflush(stdout); 
        usleep(usec * (rnd(3) + 1));
    }
    printf(_NEWLINE);
}


void user_option(char* cmd, char* text, int room) {
    int i;
    for (i=0; i<_USER_OPTIONS; i++) {
        if (user_options[i].cmd == 0) {
            user_options[i].cmd = cmd;
            user_options[i].text = text;
            user_options[i].room = room;
            if (++i != _USER_OPTIONS) user_options[i].cmd = 0;
            break;
        }
    }
}

void user_input() {
    int i;
    char s[81];
    printf("Choose your next action:%s", _NEWLINE);
    for (i=0; i<_USER_OPTIONS; i++) {
        if (user_options[i].cmd == 0) break;
        printf("    Type '%s' for %s", user_options[i].cmd, user_options[i].text);
        printf(_NEWLINE);
    }
    printf(_NEWLINE);
    while (1) {
        printf(">");
        scanf("%80s", &s);
        if (!strcmp(s, "exit")) {
            quit = 1;
            return;
        }
        for (i=0; i<_USER_OPTIONS; i++) {
            if (user_options[i].cmd == 0) break;
            if (!strcmp(s, user_options[i].cmd)) {
                current_room = user_options[i].room;
                user_options[0].cmd = 0;
                return;
            }
        }
    }
}
