int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}



struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    int* values = (int*)malloc(sizeof(int) * 10000); // assuming a max of 10,000 nodes
    int count = 0;

    // Collect all values from the k linked lists
    for (int i = 0; i < listsSize; i++) {
        struct ListNode* current = lists[i];
        while (current != NULL) {
            values[count++] = current->val;
            current = current->next;
        }
    }

    if (count == 0) {
        free(values);
        return NULL;
    }

    // Sort the collected values
    qsort(values, count, sizeof(int), compare);

    // Build the sorted linked list
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->val = values[0];
    head->next = NULL;
    struct ListNode* tail = head;

    for (int i = 1; i < count; i++) {
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = values[i];
        node->next = NULL;
        tail->next = node;
        tail = node;
    }

    free(values);
    return head;
}