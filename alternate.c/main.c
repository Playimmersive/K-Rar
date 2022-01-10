#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include "main.h"

/*************
 * GAME LOOP *
 *************/

int rnd(int length) {
    return random() % length;
}

int main() {
    clear();
    screen_intro();
    while (1) {
        screen_room();
        do_events();
        user_input();
        if (quit) break;
    }
    screen_exit();
    return 0;
}
