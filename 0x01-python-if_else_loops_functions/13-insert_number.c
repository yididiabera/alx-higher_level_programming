#include "lists.h"

/**
 * insert_node - it insert a node
 * @head: ptr 
 * @num: number to be added
 * Return: taddress
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint_t *y;
	listint_t *x;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = num;
	if (*head == NULL)
	{
		new->forw = NULL;
		*head = new;
		return(new);
	}
	y = *head;
	if (num < (*head)->n)
	{
		x = *head;
		new->forw = x;
		*head = new;
		return (new);
	}

	while (y->forw != NULL && y->forw->n < num)
		y = y->forw;
	if (y->forw == NULL)
	{
		y->forw = new;
		new->forw = NULL;
		return (new);
	}
	x = y->forw;
	y->forw = new;
	new->forw = x;
	return (new);
}