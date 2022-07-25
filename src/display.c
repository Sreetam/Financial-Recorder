#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#define BUFFER_SIZE 5000

int main(int argc, char **argv) {
    int entries = 5;
    if (argc>1) {
        entries = atoi(argv[1]);
    }
    
    FILE *src;
    int line = 0;
    char buffer[BUFFER_SIZE];

    src = fopen("./log/ledger.csv", "r");
    if (src == NULL) {
        printf("Unable to open file.\n");
        exit(EXIT_FAILURE);
    }
    // Delete given line from file.
    for(line = 0; (fgets(buffer, BUFFER_SIZE, src)) != NULL; line++);
    rewind(src);
    if (line<entries) {
        entries = line;
    }
    line = line - entries;
    
    for (int i = 0; (fgets(buffer, BUFFER_SIZE, src)) != NULL; i++) {
        if (i>=line) {
            printf("%s",buffer);
        }
    }
    /* Close all open files */
    fclose(src);
    return 0;
}