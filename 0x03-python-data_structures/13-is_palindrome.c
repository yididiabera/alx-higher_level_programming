#include "lists.h"

/**
 * is_palindrome - checks a single list if it is a palindrome
 * @head: The head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *sl = *head, *f = *head, *pv = NULL, *nt = NULL;

	while (f && f->nt)
	{
		f = f->nt->nt;
		nt = sl->nt;
		sl->nt = pv;
		pv = sl;
		sl = nt;
	}
	if (f)
		sl = sl->nt;
	while (pv && sl)
	{
		if (pv->n != sl->n)
			return (0);
		pv = pv->nt;
		sl = sl->nt;
	}
	return (1);
}
