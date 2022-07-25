#include <stdio.h>
#include <stdlib.h>
#define BUFFER_SIZE 5000

int main() {
    FILE *src;
    char c;
    char buffer[BUFFER_SIZE];
  
    // Open file
    src = fopen("./desc/manual.txt", "r");
    if (src == NULL) {
        printf("Unable to open file.\n");
        exit(EXIT_FAILURE);
    }
    
    // Read contents from file
    for(; (fgets(buffer, BUFFER_SIZE, src)) != NULL; printf("%s", buffer));
    fclose(src);
    return 0;
}