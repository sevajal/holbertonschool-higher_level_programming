#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	unsigned int i, j;
	listint_t *current;
	listint_t *temp;

	current = list;
	temp = list->next;
	for (i = 0; current != NULL; i++)
	{
		for (j = 0; temp != NULL; j++)
		{
			if (temp->n == current->n)
				return (1);
			temp = temp->next;
		}
	current = current->next;
	}
	return (0);
}
