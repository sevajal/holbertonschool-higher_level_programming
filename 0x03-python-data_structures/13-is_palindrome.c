#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	unsigned int i = 0, nodes = 0, half;
	const listint_t *forward = *head;
	const listint_t *back;
	const listint_t *half_head = *head;

	if (forward  == NULL)
		return (1);

	while (forward != NULL)
	{
		forward = forward->next;
		nodes++;
	}
	nodes--;
	half = nodes / 2;
	while (i <= half)
	{
		half_head = half_head->next;
		i++;
	}
	forward = *head;

	if (nodes == 1)
		return (1);

	if (nodes > 1)
	{
		back = half_head;
		while (half > 0)
		{
			for (i = 0; i < half; i++)
				back = back->next;
			if (forward->n != back->n)
				return (0);
			forward = forward->next;
			back = half_head;
			half--;
		}
	}
	return (1);
}
