#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	if (*head == NULL)
		return (NULL);

	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *prev = *head

	new_node->n = number;
	new_node->next = prev->next;
	prev->next = new_node;

	return(new_node);
}
