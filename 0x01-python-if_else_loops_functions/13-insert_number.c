#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the point to be inserted the number.
 * @number: int to be add into the sorted singly linked list.
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *previous, *current = *head;

	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;

	while (current)
	{
		if (number < current->n)
			break;
		previous = current;
		current = current->next;
	}

	new->next = current;
	if (current == *head)
		*head = new;
	else
		previous->next = new;
	return (new);
}
