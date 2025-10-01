#include <stdio.h>
#include <stdlib.h>

#define MAX_ITEMS 1000

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int isDuplicate(int arr[], int size, int value) {
    for (int i = 0; i < size; i++)
        if (arr[i] == value)
            return 1;
    return 0;
}

int main() {
    int allItems[MAX_ITEMS], uniqueItems[MAX_ITEMS];
    int totalItems = 0, uniqueCount = 0;
    int sections, items, id;

    printf("Enter number of sections: ");
    scanf("%d", &sections);

    for (int s = 0; s < sections; s++) {
        printf("Enter number of items in Section %d: ", s + 1);
        scanf("%d", &items);
        printf("Enter item IDs for Section %d:\n", s + 1);
        for (int i = 0; i < items; i++) {
            scanf("%d", &id);
            allItems[totalItems++] = id;
        }
    }


    for (int i = 0; i < totalItems; i++) {
        if (!isDuplicate(uniqueItems, uniqueCount, allItems[i])) {
            uniqueItems[uniqueCount++] = allItems[i];
        }
    }


    qsort(uniqueItems, uniqueCount, sizeof(int), compare);


    printf("Final sorted item list:\n[");
    for (int i = 0; i < uniqueCount; i++) {
        printf("%d", uniqueItems[i]);
        if (i < uniqueCount - 1) printf(", ");
    }
    printf("]\n");

    return 0;
}
