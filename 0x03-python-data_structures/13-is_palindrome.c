#include "lists.h"

/**
 * is_palindrome - checks a single list if it is a palindrome
 * @head: The head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *next = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast)
		slow = slow->next;
	while (prev && slow)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
