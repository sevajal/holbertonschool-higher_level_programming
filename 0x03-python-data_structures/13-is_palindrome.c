#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	unsigned int i, nodes;
	const listint_t *forward = *head;
	const listint_t *back = *head;

	nodes = 0;
	while (forward != NULL)
	{
		forward = forward->next;
		nodes++;
	}
	nodes--;
	forward = *head;

	if (nodes < 2)
		return (1);

	if (nodes == 2)
	{
		if (forward->n == forward->next->n)
			return (1);
		else
			return (0);
	}

	if (nodes > 2)
	{
		while (nodes)
		{
			for (i = 0; i < nodes; i++)
				back = back->next;
			if (forward->n != back->n)
				return (0);
			forward = forward->next;
			back = *head;
			nodes--;
		}
	}
	return (1);
}
