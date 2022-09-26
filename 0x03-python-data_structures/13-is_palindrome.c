#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
    int i;
    int list_length = 0;
    listint_t *move, *last, *prev;
    move = *head;
    last = *head;

    while (move != NULL)
    {
        list_length++;

        if (move->next == NULL)
        {
            last = move;
        }

        move = move->next;
    }

    move = *head;

    for (i = 0; i < list_length/2; i++)
    {
        if (move == last)
        {
            move = move->next;
            last = 
        }
    }
}
