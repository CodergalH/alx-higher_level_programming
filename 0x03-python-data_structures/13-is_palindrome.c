#include "lists.h"

/**
 * is_palindrome - check if list is empty
 * @head: first node
 *
 * Return: 0 if not, 1 if list is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *beginning;
	int counter;

	beginning = *head;
	counter = 0;
	while (beginning != NULL)
	{
		beginning = beginning->next;
		counter++;
	}

	int i = 0, j;
	listint_t *front, *rear;

	while (i != counter / 2)
	{
		front = rear = beginning;
		for (j = 0; j < i; j++)
			front = front->next;

		for (j = 0; j < counter - (i + 1); j++)
			rear = rear->next;

		if (front->data != rear->data)
			return (0);

		i++;
	}
	return (1);
}
