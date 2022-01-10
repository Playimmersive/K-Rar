/****************************
 * DEFINITIONEN UND GLOBALS *
 ****************************/

#ifdef linux
  #define _NEWLINE "\n"
  #define _CLEAR "clear"
#elif _WIN32 || WIN32
  #define _NEWLINE "\r\n"
  #define _CLEAR "cls"
#else
  #define _NEWLINE "\r"
  #define _CLEAR "clear"
#endif

#define _ROOMS 10
#define _USER_OPTIONS 30

void slow_print(char*);
void do_events();
int rnd(int);
void user_option(char*, char*, int);

const int typing_speed = 20;

int quit = 0;
int current_room = 0;

#include "rooms.c"
#include "weapons.c"
#include "chars.c"
#include "events.c"
#include "gui.c"
