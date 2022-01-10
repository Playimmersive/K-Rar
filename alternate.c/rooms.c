/*****************
 * RAUM ROUTINEN *
 *****************/

struct {
    char* name;
    
} rooms[_ROOMS] = {0};



void screen_intro() {
    slow_print("Hallo willkommen zur Welt von K^rar");
    user_option("enter", "start game", 1);
}

void screen_epilog(int death) {
    switch (death) {
        case 0:
            printf("There are no monsters left. Congratulations, you are the true hero of K^rar.");
            break;
        default:
            printf("You died. Restart and try again.");
    }
    printf(_NEWLINE);
}

void screen_exit() {
    
}

void screen_room() {
    
}
