#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle
* @list: list to check
* Return: interger
*/

int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL)
		return (0);

	head = list;
	tail = list->next;

	while (tail != NULL && tail->next != NULL)
	{
		if (head == tail)
			return (1);

		head = head->next;
		tail = tail->next->next;
	}

	return (0);
}
