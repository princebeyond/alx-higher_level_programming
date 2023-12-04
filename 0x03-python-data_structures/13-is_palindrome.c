#include "lists.h"

/**
 * is_palindrome - pan
 * @head: head list
 * Return: 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (this_guy(head, *head));

}

/**
 * this_guy - to know if pan
 * @head: head list
 * @end: end
 * Return: 0 or 1
 */
int this_guy(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (this_guy(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
