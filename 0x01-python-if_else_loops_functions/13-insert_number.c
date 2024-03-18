#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *prev;

	prev = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (prev == NULL || prev->n >= number)
	{
		new_node->next = prev;
		*head = new_node;
		return (new_node);
	}

	while (prev && prev->next && prev->next->n < number)
		prev = prev->next;

	new_node->next = prev->next;
	prev->next = new_node;

	return (new_node);
}
