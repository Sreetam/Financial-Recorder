#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define BUFFER_SIZE 5000
#define BUFFER 125

typedef struct recrd {
    int timestamp;
    char datetime[BUFFER];
    float amount;
    char category[BUFFER];
    int catcode;
    char description[BUFFER_SIZE];
} record;

record * getrecord();
void putrecord(record *);
void fputrecord(FILE *, record *);

int main(int argc, char **argv) {
    FILE *fptr;

    // use appropriate location if you are using MacOS or Linux
    fptr = fopen("./log/ledger.csv","a");

    if(fptr == NULL) {
        printf("Unable to open file.\n");
        exit(EXIT_FAILURE);
    }
    
    fputrecord(fptr, getrecord());

    fclose(fptr);

    return 0;
}

record * getrecord() {
    record * line = (record *) (calloc(1, sizeof(record)));
    time_t now;
    char choice;
    printf("Amount? ");
    scanf("%f", &(line -> amount));
    printf("CatCode 0F 1G 2FM 3T 4TR 5E 6R 7I 8L 9O? ");
    scanf("\n%d", &(line -> catcode));
    printf("Description? ");
    choice = getc(stdin);choice = getc(stdin);
    if(choice=='\n') {
        strcpy(line->description, "");
    }
    else {
        scanf("\n%[^\n]%*c", line -> description);
    }

    //processing
    switch (line->catcode) {
    case 0:
        strcpy(line->category, "Food");
        break;
    case 1:
        strcpy(line->category, "Groceries");
        break;
    case 2:
        strcpy(line->category, "FMCG");
        break;
    case 3:
        strcpy(line->category, "Telecom");
        break;
    case 4:
        strcpy(line->category, "Transport");
        break;
    case 5:
        strcpy(line->category, "Energy");
        break;
    case 6:
        strcpy(line->category, "Rent");
        break;
    case 7:
        strcpy(line->category, "Investments");
        break;
    case 8:
        strcpy(line->category, "Loans");
        break;
    default:
        strcpy(line->category, "Others");
        break;
    }
    line->timestamp = (int)time(&now);
    strftime((line->datetime), (sizeof(char) * BUFFER), "%Y-%m-%d %H:%M:%S", localtime(&now));
    return line;
}

void fputrecord(FILE *fptr, record *line){
    fprintf(fptr,"%d,%s,%0.2f,%s,%d,\"%s\"\n", line->timestamp, line->datetime, line->amount, line->category, line->catcode, line->description);
}

void putrecord(record *line){
    printf("%d,%s,%0.2f,%s,%d,\"%s\"\n", line->timestamp, line->datetime, line->amount, line->category, line->catcode, line->description);
}