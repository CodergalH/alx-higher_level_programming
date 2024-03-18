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

	beginning = *head;

	if (beginning == NULL)
		return (1);
	else
		return (0);
}
