#include <stdio.h>
#include <stdlib.h>
#define BUFFER_SIZE 5000

int main() {
    FILE * src;
    FILE * backup;
    int line = 0;
    char buffer[BUFFER_SIZE];
    char filename[60];
    char destination[60];

    src = fopen("./log/ledger.csv", "r");
    backup = fopen("./log/temp", "w");
    if (src == NULL) {
        printf("Unable to open log file.\n");
        exit(EXIT_FAILURE);
    }
    if (backup == NULL) {
        printf("Unable to open temp file.\n");
        exit(EXIT_FAILURE);
    }
    
    remove("./log/backup/backup9.csv");
    for (int i = 8; i >= 0; i--) {
        snprintf(filename, 60, "./log/backup/backup%d.csv", i);
        snprintf(destination, 60, "./log/backup/backup%d.csv", i+1);
        rename(filename, destination);
    }
    for (; (fgets(buffer, BUFFER_SIZE, src)) != NULL; fputs(buffer, backup));
    fclose(src);
    fclose(backup);
    rename("./log/temp", "./log/backup/backup0.csv");
    return 0;
}