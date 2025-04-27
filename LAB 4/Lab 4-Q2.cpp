#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

void append(Node** head_ref, int new_data) {
    Node* new_node = createNode(new_data);
    
    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }
    
    Node* last = *head_ref;
    while (last->next != NULL) {
        last = last->next;
    }
    
    last->next = new_node;
}

void removeDuplicates(Node* head) {
    Node* current = head;
    Node* prev = NULL;
    Node* temp = NULL;
    
    while (current != NULL && current->next != NULL) {
        prev = current;
        temp = current->next;
        
        while (temp != NULL) {
            if (current->data == temp->data) {
                prev->next = temp->next;
                free(temp);
                temp = prev->next;
            } else {
                prev = temp;
                temp = temp->next;
            }
        }
        current = current->next;
    }
}

void printList(Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    Node* head = NULL;
    int n, data;

    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    printf("Enter the elements of the linked list:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &data);
        append(&head, data);
    }

    printf("Original list: ");
    printList(head);

    removeDuplicates(head);

    printf("List after removing duplicates: ");
    printList(head);

    return 0;
}

