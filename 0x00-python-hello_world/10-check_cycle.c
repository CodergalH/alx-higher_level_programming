#include "lists.h"

/**
 * check_cycle - check for loop in linked list
 * @list:head of linked list
 *
 * Return: 1 if loop is found, 0 if none
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;


	while (slow_p && fast_p && fast_p->next)
{
	slow_p = slow_p->next;

	fast_p = fast_p->next->next;

	if (slow_p == fast_p)
		return (1);
}
	return (0);
}
