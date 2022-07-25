#include <stdio.h>
#include <stdlib.h>
#define BUFFER_SIZE 5000

int main() {
    FILE * src;
    FILE * backup;
    char buffer[BUFFER_SIZE];

    src = fopen("./log/ledger.csv", "w");
    backup = fopen("./log/backup/backup0.csv", "r");
    if (src == NULL) {
        printf("Unable to open log file.\n");
        exit(EXIT_FAILURE);
    }
    if (backup == NULL) {
        printf("Unable to open backup file.\n");
        exit(EXIT_FAILURE);
    }
    for (; (fgets(buffer, BUFFER_SIZE, backup)) != NULL; fputs(buffer, src));
    fclose(src);
    fclose(backup);
    return 0;
}