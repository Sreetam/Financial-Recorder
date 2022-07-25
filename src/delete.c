#include <stdio.h>
#include <stdlib.h>
#define BUFFER_SIZE 5000

int main() {
    FILE *src;
    FILE *temp;
    int line = 0;
    char buffer[BUFFER_SIZE];

    src = fopen("./log/ledger.csv", "r");
    temp = fopen("./log/delete.tmp", "w");
    if (src == NULL || temp == NULL) {
        printf("Unable to open file.\n");
        exit(EXIT_FAILURE);
    }
    // Delete given line from file.
    for(line = 0; (fgets(buffer, BUFFER_SIZE, src)) != NULL; line++);
    rewind(src);
    for (int i = 0; i<line-1 && (fgets(buffer, BUFFER_SIZE, src)) != NULL; fputs(buffer, temp), i++);
    /* Close all open files */
    fclose(src);
    fclose(temp);
    /* Delete src file and rename temp file as src */
    remove("./log/ledger.csv");
    rename("./log/delete.tmp", "./log/ledger.csv");
    return 0;
}