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
	listint_t *new, *tmp = *head;

	if (head)
	{
		while (number > tmp->next->n)
		{
			tmp = tmp->next;
		}
		new = (listint_t *)malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = tmp->next;
		tmp->next = new;
		return (new);
	}
	return (NULL);
}
