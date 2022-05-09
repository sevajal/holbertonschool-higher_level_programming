#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	unsigned int i = 0, j = 0;
	const listint_t *forward = *head;
	int list[1024];

	if (head)
	{
		while (forward != NULL)
		{
			list[i] = forward->n;
			forward = forward->next;
			i++;
		}
		i--;
		
		if (i < 2)
			return (1);

		if (i > 1)
		{
			for (j = 0; j <= i; j++)
			{
				if (list[j] != list[i])
					return (0);
				else
					i--;
			}
		}
		return (1);
	}
	return (1);
}
